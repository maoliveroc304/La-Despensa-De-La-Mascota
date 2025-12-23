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

# Inyectamos el CSS
st.markdown(get_css(), unsafe_allow_html=True)

# --- HEADER MEJORADO ---
# 1. El div azul de fondo (puramente visual)
st.markdown('<div class="header-background"></div>', unsafe_allow_html=True)

# 2. Los controles interactivos encima del fondo
# Usamos un contenedor para agrupar los inputs del header
with st.container():
    # Creamos 3 columnas: Logo (grande), Buscador (muy grande), Acciones (ajustado)
    # Ajusta los ratios [2, 4, 2] según necesites más espacio
    col_logo, col_search, col_actions = st.columns([2, 4, 2], gap="small")

    with col_logo:
        # LOGO CLICKEABLE
        # Usamos un botón "secondary" (transparente por CSS) que simula ser el logo.
        # \n fuerza un salto de línea para el subtítulo
        if st.button("🐾 La Despensa\npor Tienda Buendía", type="secondary", key="logo_home_btn"):
            navigate_to('home')

    with col_search:
        # BARRA DE BÚSQUEDA
        # El CSS la hará blanca y redondeada
        st.text_input("search", placeholder="Buscar croquetas, juguetes...", label_visibility="collapsed", key="header_search")

    with col_actions:
        # BOTONES DERECHA (Mi Cuenta | Carrito)
        c_acc, c_cart = st.columns(2)
        
        with c_acc:
            # Lógica para mostrar nombre si está logueado
            user_label = "👤 Mi Cuenta"
            if st.session_state.get('user_logged_in'):
                user_label = "👤 Perfil"
                
            # Usamos type="secondary" para que tome el estilo transparente del header
            if st.button(user_label, type="secondary", key="btn_account"):
                if st.session_state.get('user_logged_in'):
                    # Ir a perfil (opcional)
                    pass 
                else:
                    navigate_to('login')
                    
        with c_cart:
            # Badge y Total
            count = get_cart_count()
            total = get_cart_total()
            
            # Icono de carrito con badge simulado en texto
            cart_label = f"🛒"
            if count > 0:
                cart_label += f" ({count})"
            cart_label += f" S/. {total:.2f}"
            
            if st.button(cart_label, type="secondary", key="btn_cart_top"):
                navigate_to('cart')

# Espacio para separar el contenido del header fijo (80px de altura visual)
st.markdown("<div style='margin-bottom: 50px;'></div>", unsafe_allow_html=True)

# --- ROUTER DE PÁGINAS ---
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
    from views.checkout import render_confirmation # Asegúrate de tener esta función o definirla
    render_confirmation()

# --- FOOTER ---
st.markdown("<br><hr><div style='text-align:center; color:#888; font-size:12px; padding:20px;'>© 2025 Tienda Buendía - Todos los derechos reservados</div>", unsafe_allow_html=True)
