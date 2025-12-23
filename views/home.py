import streamlit as st
from assets import CATEGORIES, PRODUCTS
from state import add_to_cart, navigate_to

def render_home():
    # --- HERO SECTION ---
    st.markdown("""
        <div class="hero-section">
            <span style="background-color: #FF4500; width: fit-content; padding: 4px 12px; border-radius: 99px; font-weight: bold; text-transform: uppercase; font-size: 0.8rem; margin-bottom: 1rem;">Solo lo mejor</span>
            <h1 style="font-size: 3rem; font-weight: 900; line-height: 1.1; margin-bottom: 1rem;">Todo para tu engreído,<br><span style="color: #FF4500">precios de barrio.</span></h1>
            <p style="font-size: 1.2rem; max-width: 500px; opacity: 0.9;">Encuentra alimentos premium, accesorios y más. Delivery rápido a todo San Juan de Lurigancho.</p>
        </div>
    """, unsafe_allow_html=True)

    # --- CATEGORÍAS ---
    st.markdown("<h3 style='color:#001f3f; font-weight:bold; margin: 2rem 0 1rem 0; padding-left: 1rem;'>Categorías Populares</h3>", unsafe_allow_html=True)
    cols = st.columns(4)
    for idx, cat in enumerate(CATEGORIES):
        with cols[idx]:
            st.markdown(f"""
            <div class="category-card">
                <div style="width: 80px; height: 80px; background-image: url('{cat['image']}'); background-size: cover; border-radius: 50%; margin: 0 auto 10px auto;"></div>
                <div style="font-weight: bold; color: #333;">{cat['name']}</div>
            </div>
            """, unsafe_allow_html=True)

    # --- PRODUCTOS DESTACADOS ---
    st.markdown("<div style='height: 2rem;'></div>", unsafe_allow_html=True)
    col_head1, col_head2 = st.columns([3, 1])
    with col_head1:
        st.markdown("<h3 style='color:#001f3f; font-weight:bold; padding-left: 1rem;'>Productos Destacados</h3>", unsafe_allow_html=True)
    
    # Grid de Productos
    # Usamos st.columns dentro de un loop para simular el grid
    
    # Creamos filas de 4 productos
    rows = [PRODUCTS[i:i + 4] for i in range(0, len(PRODUCTS), 4)]
    
    for row in rows:
        cols = st.columns(4)
        for idx, product in enumerate(row):
            with cols[idx]:
                # Contenedor visual del producto
                # Nota: Streamlit separa UI de lógica. Renderizamos HTML para la imagen y precio,
                # pero usamos un botón nativo de Streamlit para la acción "Agregar".
                
                # HTML Parte Superior
                badge_html = f'<div class="badge">{product["badge"]}</div>' if "badge" in product else ""
                orig_price_html = f'<span style="text-decoration: line-through; color: gray; font-size: 0.8rem;">S/. {product["originalPrice"]:.2f}</span>' if product.get("originalPrice") else ""
                
                st.markdown(f"""
                <div class="product-card">
                    <div style="position: relative; height: 200px; overflow: hidden;">
                        {badge_html}
                        <div style="width: 100%; height: 100%; background-image: url('{product['image']}'); background-size: cover; background-position: center;"></div>
                    </div>
                    <div style="padding: 1rem; flex-grow: 1; display: flex; flex-direction: column;">
                        <div style="font-size: 0.8rem; color: gray;">{product['category']}</div>
                        <div style="font-weight: bold; color: #001f3f; margin-bottom: 0.5rem; line-height: 1.2; height: 2.4em; overflow: hidden;">{product['name']}</div>
                        <div style="margin-top: auto; display: flex; justify-content: space-between; align-items: flex-end;">
                            <div style="display: flex; flex-direction: column;">
                                {orig_price_html}
                                <span class="price-text">S/. {product['price']:.2f}</span>
                            </div>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
                # Botón de acción (Nativo para que funcione el callback)
                if st.button("Agregar 🛒", key=f"add_{product['id']}", use_container_width=True):
                    add_to_cart(product)
