import streamlit as st
from state import get_cart_total, navigate_to

def render_checkout():
    st.markdown("<h2 class='text-navy'>Finalizar Compra</h2>", unsafe_allow_html=True)
    
    col_left, col_right = st.columns([2, 1])
    
    with col_left:
        # --- PASO 1 ---
        st.markdown('<div class="custom-card" style="padding: 20px; margin-bottom: 20px;">', unsafe_allow_html=True)
        st.markdown("<h4 class='text-navy'>1. Método de Entrega</h4>", unsafe_allow_html=True)
        
        delivery = st.radio("Selecciona:", ["🏠 Recojo en Tienda", "🚚 Delivery (Gratis > S/ 50)"], horizontal=True, label_visibility="collapsed")
        
        if "Delivery" in delivery:
            c1, c2 = st.columns(2)
            with c1: st.selectbox("Departamento / Distrito", ["Lima, San Juan de Lurigancho", "Lima, Miraflores"])
            with c2: st.text_input("Dirección exacta")
            st.text_input("Referencia", placeholder="Ej: Portón negro...")
        st.markdown('</div>', unsafe_allow_html=True)

        # --- PASO 2 ---
        st.markdown('<div class="custom-card" style="padding: 20px; margin-bottom: 20px;">', unsafe_allow_html=True)
        st.markdown("<h4 class='text-navy'>2. Datos de Contacto</h4>", unsafe_allow_html=True)
        c1, c2 = st.columns(2)
        with c1: st.text_input("Nombres", value="Juan Alberto")
        with c2: st.text_input("Apellidos", value="Pérez")
        c3, c4 = st.columns(2)
        with c3: st.text_input("Celular", value="999 999 999")
        with c4: st.text_input("Correo", value="juan@gmail.com")
        st.markdown('</div>', unsafe_allow_html=True)

        # --- PASO 3 ---
        st.markdown('<div class="custom-card" style="padding: 20px; margin-bottom: 20px;">', unsafe_allow_html=True)
        st.markdown("<h4 class='text-navy'>3. Método de Pago</h4>", unsafe_allow_html=True)
        
        payment = st.radio("Pago", ["📱 Yape / Plin", "💳 Tarjeta", "💵 Efectivo"], horizontal=True, label_visibility="collapsed")
        
        if "Yape" in payment:
            st.warning("⚠️ Te mostraremos el código QR en la siguiente pantalla.")
        st.markdown('</div>', unsafe_allow_html=True)


    with col_right:
        # --- RESUMEN FLOTANTE ---
        st.markdown('<div class="custom-card" style="padding: 20px; position: sticky; top: 100px;">', unsafe_allow_html=True)
        st.markdown("<h4 class='text-navy'>Resumen de tu Pedido</h4>", unsafe_allow_html=True)
        
        # Listar items pequeños
        for item in st.session_state.cart:
            st.markdown(f"""
            <div style="display:flex; gap:10px; margin-bottom:10px; font-size:12px;">
                <div style="width:40px; height:40px; background-image:url('{item['image']}'); background-size:cover; border-radius:5px;"></div>
                <div style="flex-grow:1;">
                    <div style="font-weight:bold;">{item['name']}</div>
                    <div style="color:gray;">Cant: {item['quantity']}</div>
                </div>
                <div style="font-weight:bold; color:#FF4500;">S/. {(item['price']*item['quantity']):.2f}</div>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("<hr>", unsafe_allow_html=True)
        total = get_cart_total()
        
        st.markdown(f"""
        <div style="display:flex; justify-content:space-between; font-weight:bold; font-size:20px; color:#001f3f; margin-bottom:20px;">
            <span>Total a Pagar</span>
            <span>S/. {total:.2f}</span>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("CONFIRMAR PEDIDO", key="btn_confirm_order"):
            st.session_state.cart = []
            st.balloons()
            st.success("¡Pedido realizado!")
            # Aquí podrías navegar a una página de 'confirmation'
            
        st.markdown("<div style='text-align:center; font-size:10px; color:gray; margin-top:10px;'>🔒 Datos protegidos por SSL</div>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
