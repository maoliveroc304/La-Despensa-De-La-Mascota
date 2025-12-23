def get_css():
    return """
    <style>
        /* --- IMPORTAR FUENTES (Spline Sans) --- */
        @import url('https://fonts.googleapis.com/css2?family=Spline+Sans:wght@300;400;500;600;700&family=Noto+Sans:wght@400;500;600;700&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&display=swap');

        /* --- CONFIGURACIÓN BASE --- */
        html, body, [class*="css"] {
            font-family: 'Spline Sans', sans-serif;
            background-color: #f8f6f6;
        }

        /* Ocultar elementos nativos de Streamlit */
        #MainMenu, footer, header {visibility: hidden;}
        
        /* Eliminar padding superior para pegar el header al techo */
        .block-container {
            padding-top: 0rem !important;
            padding-bottom: 5rem !important;
            max-width: 100% !important;
        }

        /* --- FONDO DEL HEADER (Barra Azul) --- */
        /* Imitamos la clase .bg-secondary-nav de Tailwind */
        .header-bg {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 80px;
            background-color: #001f3f;
            z-index: 990;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
        }

        /* --- POSICIONAMIENTO DE LOS WIDGETS --- */
        /* Ajustamos el contenedor de Streamlit para que los widgets floten sobre la barra azul */
        div[data-testid="stVerticalBlock"] > div:first-child {
            z-index: 999;
            position: sticky;
            top: 0;
        }

        /* --- LOGO (Botón Transparente) --- */
        /* Convertimos el botón de Streamlit en el logo de texto */
        .logo-btn button {
            background-color: transparent !important;
            color: white !important;
            border: none !important;
            font-size: 20px !important;
            font-weight: 700 !important;
            text-align: left !important;
            padding: 0 !important;
            margin-top: 10px !important;
        }
        .logo-btn button:hover {
            color: #FF4500 !important; /* Primary hover */
        }
        .logo-subtext {
            color: rgba(255,255,255,0.9);
            font-size: 12px;
            font-weight: 300;
            margin-top: -15px;
            margin-left: 2px;
            pointer-events: none; /* Para que el click pase al botón si se superpone */
        }

        /* --- BUSCADOR (Input Redondeado) --- */
        /* Imitamos: rounded-full border-none focus:ring-2 focus:ring-primary text-sm bg-white */
        .search-container div[data-testid="stTextInput"] > div > div > input {
            border-radius: 9999px !important; /* rounded-full */
            border: none !important;
            background-color: white !important;
            color: #4b5563 !important; /* text-gray-600 */
            padding: 10px 20px !important;
            margin-top: 5px;
            box-shadow: 0 0 0 0 transparent !important; /* Quitar borde rojo default de streamlit */
        }
        .search-container div[data-testid="stTextInput"] > div > div > input:focus {
            box-shadow: 0 0 0 2px #FF4500 !important; /* focus:ring-primary */
        }

        /* --- BOTONES DE ACCIÓN (Derecha) --- */
        .action-btn button {
            background-color: transparent !important;
            color: white !important;
            border: none !important;
            font-size: 14px !important;
            font-weight: 500 !important;
            display: flex;
            align-items: center;
            padding: 0px 10px !important;
            margin-top: 12px !important;
        }
        .action-btn button:hover {
            color: #e5e7eb !important; /* hover:text-gray-200 */
        }

        /* Estilo para el Badge del Carrito */
        .cart-badge {
            background-color: #FF4500;
            color: white;
            border-radius: 9999px;
            padding: 2px 6px;
            font-size: 10px;
            font-weight: bold;
            position: absolute;
            top: 10px;
            right: 40px; /* Ajustar posición según layout */
            z-index: 1000;
            border: 1px solid #001f3f;
            pointer-events: none;
        }

        /* --- ESTILOS GENERALES DE LA APP --- */
        .product-card {
            background: white;
            border-radius: 12px;
            box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.1);
            overflow: hidden;
            transition: all 0.3s;
        }
        .product-card:hover {
            transform: translateY(-4px);
            box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
        }
    </style>
    """
