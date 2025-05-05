import streamlit as st
import random

st.title("Simulación Interactiva: Problema de Monty Hall")

# --- Inicializar estado ---
if 'step' not in st.session_state:
    st.session_state.step = 1
    st.session_state.door = random.choice([1, 2, 3])
    st.session_state.chosen = None
    st.session_state.opened = None
    st.session_state.result = None

# --- Paso 1: Selección ---
if st.session_state.step == 1:
    choice = st.radio("Elige una puerta:", [1, 2, 3], key="radio_choice")
    if st.button("Confirmar elección", key="confirm_button"):
        st.session_state.chosen = choice
        # Abrir una puerta vacía
        available = [d for d in [1, 2, 3] if d != choice and d != st.session_state.door]
        st.session_state.opened = random.choice(available)
        st.session_state.step = 2

# --- Paso 2: Ofrecer cambio ---
elif st.session_state.step == 2:
    st.write(f"El anfitrión abre la puerta {st.session_state.opened}, está vacía.")
    col1, col2 = st.columns(2)
    if col1.button("Me quedo con mi elección", key="stay_button"):
        st.session_state.result = (st.session_state.chosen == st.session_state.door)
        st.session_state.step = 3
    if col2.button("Cambio de puerta", key="switch_button"):
        remaining = next(d for d in [1, 2, 3] if d not in (st.session_state.chosen, st.session_state.opened))
        st.session_state.chosen = remaining
        st.session_state.result = (remaining == st.session_state.door)
        st.session_state.step = 3

# --- Paso 3: Mostrar resultado ---
elif st.session_state.step == 3:
    st.write(f"Tu elección final fue la puerta {st.session_state.chosen}.")
    if st.session_state.result:
        st.success("¡Ganaste el premio 🎉!")
    else:
        st.error("Lo siento, no hay premio 😞")
    if st.button("Jugar otra vez", key="reset_button"):
        for key in ['step', 'door', 'chosen', 'opened', 'result']:
            del st.session_state[key]
