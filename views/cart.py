import streamlit as st
from state import update_quantity, remove_from_cart, get_cart_total, navigate_to

def render_cart():
    st.markdown("<h2 class='text-navy' style='margin: 0 0 30px 0;'>Carrito de Compras</h2>", unsafe_allow_html=True)
    
    if not st.session_state.cart:
        st.info("Tu carrito está vacío.")
        if st.button("Volver a la tienda"):
            navigate_to('home')
        return

    c_items, c_summary = st.columns([2.5, 1.2])

    with c_items:
        for item in st.session_state.cart:
            # Contenedor Visual de Fila
            with st.container():
                c_img, c_info, c_qty, c_price = st.columns([1, 2.5, 1.5, 1])
                
                with c_img:
                    st.image(item['image'], use_container_width=True)
                
                with c_info:
                    st.markdown(f"**{item['name']}**")
                    st.caption(item['category'])
                    if st.button("Eliminar", key=f"del_{item['id']}"):
                        remove_from_cart(item['id'])

                with c_qty:
                    # Controles de cantidad
                    cq1, cq2, cq3 = st.columns([1, 1, 1])
                    with cq1:
                        # Usamos help para identificar, pero el estilo lo hace el CSS global de botones pequeños si es necesario
                        if st.button("-", key=f"dec_{item['id']}"):
                            update_quantity(item['id'], -1)
                    with cq2:
                        st.markdown(f"<div style='text-align:center; padding-top:10px; font-weight:bold;'>{item['quantity']}</div>", unsafe_allow_html=True)
                    with cq3:
                        if st.button("+", key=f"inc_{item['id']}"):
                            update_quantity(item['id'], 1)

                with c_price:
                    total_item = item['price'] * item['quantity']
                    st.markdown(f"<div style='color:#FF4500; font-weight:bold; text-align:right;'>S/. {total_item:.2f}</div>", unsafe_allow_html=True)
                
                st.markdown("<hr style='margin: 10px 0; border-color: #eee;'>", unsafe_allow_html=True)

    with c_summary:
        st.markdown('<div class="custom-card" style="padding: 20px;">', unsafe_allow_html=True)
        st.markdown("<h3 class='text-navy'>Resumen</h3>", unsafe_allow_html=True)
        
        total = get_cart_total()
        
        st.markdown(f"""
        <div style="display:flex; justify-content:space-between; margin-bottom:10px;">
            <span>Subtotal</span>
            <span>S/. {total:.2f}</span>
        </div>
        <div style="display:flex; justify-content:space-between; color:gray; font-size:12px;">
            <span>Envío</span>
            <span>Calculado en checkout</span>
        </div>
        <hr>
        <div style="display:flex; justify-content:space-between; font-weight:bold; font-size:18px; color:#001f3f; margin-bottom:20px;">
            <span>Total</span>
            <span>S/. {total:.2f}</span>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("Ir a Pagar ➔", key="checkout_btn"):
            navigate_to('checkout')
            
        st.markdown('</div>', unsafe_allow_html=True)
