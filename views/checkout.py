import streamlit as st
from state import st, navigate_to, get_cart_total

def render_checkout():
    st.markdown("<h2 style='color:#001f3f; font-weight:bold;'>Finalizar Compra</h2>", unsafe_allow_html=True)
    
    col_form, col_summ = st.columns([2, 1])
    
    with col_form:
        # Paso 1
        with st.container():
            st.markdown("### 1. Método de Entrega")
            option = st.radio("Selecciona:", ["Recojo en Tienda", "Delivery"], horizontal=True)
            
            if option == "Delivery":
                c1, c2 = st.columns(2)
                with c1: st.selectbox("Distrito", ["San Juan de Lurigancho", "Lima", "Miraflores"])
                with c2: st.text_input("Dirección")
                st.text_input("Referencia")

        st.divider()

        # Paso 2
        with st.container():
            st.markdown("### 2. Datos de Contacto")
            c1, c2 = st.columns(2)
            with c1: st.text_input("Nombres", value="Juan Alberto")
            with c2: st.text_input("Celular", value="999 999 999")

        st.divider()
        
        # Paso 3
        with st.container():
            st.markdown("### 3. Pago")
            pay_method = st.radio("Medio de Pago:", ["Yape / Plin", "Tarjeta", "Efectivo"], horizontal=True)
            if pay_method == "Yape / Plin":
                st.warning("⚠️ Te mostraremos el QR al confirmar.")

    with col_summ:
        st.info(f"Total a Pagar: **S/. {get_cart_total():.2f}**")
        st.markdown("Tus datos están protegidos por SSL.")
        if st.button("CONFIRMAR PEDIDO", type="primary", use_container_width=True):
            st.session_state.cart = [] # Limpiar carrito
            navigate_to('home')
            st.toast("Pedido realizado con éxito", icon="🎉")
