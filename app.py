import streamlit as st
from styles import get_css
from state import init_state, get_cart_count, get_cart_total, navigate_to
# Importar vistas
from views.home import render_home
from views.cart import render_cart
from views.checkout import render_checkout
from views.auth import render_login, render_register

# --- CONFIGURACIÓN ---
st.set_page_config(layout="wide", page_title="La Despensa de la Mascota", page_icon="🐾")
init_state()

# Inyectamos CSS
st.markdown(get_css(), unsafe_allow_html=True)

# ==========================================
# HEADER ADAPTADO DE STITCH
# ==========================================

# 1. Fondo Azul Fijo (Visual)
st.markdown('<div class="header-bg"></div>', unsafe_allow_html=True)

# 2. Contenedor Interactivo (Sobre el fondo)
# Usamos un container para agrupar y columnas para distribuir
header_container = st.container()

with header_container:
    # Definimos columnas: Logo (Izquierda), Buscador (Centro), Acciones (Derecha)
    # Ratios ajustados para parecerse a tu imagen: [2, 3, 2]
    col1, col2, col3 = st.columns([2, 3, 2], gap="medium")

    # --- COLUMNA 1: LOGO ---
    with col1:
        # Envolvemos el botón en un div para aplicar el CSS .logo-btn
        st.markdown('<div class="logo-btn">', unsafe_allow_html=True)
        # El botón actúa como el texto clickeable "La Despensa..."
        if st.button("🐾 La Despensa de la Mascota", key="logo_home"):
            navigate_to('home')
        st.markdown('</div>', unsafe_allow_html=True)
        # Subtítulo (visual, no clickeable)
        st.markdown('<div class="logo-subtext">por Tienda Buendía</div>', unsafe_allow_html=True)

    # --- COLUMNA 2: BUSCADOR ---
    with col2:
        # Envolvemos en .search-container para hacerlo redondo y blanco
        st.markdown('<div class="search-container">', unsafe_allow_html=True)
        # Usamos label_visibility="collapsed" para ocultar la etiqueta
        search_query = st.text_input("search", placeholder="🔍 Buscar croquetas, juguetes...", label_visibility="collapsed")
        st.markdown('</div>', unsafe_allow_html=True)
        
        # (Opcional) Lógica de búsqueda
        if search_query:
            # Aquí podrías filtrar productos
            pass

    # --- COLUMNA 3: ACCIONES (Cuenta y Carrito) ---
    with col3:
        # Sub-columnas para alinear los botones a la derecha
        # Usamos columnas vacías a la izquierda para empujar
        c_spacer, c_acc, c_cart = st.columns([0.5, 1, 1.2])
        
        with c_acc:
            st.markdown('<div class="action-btn">', unsafe_allow_html=True)
            # Icono de persona simulado con texto o emoji
            user_label = "👤 Mi Cuenta"
            if st.session_state.get('user_logged_in'):
                user_label = "👤 Perfil"
                
            if st.button(user_label, key="btn_account_header"):
                if not st.session_state.get('user_logged_in'):
                    navigate_to('login')
            st.markdown('</div>', unsafe_allow_html=True)

        with c_cart:
            # Calculamos totales
            count = get_cart_count()
            total = get_cart_total()
            
            # Badge visual (HTML puro superpuesto)
            if count > 0:
                st.markdown(f'<div class="cart-badge">{count}</div>', unsafe_allow_html=True)
            
            st.markdown('<div class="action-btn">', unsafe_allow_html=True)
            # Botón del carrito
            cart_label = f"🛒 S/. {total:.2f}"
            if st.button(cart_label, key="btn_cart_header"):
                navigate_to('cart')
            st.markdown('</div>', unsafe_allow_html=True)

# Espaciador para que el contenido de la página no quede oculto tras el header fijo
st.markdown('<div style="height: 80px;"></div>', unsafe_allow_html=True)

# ==========================================
# CONTENIDO DE LA PÁGINA
# ==========================================

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
    from views.checkout import render_confirmation # Asegúrate de tener esto en views/checkout.py
    render_confirmation()

# ==========================================
# FOOTER
# ==========================================
# (Aquí puedes adaptar el footer de Stitch usando st.markdown con HTML puro si lo deseas estático)
