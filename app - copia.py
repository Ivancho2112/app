import streamlit as st
import random

# Título de la app
st.title("Simulación Interactiva: Problema de Monty Hall")

# --- Inicialización del estado de sesión ---
def init():
    st.session_state.door = random.choice([1, 2, 3])
    st.session_state.chosen = None
    st.session_state.opened = None
    st.session_state.result = None
    st.session_state.reset_game = False

if 'door' not in st.session_state or st.session_state.reset_game:
    init()

# --- Paso 1: Seleccionar puerta ---
if st.session_state.chosen is None:
    choice = st.radio("Elige una puerta:", [1, 2, 3], key="radio_choice")
    if st.button("Confirmar elección", key="confirm"):  
        st.session_state.chosen = choice
        # Abrir una puerta vacía
        options = [d for d in [1, 2, 3] 
                   if d != st.session_state.chosen 
                   and d != st.session_state.door]
        st.session_state.opened = random.choice(options)

# --- Paso 2: Ofrecer cambio ---
elif st.session_state.result is None:
    st.write(f"El anfitrión abre la puerta {st.session_state.opened}, está vacía.")
    col1, col2 = st.columns(2)
    # Quedarse
    if col1.button("Me quedo con mi elección", key="stay"):  
        st.session_state.result = (st.session_state.chosen == st.session_state.door)
    # Cambiar\    
    if col2.button("Cambio de puerta", key="switch"):  
        remaining = next(d for d in [1, 2, 3] 
                         if d not in (st.session_state.chosen, st.session_state.opened))
        st.session_state.chosen = remaining
        st.session_state.result = (st.session_state.chosen == st.session_state.door)

# --- Paso 3: Revelar resultado ---
if st.session_state.result is not None:
    # Mostrar elección final y resultado
    st.write(f"Tu elección final fue la puerta {st.session_state.chosen}.")
    if st.session_state.result:
        st.success("¡Ganaste el premio 🎉!")
    else:
        st.error("Lo siento, no hay premio 😞")
    # Botón para reiniciar
    if st.button("Jugar otra vez", key="reset"):  
        st.session_state.reset_game = True
        st.experimental_rerun()
