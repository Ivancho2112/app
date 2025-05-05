import streamlit as st
import random

# Título de la app
st.title("Simulación Interactiva: Problema de Monty Hall – Corrección de Selección")

# --- Funciones de estado ---
def initialize():
    st.session_state.step = 1
    st.session_state.door = random.choice([1, 2, 3])
    st.session_state.chosen = None
    st.session_state.opened = None
    st.session_state.result = None
    st.session_state.reset_game = False

# Inicializar o reiniciar
if 'step' not in st.session_state or st.session_state.reset_game:
    initialize()

# --- Paso 1: Selección de puerta ---
if st.session_state.step == 1:
    choice = st.radio("Elige una puerta:", [1, 2, 3], key="radio_choice")
    if st.button("Confirmar elección", key="confirm_button"):
        st.session_state.chosen = choice
        # Abrir una puerta vacía
        available = [d for d in [1, 2, 3] if d != choice and d != st.session_state.door]
        st.session_state.opened = random.choice(available)
        st.session_state.step = 2
        st.experimental_rerun()

# --- Paso 2: Oferta de cambio ---
elif st.session_state.step == 2:
    st.write(f"El anfitrión abre la puerta {st.session_state.opened}, está vacía.")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Me quedo con mi elección", key="stay_button"):
            st.session_state.result = (st.session_state.chosen == st.session_state.door)
            st.session_state.step = 3
            st.experimental_rerun()
    with col2:
        if st.button("Cambio de puerta", key="switch_button"):
            remaining = next(d for d in [1, 2, 3] if d not in (st.session_state.chosen, st.session_state.opened))
            st.session_state.chosen = remaining
            st.session_state.result = (remaining == st.session_state.door)
            st.session_state.step = 3
            st.experimental_rerun()

# --- Paso 3: Revelar resultado ---
elif st.session_state.step == 3:
    st.write(f"Tu elección final fue la puerta {st.session_state.chosen}.")
    if st.session_state.result:
        st.success("¡Ganaste el premio 🎉!")
    else:
        st.error("Lo siento, no hay premio 😞")
    # Botón para reiniciar
    if st.button("Jugar otra vez", key="reset_button"):
        st.session_state.reset_game = True
        st.experimental_rerun()

