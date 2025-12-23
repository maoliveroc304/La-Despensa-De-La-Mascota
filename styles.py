def get_css():
    return """
    <style>
        /* --- 1. FUENTES Y COLORES DEL DISEÑO ORIGINAL --- */
        @import url('https://fonts.googleapis.com/css2?family=Spline+Sans:wght@300;400;500;600;700&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&display=swap');

        :root {
            --primary: #FF4500;
            --navy: #001f3f;
            --bg-light: #f8f6f6;
        }

        html, body, [class*="css"] {
            font-family: 'Spline Sans', sans-serif;
            background-color: var(--bg-light);
            color: #181111;
        }

        /* Ocultar elementos nativos molestos */
        #MainMenu, footer, header {visibility: hidden;}
        .block-container {
            padding-top: 0rem !important;
            padding-bottom: 5rem !important;
            max-width: 100% !important;
        }

        /* --- 2. HEADER EXACTO (Barra Azul) --- */
        .header-bg {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 72px; /* Altura exacta del diseño Tailwind */
            background-color: var(--navy);
            z-index: 990;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        }

        /* Contenedor flotante para los widgets de Python */
        .header-widgets-container {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 72px;
            z-index: 999;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        /* --- 3. ESTILIZACIÓN DE WIDGETS DE PYTHON --- */

        /* A) LOGO (Botón transparente) */
        .logo-btn button {
            background-color: transparent !important;
            color: white !important;
            border: none !important;
            font-size: 18px !important;
            font-weight: 700 !important;
            padding: 0 !important;
            margin-top: 5px !important;
        }
        .logo-btn button:hover { color: #ddd !important; }

        /* B) BUSCADOR (Input Redondo + Icono Lupa) */
        /* Hack: Ponemos una imagen de lupa de fondo en el input */
        div[data-testid="stTextInput"] > div > div > input {
            border-radius: 9999px !important; /* rounded-full */
            border: none !important;
            padding: 10px 10px 10px 40px !important; /* Espacio a la izq para el icono */
            background-color: white !important;
            color: #4b5563 !important;
            background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' fill='none' viewBox='0 0 24 24' stroke-width='1.5' stroke='%239CA3AF' class='w-6 h-6'%3E%3Cpath stroke-linecap='round' stroke-linejoin='round' d='M21 21l-5.197-5.197m0 0A7.5 7.5 0 105.196 5.196a7.5 7.5 0 0010.607 10.607z' /%3E%3C/svg%3E");
            background-repeat: no-repeat;
            background-position: 10px center;
            background-size: 20px;
            height: 40px;
            margin-top: -5px; /* Ajuste fino de alineación vertical */
        }
        
        /* C) BOTONES DERECHA (Iconos transparentes) */
        .nav-btn button {
            background-color: transparent !important;
            color: white !important;
            border: 1px solid transparent !important;
            font-weight: 500 !important;
            font-size: 14px !important;
        }
        .nav-btn button:hover {
            background-color: rgba(255,255,255,0.1) !important;
            border: 1px solid rgba(255,255,255,0.2) !important;
            border-radius: 8px !important;
        }
        
        /* Badge rojo del carrito */
        .cart-badge {
            position: absolute;
            top: -5px;
            right: -5px;
            background-color: var(--primary);
            color: white;
            font-size: 10px;
            font-weight: bold;
            padding: 2px 6px;
            border-radius: 999px;
            border: 1px solid var(--navy);
            pointer-events: none;
            z-index: 1000;
        }

        /* --- 4. COMPONENTES GENERALES (Cards, Botones Naranjas) --- */
        .card {
            background: white;
            border-radius: 12px;
            box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.1);
            border: 1px solid #f3f4f6;
            padding: 20px;
        }
        
        /* Botón Primario (Naranja) - Reemplaza los botones por defecto */
        div.stButton > button[kind="primary"] {
            background-color: var(--primary) !important;
            color: white !important;
            border-radius: 12px !important;
            border: none !important;
            font-weight: bold !important;
            padding: 10px 24px !important;
            transition: transform 0.1s;
        }
        div.stButton > button[kind="primary"]:hover {
            transform: scale(1.02);
            box-shadow: 0 4px 12px rgba(255, 69, 0, 0.3);
        }

    </style>
    """
