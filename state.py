import streamlit as st

def init_state():
    if 'cart' not in st.session_state:
        st.session_state.cart = []
    if 'page' not in st.session_state:
        st.session_state.page = 'home'

def navigate_to(page):
    st.session_state.page = page
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
    st.toast(f"✅ Agregado: {product['name']}")

def remove_from_cart(product_id):
    st.session_state.cart = [item for item in st.session_state.cart if item['id'] != product_id]
    st.rerun()

def update_quantity(product_id, delta):
    for item in st.session_state.cart:
        if item['id'] == product_id:
            item['quantity'] = max(1, item['quantity'] + delta)
    st.rerun()

def get_cart_total():
    return sum(item['price'] * item['quantity'] for item in st.session_state.cart)

def get_cart_count():
    return sum(item['quantity'] for item in st.session_state.cart)
