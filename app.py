import streamlit as st
from styles import get_css
# Asumimos que tienes estas carpetas y archivos creados como en la iteración anterior
from state import init_state, get_cart_count, get_cart_total, navigate_to
from views.home import render_home
from views.cart import render_cart
from views.checkout import render_checkout
from views.auth import render_login, render_register

# --- CONFIGURACIÓN INICIAL ---
st.set_page_config(layout="wide", page_title="La Despensa de la Mascota", page_icon="🐾")
init_state() # Inicializa variables de sesión

# Inyectar estilos CSS
st.markdown(get_css(), unsafe_allow_html=True)

# ==============================================================================
# HEADER HÍBRIDO: APARIENCIA DE HTML + FUNCIONALIDAD DE PYTHON
# ==============================================================================

# 1. El Fondo Azul (Pura decoración visual, posición fija)
st.markdown('<div class="header-bg"></div>', unsafe_allow_html=True)

# 2. El Contenido Funcional (Widgets de Streamlit superpuestos)
# Usamos un contenedor para centrar el contenido (max-w-1280px equivalente)
with st.container():
    # Creamos columnas con proporciones ajustadas al diseño HTML
    # [Logo 20%] [Buscador 40%] [Acciones 40%]
    c_logo, c_search, c_actions = st.columns([2, 4, 3])

    # --- LOGO (Izquierda) ---
    with c_logo:
        st.markdown('<div class="logo-btn" style="display:flex; align-items:center; gap:10px;">', unsafe_allow_html=True)
        # Icono visual (HTML)
        st.markdown("""
            <div style="background:rgba(255,255,255,0.1); padding:8px; border-radius:50%; width:40px; height:40px; display:flex; justify-content:center; align-items:center; float:left; margin-right:10px;">
                <span style="font-size:20px;">🐾</span>
            </div>
        """, unsafe_allow_html=True)
        # Botón funcional invisible encima del texto
        if st.button("La Despensa\nde la Mascota", key="logo_home_btn"):
            navigate_to('home')
        st.markdown('</div>', unsafe_allow_html=True)

    # --- BUSCADOR (Centro) ---
    with c_search:
        # El CSS se encarga de hacerlo redondo y ponerle la lupa
        st.text_input("search", placeholder="Buscar croquetas, juguetes...", label_visibility="collapsed")

    # --- ACCIONES (Derecha) ---
    with c_actions:
        # Sub-columnas para alinear a la derecha
        cc1, cc2, cc3 = st.columns([1, 1.5, 2])
        
        with cc2: # Botón Usuario
            st.markdown('<div class="nav-btn">', unsafe_allow_html=True)
            label_user = "👤 Mi Cuenta"
            if st.session_state.get('user_logged_in'):
                label_user = "👤 Perfil"
            
            if st.button(label_user, key="header_user"):
                if not st.session_state.get('user_logged_in'):
                    navigate_to('login')
            st.markdown('</div>', unsafe_allow_html=True)

        with cc3: # Botón Carrito
            count = get_cart_count()
            total = get_cart_total()
            
            # Badge rojo visual
            if count > 0:
                # Usamos posición relativa para que el badge flote sobre el botón
                st.markdown(f"""
                <div style="position:relative; width: fit-content; margin: 0 auto;">
                    <div class="cart-badge">{count}</div>
                </div>
                """, unsafe_allow_html=True)

            st.markdown('<div class="nav-btn">', unsafe_allow_html=True)
            # El botón muestra el total, tal cual el diseño
            label_cart = f"🛒 S/. {total:.2f}"
            if st.button(label_cart, key="header_cart"):
                navigate_to('cart')
            st.markdown('</div>', unsafe_allow_html=True)

# Espaciador invisible para empujar el contenido hacia abajo (ya que el header es fijo)
st.markdown('<div style="margin-bottom: 90px;"></div>', unsafe_allow_html=True)

# ==============================================================================
# CONTENIDO DE LA PÁGINA (Router)
# ==============================================================================
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
    # Si aún no tienes confirmation.py, puedes poner el contenido aquí directo
    st.balloons()
    st.markdown("""
    <div style="text-align:center; padding: 50px;">
        <h1 style="color:#001f3f;">¡Pedido Registrado! 🎉</h1>
        <p>Gracias por tu compra.</p>
        <button style="background-color:#25D366; color:white; padding:10px 20px; border-radius:20px; border:none; margin-top:20px;">
            Enviar constancia al WhatsApp
        </button>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Volver al Inicio"):
        navigate_to('home')

# ==============================================================================
# FOOTER
# ==============================================================================
st.markdown("""
<div style="background-color:#001f3f; color:white; padding:40px; margin-top:50px; text-align:center; font-size:14px;">
    <p style="opacity:0.7;">© 2024 Tienda Buendía. Todos los derechos reservados.</p>
</div>
""", unsafe_allow_html=True)
