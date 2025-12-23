import streamlit as st
from state import st, remove_from_cart, update_quantity, get_cart_total, navigate_to

def render_cart():
    st.markdown("<h2 style='color:#001f3f; font-weight:bold; margin-bottom: 1.5rem;'>Carrito de Compras</h2>", unsafe_allow_html=True)
    
    if not st.session_state.cart:
        st.info("Tu carrito está vacío.")
        if st.button("Seguir comprando"):
            navigate_to('home')
        return

    col_items, col_summary = st.columns([2, 1])

    with col_items:
        for item in st.session_state.cart:
            with st.container():
                c1, c2, c3 = st.columns([1, 2, 1])
                with c1:
                    st.markdown(f"""
                    <div style="border-radius: 8px; overflow: hidden; height: 100px; width: 100px; background-image: url('{item['image']}'); background-size: cover;"></div>
                    """, unsafe_allow_html=True)
                with c2:
                    st.markdown(f"<div style='font-weight: bold; color: #001f3f;'>{item['name']}</div>", unsafe_allow_html=True)
                    st.caption(item['category'])
                    
                    # Controles de cantidad
                    cc1, cc2, cc3 = st.columns([1,1,2])
                    with cc1:
                        if st.button("−", key=f"dec_{item['id']}"):
                            update_quantity(item['id'], -1)
                    with cc2:
                        st.markdown(f"<div style='text-align: center; font-weight: bold; padding-top: 5px;'>{item['quantity']}</div>", unsafe_allow_html=True)
                    with cc3:
                        if st.button("+", key=f"inc_{item['id']}"):
                            update_quantity(item['id'], 1)
                            
                with c3:
                    subtotal = item['price'] * item['quantity']
                    st.markdown(f"<div style='text-align: right; color: #FF4500; font-weight: bold; font-size: 1.1rem;'>S/. {subtotal:.2f}</div>", unsafe_allow_html=True)
                    if st.button("Eliminar", key=f"del_{item['id']}"):
                        remove_from_cart(item['id'])
                st.divider()

    with col_summary:
        st.markdown("""
        <div style="background-color: white; padding: 1.5rem; border-radius: 12px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1);">
            <h3 style="color: #001f3f; font-weight: bold; margin-bottom: 1rem;">Resumen</h3>
        """, unsafe_allow_html=True)
        
        total = get_cart_total()
        st.markdown(f"""
            <div style="display: flex; justify-content: space-between; margin-bottom: 0.5rem;">
                <span>Subtotal</span>
                <span>S/. {total:.2f}</span>
            </div>
            <div style="display: flex; justify-content: space-between; margin-bottom: 1rem;">
                <span>Envío</span>
                <span style="font-size: 0.8rem; color: gray;">Calculado en el siguiente paso</span>
            </div>
            <div style="border-top: 1px dashed #ddd; margin: 1rem 0;"></div>
            <div style="display: flex; justify-content: space-between; font-weight: bold; font-size: 1.2rem; color: #001f3f;">
                <span>Total</span>
                <span>S/. {total:.2f}</span>
            </div>
            <br>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("Ir a Pagar ➔", type="primary", use_container_width=True):
            navigate_to('checkout')
