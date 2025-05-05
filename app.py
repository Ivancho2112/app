import streamlit as st
import random

st.title("Simulación Interactiva: Problema de Monty Hall")

# Inicializar juego
if 'door' not in st.session_state:
    st.session_state.door = random.choice([1,2,3])
    st.session_state.chosen = None
    st.session_state.opened = None
    st.session_state.switched = False

# Paso 1: elige puerta
if st.session_state.chosen is None:
    choice = st.radio("Elige una puerta:", [1,2,3])
    if st.button("Confirmar elección"):
        st.session_state.chosen = choice
        # abrir una puerta vacía
        options = [d for d in [1,2,3] if d != st.session_state.chosen and d != st.session_state.door]
        st.session_state.opened = random.choice(options)

# Paso 2: ofrecer cambio
if st.session_state.chosen is not None and st.session_state.opened is not None:
    st.write(f"El anfitrión abre la puerta {st.session_state.opened}, está vacía.")
    if not st.session_state.switched:
        if st.button("Me quedo con mi elección"):
            pass
        if st.button("Cambio de puerta"):
            remaining = next(d for d in [1,2,3] if d not in (st.session_state.chosen, st.session_state.opened))
            st.session_state.chosen = remaining
            st.session_state.switched = True

# Paso 3: revelar el premio
if st.session_state.chosen is not None and (st.session_state.switched or st.session_state.opened):
    if st.session_state.chosen == st.session_state.door:
        st.success("¡Ganaste el premio 🎉!")
    else:
        st.error("Lo siento, no hay premio 😞")
    if st.button("Jugar otra vez"):
        for k in ['door','chosen','opened','switched']:
            del st.session_state[k]
        st.experimental_rerun()
