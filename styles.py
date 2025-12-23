def get_css():
    return """
    <style>
        /* IMPORTAR FUENTES */
        @import url('https://fonts.googleapis.com/css2?family=Spline+Sans:wght@300;400;500;600;700&display=swap');
        
        /* --- RESET Y BASE --- */
        html, body, [class*="css"] {
            font-family: 'Spline Sans', sans-serif;
            background-color: #F8F6F6; /* Color de fondo general */
            color: #181111;
        }

        /* Ocultar elementos nativos molestos */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;} 
        .block-container {
            padding-top: 0rem !important;
            padding-bottom: 5rem !important;
            padding-left: 0rem !important;
            padding-right: 0rem !important;
            max-width: 100% !important;
        }

        /* --- HEADER (NAVBAR) --- */
        .nav-container {
            background-color: #001f3f;
            padding: 15px 40px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            position: sticky;
            top: 0;
            z-index: 9999;
            box-shadow: 0 4px 10px rgba(0,0,0,0.1);
            color: white;
            margin-bottom: 20px;
        }
        
        /* --- TARJETAS (LOGIN, REGISTRO, RESUMEN) --- */
        .custom-card {
            background-color: white;
            padding: 40px;
            border-radius: 20px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.05);
            border: 1px solid #E5E7EB;
        }

        /* --- INPUTS --- */
        /* Forzamos el estilo de los inputs de Streamlit */
        .stTextInput > div > div > input {
            border-radius: 12px;
            padding: 12px 15px;
            border: 1px solid #E5E7EB;
            background-color: #F9FAFB;
            color: #111827;
        }
        .stTextInput > div > div > input:focus {
            border-color: #FF4500;
            box-shadow: 0 0 0 2px rgba(255, 69, 0, 0.2);
        }

        /* --- BOTONES --- */
        /* Botón Primario (Naranja) */
        div.stButton > button {
            background-color: #FF4500;
            color: white;
            border: none;
            border-radius: 12px;
            padding: 12px 24px;
            font-weight: 700;
            transition: all 0.2s;
            width: 100%;
        }
        div.stButton > button:hover {
            background-color: #CC3700;
            color: white;
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(255, 69, 0, 0.3);
        }
        
        /* Botón Secundario (Borde, para "Eliminar" o "Volver") */
        div.stButton > button.secondary-btn {
            background-color: transparent;
            border: 2px solid #E5E7EB;
            color: #374151;
        }
        
        /* Botones Pequeños (+ / -) */
        .small-btn > button {
            padding: 5px 10px !important;
            background-color: #F3F4F6 !important;
            color: #1F2937 !important;
            border-radius: 8px !important;
        }

        /* --- PRODUCTOS --- */
        .product-grid-item {
            background: white;
            border-radius: 16px;
            overflow: hidden;
            border: 1px solid #F3F4F6;
            transition: transform 0.2s;
            height: 100%;
            display: flex;
            flex-direction: column;
        }
        .product-grid-item:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 20px rgba(0,0,0,0.08);
        }
        .product-img {
            width: 100%;
            height: 200px;
            background-size: cover;
            background-position: center;
        }
        
        /* --- CARRITO & CHECKOUT --- */
        .cart-item {
            background: white;
            padding: 20px;
            border-radius: 12px;
            border: 1px solid #F3F4F6;
            display: flex;
            align-items: center;
            gap: 20px;
            margin-bottom: 15px;
        }
        
        /* Utility */
        .text-primary { color: #FF4500; }
        .text-navy { color: #001f3f; }
        .font-bold { font-weight: 700; }
        
    </style>
    """
