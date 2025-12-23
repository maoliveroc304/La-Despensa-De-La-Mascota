import streamlit as st
from assets import CATEGORIES, PRODUCTS
from state import add_to_cart

def render_home():
    # Hero Section Simplificado
    st.markdown("""
    <div style="background-image: linear-gradient(rgba(0,31,63,0.5), rgba(0,31,63,0.8)), url('https://images.unsplash.com/photo-1583337130417-3346a1be7dee?auto=format&fit=crop&w=1000&q=80'); 
                background-size: cover; background-position: center; border-radius: 20px; padding: 60px 40px; color: white; margin: 20px 40px;">
        <span style="background: #FF4500; padding: 5px 15px; border-radius: 20px; font-weight: bold; font-size: 12px;">NUEVO</span>
        <h1 style="font-size: 48px; font-weight: 800; line-height: 1.1; margin-top: 10px;">Todo para tu mascota<br>a precios de barrio.</h1>
    </div>
    """, unsafe_allow_html=True)

    # Grid de Productos
    st.markdown("<h2 class='text-navy' style='margin: 30px 40px;'>Productos Destacados</h2>", unsafe_allow_html=True)
    
    # Truco: CSS Grid nativo dentro de markdown para el layout, pero botones de Streamlit
    # Streamlit no deja meter botones dentro de HTML puro. 
    # Así que usamos st.columns, pero envolvemos el contenido en divs con estilo .product-grid-item
    
    # Iteramos de 4 en 4
    for i in range(0, len(PRODUCTS), 4):
        cols = st.columns(4, gap="medium")
        batch = PRODUCTS[i:i+4]
        
        for idx, product in enumerate(batch):
            with cols[idx]:
                # 1. Parte Visual (HTML)
                st.markdown(f"""
                <div class="product-grid-item">
                    <div class="product-img" style="background-image: url('{product['image']}');">
                        {f'<span style="position:absolute; top:10px; left:10px; background:red; color:white; padding:2px 8px; border-radius:4px; font-size:10px; font-weight:bold;">{product["badge"]}</span>' if "badge" in product else ""}
                    </div>
                    <div style="padding: 15px; flex-grow: 1;">
                        <div style="font-size: 12px; color: gray;">{product['category']}</div>
                        <div style="font-weight: 700; color: #001f3f; margin-bottom: 5px; height: 40px; overflow: hidden; line-height: 1.2;">{product['name']}</div>
                        <div style="display: flex; justify-content: space-between; align-items: flex-end; margin-top: 10px;">
                            <div>
                                {f'<div style="text-decoration: line-through; color: #ccc; font-size: 12px;">S/. {product["originalPrice"]:.2f}</div>' if product.get("originalPrice") else ""}
                                <div style="color: #FF4500; font-weight: 800; font-size: 18px;">S/. {product['price']:.2f}</div>
                            </div>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
                # 2. Parte Interactiva (Botón Streamlit)
                # Ponemos el botón justo debajo
                if st.button("Agregar 🛒", key=f"add_{product['id']}_{i}"):
                    add_to_cart(product)
                
                # Espacio para separar filas
                st.markdown("<div style='margin-bottom: 20px;'></div>", unsafe_allow_html=True)
