import streamlit as st
import time

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(
    page_title="La Despensa de la Mascota",
    page_icon="🐾",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- ESTILOS CSS PERSONALIZADOS (Para imitar el look de Tailwind) ---
st.markdown("""
<style>
    .main-header {font-size: 2.5rem; font-weight: 800; color: #001f3f;}
    .sub-header {font-size: 1.5rem; font-weight: 600; color: #FF4500;}
    .price-tag {font-size: 1.2rem; font-weight: bold; color: #FF4500;}
    .original-price {text-decoration: line-through; color: gray; font-size: 0.9rem;}
    .card {background-color: #f9f9f9; padding: 20px; border-radius: 10px; box-shadow: 2px 2px 5px rgba(0,0,0,0.1); margin-bottom: 20px;}
    .stButton>button {width: 100%; border-radius: 20px;}
    .big-button>button {background-color: #FF4500; color: white; font-weight: bold; padding: 10px;}
</style>
""", unsafe_allow_html=True)

# --- DATOS (Convertidos de constants.ts) ---
CATEGORIES = [
    {"name": 'Perros', "image": 'https://lh3.googleusercontent.com/aida-public/AB6AXuBxJJZQSRTQ0d3RKsd0GOtVnS2laFdNxXf9XMNVqwESzzv5kQHJ4FIAMm94jgbMECYVE0KC95XAsPxbd7Fg6y4TJkwqixQKRRS2SCWdT5Bd8EZbrGMfX8_csIhZQ2uBErN0k2drBCBhCSyfI7V78EQ6q_2vg94eFt95QP4FGgrPDnAZkKBT-XYRnxYXkDOBfjR52nT9wvepDdpoaLuaPGc18T3I988FjsB_fm1idg_rpi7_BFnQqEj7mtVp6fjDEPHMsZfOL2Zowms'},
    {"name": 'Gatos', "image": 'https://lh3.googleusercontent.com/aida-public/AB6AXuDLvRHsyjVQP1uhoCOkONZCFixnoFHiw5Z1xtRkqK4V4pblh4UkWmnuKV_2P3TR27duVlNHU6s36T32AcImaBNFrW7eznG5lfP0UnlX5TyS7u27uCWU81sTzkPnxh4WDgZ1QOk3qNwQFRYpKKXiIEJP2WIA6hZuiHDYi66VDrNsP2f0G-h5749WP_z-pKIZKSqJ2QSNMDWjRnyY5MuyRcFX75jmgdkE3Dh62ZNN0YCfgrCYige7tbZdWzwOG13ZXsJPW-mBmsaM-Gg'},
    {"name": 'Limpieza', "image": 'https://lh3.googleusercontent.com/aida-public/AB6AXuBsKUPgikB3fJs3ojUHfn_CM-8Dy6PtMWCV1M6dGElH5ReNOAbRGCTZK1U_zxNCOR9ol-qgfzVtVP_XnB5ygpins7xh17Jd5gEguXz4-WzTy3pvEi5Bo2JFvIBrOl8kq6nDn-5CmZ68LrLaDdhdXw7aiyLOAqF0yjIwoVWIttgbmCNaVWMHJwmeYgr6Vu4hpIuxDJGMag_TbD453HanYAP4kIW1qBgZL2wiEC_k97dey-SZmfRJRGOtSLo6HxAtA3QK9zSc-LlEb1I'},
    {"name": 'Accesorios', "image": 'https://lh3.googleusercontent.com/aida-public/AB6AXuDrzlDhbGO8MTcJcZxJANrICy-xhP89_rBDxjx0tK2Z8HsCGtZihpmd21FiDgnwMuZeYSsuiQTdjNVNCZ6x9MvoEUVHTxATxSyVEbrhIl3BJRJc-COSOAE2LPDKCvtjntIIzf5Uezv-85VQWu43eaVHB_Aco7_n_bt6pC9mYYSTzfaShdSLQFZObH-MMMo4XzKV9tScapf6SeJrD-9jW2lDRoF-truwTBfH9pkTkbmzLD0JCUqhkHbxrTz9iAC35Mnnr0QHJwpk1YA'},
]

PRODUCTS = [
    {
        "id": 1,
        "name": 'Ricocan Cordero y Cereales 15kg',
        "category": 'Perros - Alimento Seco',
        "price": 119.00,
        "originalPrice": 140.00,
        "image": 'https://lh3.googleusercontent.com/aida-public/AB6AXuB3Z1LMZsb74Tgm4Cdh1NMPZkSL8GB__pXbsiyqQiyL2faccfvknLupd0mIUrZUg21s-PggD_RMTBlxDgiiaiSilpfny7A0F9W31Cv2Em_QRo1wYXLs1RcxPnAMj4rJqn4YxlTUp3ac9Rqp-fRTxVYJI4jO__tswqLtZH-ucX4STrjSFuNuIZMutrtmJQAVPwMuOKrC7j6ng0L3vIc-tYRfzwfaLRnHRKhNPNhq48nkeD6ewUYIpuckVMjlRwX0CGiB8OcovDKBUA8',
        "badge": '-15%',
        "description": 'Saco 15kg'
    },
    {
        "id": 2,
        "name": 'Ricocat Atún y Sardinas 9kg',
        "category": 'Gatos - Alimento Seco',
        "price": 85.00,
        "originalPrice": 0,
        "image": 'https://lh3.googleusercontent.com/aida-public/AB6AXuBKCo8V8QDG2SAZBukKaZ8D8HDpP5iAdequtjJM52Cl7DdstyFKI-h5bT7ikgc6akCZkKh5dpxASuLMayYRV5PKOepgBpwZfRTiblJxhX3IfCx9G5Ql6zNElkpTYGjHM4rGvyvujKHnh0VtmlBrQRrA-FV3RMpy1elDWCTieVyIZE_sejTAfbom39OiZytu31dTEl5XZ8bDOktGsZiQv5fUeadhaB23DuUQuQt53Lq6Hjvisg9EIucJE5owEjeF1MKf8pv2wkQwseA'
    },
    {
        "id": 3,
        "name": 'Hueso de Goma Resistente',
        "category": 'Juguetes - Perros',
        "price": 25.50,
        "originalPrice": 0,
        "image": 'https://lh3.googleusercontent.com/aida-public/AB6AXuDYlSHN0ihN9GWy8Ixg5SkN_LmV3g4svzUUE8T1GOvttUR2Vzs_vVCnqfM5l9k2E2ap1YvC4JJEizq0Bo6GCqOWIGy7dNL_xLgSJpQEsRIXRgkQVgq4kDZuCd7sU9EIgIqIhtJ5VMX932AOOAkmZYQP-eoezJNLwtKtATXOnXC4x2kDkq0sjXHwyv4Gi6E-sk0p8cEnvQuW55KvNA48Nx2QI12xPdztXGq-tYBioWsSem8oW2TaUOSgv8yq7Ux2rKtYupITY2Cd7ZU',
        "description": 'Azul, Talla M'
    },
    {
        "id": 4,
        "name": 'Shampoo Antipulgas 400ml',
        "category": 'Higiene - General',
        "price": 32.00,
        "originalPrice": 38.00,
        "image": 'https://lh3.googleusercontent.com/aida-public/AB6AXuDsuVxadySIdQfFR3W32inefrZh7BcWmzCnla6FpYVAfCTeCGK5rTWsSYFf5FLwwGAtTUy33YNK46Ad-mhHQQKOGEgvog9YJ110IeNv59vwAICfqoqTdTY90vBUDkDIRqnbpyJqKXdt_9Pu94OybLQ7h26cCrkQPVGcFxoL1MXb1h6KA0P6mWDllW6YML62mBS5XdjzoPu54kFbc1n2aNYA3bSOi-PlbMN5m9WzwthdBPb2TCDB-GYZWpSwEomsvQkHlyWZXK4npd0',
        "badge": 'OFERTA',
        "description": 'Uso veterinario'
    },
    {
        "id": 5,
        "name": 'Spray Limpiador 300ml',
        "category": 'Higiene',
        "price": 28.90,
        "originalPrice": 0,
        "image": 'https://lh3.googleusercontent.com/aida-public/AB6AXuDsuVxadySIdQfFR3W32inefrZh7BcWmzCnla6FpYVAfCTeCGK5rTWsSYFf5FLwwGAtTUy33YNK46Ad-mhHQQKOGEgvog9YJ110IeNv59vwAICfqoqTdTY90vBUDkDIRqnbpyJqKXdt_9Pu94OybLQ7h26cCrkQPVGcFxoL1MXb1h6KA0P6mWDllW6YML62mBS5XdjzoPu54kFbc1n2aNYA3bSOi-PlbMN5m9WzwthdBPb2TCDB-GYZWpSwEomsvQkHlyWZXK4npd0'
    },
    {
        "id": 6,
        "name": 'Pack Premios DogChow',
        "category": 'Snacks',
        "price": 15.90,
        "originalPrice": 18.90,
        "image": 'https://lh3.googleusercontent.com/aida-public/AB6AXuB3Z1LMZsb74Tgm4Cdh1NMPZkSL8GB__pXbsiyqQiyL2faccfvknLupd0mIUrZUg21s-PggD_RMTBlxDgiiaiSilpfny7A0F9W31Cv2Em_QRo1wYXLs1RcxPnAMj4rJqn4YxlTUp3ac9Rqp-fRTxVYJI4jO__tswqLtZH-ucX4STrjSFuNuIZMutrtmJQAVPwMuOKrC7j6ng0L3vIc-tYRfzwfaLRnHRKhNPNhq48nkeD6ewUYIpuckVMjlRwX0CGiB8OcovDKBUA8',
        "badge": '-15%'
    },
    {
        "id": 7,
        "name": 'Collar Antipulgas Seresto',
        "category": 'Salud',
        "price": 145.00,
        "originalPrice": 0,
        "image": 'https://lh3.googleusercontent.com/aida-public/AB6AXuDYlSHN0ihN9GWy8Ixg5SkN_LmV3g4svzUUE8T1GOvttUR2Vzs_vVCnqfM5l9k2E2ap1YvC4JJEizq0Bo6GCqOWIGy7dNL_xLgSJpQEsRIXRgkQVgq4kDZuCd7sU9EIgIqIhtJ5VMX932AOOAkmZYQP-eoezJNLwtKtATXOnXC4x2kDkq0sjXHwyv4Gi6E-sk0p8cEnvQuW55KvNA48Nx2QI12xPdztXGq-tYBioWsSem8oW2TaUOSgv8yq7Ux2rKtYupITY2Cd7ZU'
    }
]

# --- GESTIÓN DE ESTADO (Session State) ---
# Replica el CartContext de React
if 'cart' not in st.session_state:
    st.session_state.cart = [] # Lista de diccionarios {product, quantity}

if 'page' not in st.session_state:
    st.session_state.page = 'home'

# --- FUNCIONES DE LÓGICA ---
def navigate_to(page_name):
    st.session_state.page = page_name
    st.rerun()

def add_to_cart(product):
    found = False
    for item in st.session_state.cart:
        if item['id'] == product['id']:
            item['quantity'] += 1
            found = True
            break
    if not found:
        new_item = product.copy()
        new_item['quantity'] = 1
        st.session_state.cart.append(new_item)
    st.toast(f"Agregado: {product['name']}", icon="🛒")

def remove_from_cart(product_id):
    st.session_state.cart = [item for item in st.session_state.cart if item['id'] != product_id]
    st.rerun()

def update_quantity(product_id, delta):
    for item in st.session_state.cart:
        if item['id'] == product_id:
            new_qty = item['quantity'] + delta
            if new_qty >= 1:
                item['quantity'] = new_qty
    st.rerun()

def get_cart_total():
    return sum(item['price'] * item['quantity'] for item in st.session_state.cart)

def get_cart_count():
    return sum(item['quantity'] for item in st.session_state.cart)

# --- COMPONENTES UI (Views) ---

def header_component():
    col1, col2, col3 = st.columns([1, 2, 1])
    with col1:
        if st.button("🐾 La Despensa"):
            navigate_to('home')
    with col2:
        st.text_input("Buscar...", placeholder="Buscar croquetas, juguetes...", label_visibility="collapsed")
    with col3:
        cart_count = get_cart_count()
        cart_total = get_cart_total()
        btn_label = f"🛒 Carrito ({cart_count}) - S/. {cart_total:.2f}"
        if st.button(btn_label):
            navigate_to('cart')
    st.divider()

def footer_component():
    st.divider()
    cols = st.columns(4)
    with cols[0]:
        st.markdown("**La Despensa de la Mascota**")
        st.caption("Tu tienda de confianza con precios de barrio.")
    with cols[1]:
        st.markdown("**Contacto**")
        st.text("📍 San Juan de Lurigancho")
        st.text("📞 (01) 345-6789")
    with cols[2]:
        st.markdown("**Redes**")
        st.text("Facebook | Instagram | TikTok")
    with cols[3]:
        st.markdown("© 2024 Tienda Buendía")

# --- PÁGINAS ---

def home_page():
    # Hero Section
    st.markdown("""
    <div style="background-color: #001f3f; padding: 40px; border-radius: 15px; color: white; text-align: left; margin-bottom: 30px;">
        <span style="background-color: #FF4500; padding: 5px 10px; border-radius: 15px; font-size: 0.8em; font-weight: bold;">SOLO LO MEJOR</span>
        <h1 style="margin-top: 10px;">Todo para tu engreído,<br><span style="color: #FF4500;">precios de barrio.</span></h1>
        <p>Delivery rápido a todo San Juan de Lurigancho.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Categorías
    st.markdown("### Categorías Populares")
    cat_cols = st.columns(len(CATEGORIES))
    for i, cat in enumerate(CATEGORIES):
        with cat_cols[i]:
            st.image(cat['image'], caption=cat['name'], use_container_width=True)

    st.markdown("---")

    # Productos Destacados
    st.markdown("### Productos Destacados")
    
    # Grid de productos (usando columnas)
    prod_cols = st.columns(4)
    
    for i, product in enumerate(PRODUCTS):
        col_idx = i % 4
        with prod_cols[col_idx]:
            with st.container(border=True):
                # Badge
                if "badge" in product:
                    st.markdown(f":red_circle: **{product['badge']}**")
                
                st.image(product['image'], use_container_width=True)
                st.markdown(f"**{product['name']}**")
                st.caption(product['category'])
                
                # Precios
                if product.get('originalPrice', 0) > 0:
                    st.markdown(f"<span class='original-price'>S/. {product['originalPrice']:.2f}</span>", unsafe_allow_html=True)
                st.markdown(f"<span class='price-tag'>S/. {product['price']:.2f}</span>", unsafe_allow_html=True)
                
                if st.button("Agregar", key=f"add_{product['id']}"):
                    add_to_cart(product)

    # Sección de sugerencias
    st.markdown("---")
    st.info("¿No encuentras lo que buscas? Somos tu tienda de barrio. Escríbenos y lo conseguimos.")

def cart_page():
    st.markdown("## 🛒 Carrito de Compras")
    
    if not st.session_state.cart:
        st.warning("Tu carrito está vacío.")
        if st.button("Ir a comprar"):
            navigate_to('home')
        return

    col_items, col_summary = st.columns([2, 1])

    with col_items:
        for item in st.session_state.cart:
            with st.container(border=True):
                c1, c2, c3, c4 = st.columns([1, 3, 2, 1])
                with c1:
                    st.image(item['image'], use_container_width=True)
                with c2:
                    st.markdown(f"**{item['name']}**")
                    st.caption(item['category'])
                with c3:
                    # Controles de cantidad
                    cc1, cc2, cc3 = st.columns([1,1,1])
                    with cc1:
                        if st.button("➖", key=f"dec_{item['id']}"):
                            update_quantity(item['id'], -1)
                    with cc2:
                        st.markdown(f"<div style='text-align:center; padding-top:10px'><b>{item['quantity']}</b></div>", unsafe_allow_html=True)
                    with cc3:
                        if st.button("➕", key=f"inc_{item['id']}"):
                            update_quantity(item['id'], 1)
                with c4:
                    st.markdown(f"**S/. {(item['price'] * item['quantity']):.2f}**")
                    if st.button("🗑️", key=f"del_{item['id']}"):
                        remove_from_cart(item['id'])

    with col_summary:
        st.markdown("### Resumen del Pedido")
        total = get_cart_total()
        st.write(f"Subtotal: S/. {total:.2f}")
        st.write("Envío: Calculado en checkout")
        st.divider()
        st.markdown(f"### Total: S/. {total:.2f}")
        
        if st.button("Ir a Pagar ➡️", type="primary", use_container_width=True):
            navigate_to('checkout')

def checkout_page():
    st.markdown("## 📦 Finalizar Compra")
    
    if not st.session_state.cart:
        navigate_to('home')
    
    col_form, col_summ = st.columns([2, 1])
    
    with col_form:
        st.subheader("1. Método de Entrega")
        delivery_method = st.radio("Selecciona opción:", ["Recojo en Tienda", "Delivery (Gratis > S/ 50)"])
        
        st.subheader("2. Datos de Envío")
        c1, c2 = st.columns(2)
        with c1:
            st.selectbox("Distrito", ["San Juan de Lurigancho", "La Molina", "Miraflores"])
        with c2:
            st.text_input("Dirección exacta")
        st.text_input("Referencia", placeholder="Ej: Frente al parque...")
        
        st.subheader("3. Datos Personales")
        c3, c4 = st.columns(2)
        with c3:
            st.text_input("Nombres", value="Juan Alberto")
        with c4:
            st.text_input("Celular", value="999 999 999")
            
        st.subheader("4. Pago")
        payment = st.radio("Método de Pago", ["Yape / Plin", "Tarjeta de Crédito/Débito", "Efectivo Contraentrega"])
        
        if payment == "Yape / Plin":
            st.info("ℹ️ Al confirmar, te mostraremos el QR para escanear.")

    with col_summ:
        with st.container(border=True):
            st.markdown("### Tu Pedido")
            for item in st.session_state.cart:
                st.text(f"{item['quantity']}x {item['name'][:20]}...")
            
            st.divider()
            total = get_cart_total()
            igv = total * 0.18
            final_total = total + igv # Simplificación lógica
            
            st.write(f"Subtotal: S/. {total:.2f}")
            st.write(f"IGV (18%): S/. {igv:.2f}")
            st.markdown(f"## Total: S/. {final_total:.2f}")
            
            if st.button("Confirmar Pedido ✅", type="primary", use_container_width=True):
                # Limpiar carrito
                st.session_state.cart = []
                navigate_to('confirmation')

def confirmation_page():
    st.balloons()
    st.success("¡Pedido Registrado con Éxito!")
    
    st.markdown("""
    <div style="text-align: center; padding: 20px;">
        <h1>🎉</h1>
        <h3>Orden #12345</h3>
        <p>Tu pedido ha sido procesado. Para coordinar el envío, por favor envíanos la constancia a WhatsApp.</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.link_button("📱 Enviar Constancia por WhatsApp", "https://wa.me/")
        st.write("")
        if st.button("Volver a la Tienda"):
            navigate_to('home')

def login_page():
    # Simulación simple de la página de Login basada en React
    c1, c2, c3 = st.columns([1,1,1])
    with c2:
        st.markdown("## Iniciar Sesión")
        st.text_input("Correo")
        st.text_input("Contraseña", type="password")
        if st.button("Ingresar", type="primary"):
            st.success("Ingreso simulado exitoso")
            time.sleep(1)
            navigate_to('home')
        if st.button("Volver"):
            navigate_to('home')

# --- ROUTER PRINCIPAL ---
# Simula el React Router

# Renderizar Header (excepto en login/register si se desea, pero aquí lo dejamos fijo)
if st.session_state.page != 'login':
    header_component()

# Renderizar Página Actual
if st.session_state.page == 'home':
    home_page()
elif st.session_state.page == 'cart':
    cart_page()
elif st.session_state.page == 'checkout':
    checkout_page()
elif st.session_state.page == 'confirmation':
    confirmation_page()
elif st.session_state.page == 'login':
    login_page()

# Renderizar Footer
if st.session_state.page != 'login':
    footer_component()
