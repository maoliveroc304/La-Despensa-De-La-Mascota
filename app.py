import streamlit as st
from styles import get_css
from state import init_state, get_cart_count, get_cart_total, navigate_to
# Importamos las vistas (asegúrate de tener los archivos creados)
from views.home import render_home
from views.cart import render_cart
from views.checkout import render_checkout
from views.auth import render_login, render_register

# Configuración inicial
st.set_page_config(layout="wide", page_title="La Despensa de la Mascota", page_icon="🐾")

# Inicializar estado y CSS
init_state()
st.markdown(get_css(), unsafe_allow_html=True)

# --- HEADER FIEL AL ORIGINAL ---
# Creamos un contenedor HTML visual para el fondo azul oscuro
st.markdown("""
<div class="nav-container">
    <div style="display: flex; align-items: center; gap: 10px;">
        <div style="background: rgba(255,255,255,0.1); padding: 8px; border-radius: 50%;">
            <span style="font-size: 24px;">🐾</span>
        </div>
        <div style="line-height: 1.1;">
            <div style="font-weight: bold; font-size: 18px;">La Despensa</div>
            <div style="font-size: 12px; opacity: 0.8;">de la Mascota</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Usamos columnas de Streamlit "flotando" visualmente en la posición correcta mediante margin negativo
# para inyectar la funcionalidad interactiva (botones y búsqueda)
col_spacer, col_search, col_actions = st.columns([2, 4, 3])

with col_search:
    # Barra de búsqueda
    st.text_input("search", placeholder="Buscar croquetas, juguetes...", label_visibility="collapsed")

with col_actions:
    c_user, c_cart = st.columns([1, 1])
    with c_user:
        if st.session_state.get('user_logged_in'):
            st.button("👤 Mi Cuenta", key="btn_account")
        else:
            if st.button("👤 Ingresar", key="btn_login_nav"):
                navigate_to('login')
    with c_cart:
        count = get_cart_count()
        total = get_cart_total()
        # Botón de carrito con información dinámica
        if st.button(f"🛒 S/. {total:.2f}", key="btn_cart_nav"):
            navigate_to('cart')

# Separador invisible para bajar el contenido del header sticky
st.markdown("<div style='margin-bottom: 30px;'></div>", unsafe_allow_html=True)

# --- ROUTER ---
page = st.session_state.page

if page == 'home':
    render_home()
elif page == 'cart':
    render_cart()
elif page == 'checkout':
    render_checkout()
elif page == 'login':
    render_login()
elif page == 'register':
    render_register()
elif page == 'confirmation':
    from views.checkout import render_confirmation # Si tienes esto separado
    render_confirmation()

# --- FOOTER (Opcional, simple) ---
st.markdown("<br><br><div style='text-align:center; color:gray; font-size:12px;'>© 2024 Tienda Buendía</div>", unsafe_allow_html=True)
