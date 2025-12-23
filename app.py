import streamlit as st
from styles import get_css
from state import init_state, get_cart_count, get_cart_total, navigate_to
from views.home import render_home
from views.cart import render_cart
from views.checkout import render_checkout
from views.auth import render_login, render_register # Asumiendo que creas estos archivos similares

# Configuración inicial
st.set_page_config(layout="wide", page_title="La Despensa de la Mascota", page_icon="🐾")

# Inicializar estado y CSS
init_state()
st.markdown(get_css(), unsafe_allow_html=True)

# --- HEADER PERSONALIZADO ---
# Usamos un contenedor sticky simulado con CSS (.nav-container) y columnas de Streamlit dentro.
st.markdown('<div class="nav-container">', unsafe_allow_html=True)
col_logo, col_search, col_actions = st.columns([2, 3, 2])

with col_logo:
    # Usamos markdown con html para el logo
    if st.button("🐾 La Despensa", key="btn_logo"):
        navigate_to('home')

with col_search:
    st.text_input("search", placeholder="Buscar croquetas, juguetes...", label_visibility="collapsed")

with col_actions:
    # Mostramos resumen del carrito
    count = get_cart_count()
    total = get_cart_total()
    label = f"🛒 {count} items | S/. {total:.2f}"
    
    c_login, c_cart = st.columns(2)
    with c_login:
        if st.button("👤 Ingresar"):
            navigate_to('login')
    with c_cart:
        if st.button(label):
            navigate_to('cart')

st.markdown('</div>', unsafe_allow_html=True)

# --- ROUTER DE VISTAS ---
page = st.session_state.page

if page == 'home':
    render_home()
elif page == 'cart':
    render_cart()
elif page == 'checkout':
    render_checkout()
elif page == 'login':
    # Implementación simple inline o importar de views/auth.py
    st.markdown("### Iniciar Sesión")
    st.text_input("Usuario")
    st.text_input("Contraseña", type="password")
    if st.button("Entrar"):
        navigate_to('home')
elif page == 'register':
    st.markdown("### Registro")
    # Campos de registro...
    if st.button("Crear Cuenta"):
        navigate_to('home')

# --- FOOTER ---
st.markdown("""
<div class="footer-sec">
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 2rem;">
        <div>
            <h4>La Despensa de la Mascota</h4>
            <p style="opacity: 0.7; font-size: 0.9rem;">Tu tienda de confianza con precios de barrio.</p>
        </div>
        <div>
            <h4>Contacto</h4>
            <p>📍 Av. Próceres de la Independencia 1234</p>
            <p>📞 (01) 345-6789</p>
        </div>
        <div>
            <h4>Encuéntranos</h4>
            <p>Aceptamos Yape, Plin, Visa</p>
        </div>
    </div>
    <div style="margin-top: 2rem; border-top: 1px solid rgba(255,255,255,0.1); padding-top: 1rem; font-size: 0.8rem; opacity: 0.6;">
        © 2024 Tienda Buendía. Todos los derechos reservados.
    </div>
</div>
""", unsafe_allow_html=True)
