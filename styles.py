def get_css():
    return """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Spline+Sans:wght@300;400;500;600;700&display=swap');
        
        /* --- RESET Y BASE --- */
        html, body, [class*="css"] {
            font-family: 'Spline Sans', sans-serif;
            background-color: #F8F6F6;
            color: #181111;
        }

        /* Ocultar elementos nativos */
        #MainMenu, footer, header {visibility: hidden;}
        
        /* Eliminar padding superior para que el header pegue al borde */
        .block-container {
            padding-top: 0rem !important;
            padding-bottom: 5rem !important;
            margin-top: 0 !important;
        }

        /* --- FONDO DEL HEADER (VISUAL) --- */
        /* Creamos una barra azul fija detrás de los controles de Streamlit */
        .header-background {
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 80px; /* Ajusta la altura del header */
            background-color: #001f3f;
            z-index: 50; /* Detrás de los widgets, pero encima del contenido */
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        
        /* --- POSICIONAMIENTO DE LOS WIDGETS DEL HEADER --- */
        /* Esto empuja los widgets de Streamlit hacia abajo para que no queden tapados,
           excepto los que queremos EN el header */
        
        /* Estilo específico para el LOGO (Botón transparente) */
        div[data-testid="stHorizontalBlock"] button[kind="secondary"] {
            background-color: transparent !important;
            border: none !important;
            color: white !important;
            text-align: left !important;
            font-size: 20px !important;
            padding: 0 !important;
        }
        div[data-testid="stHorizontalBlock"] button[kind="secondary"]:hover {
            color: #FF4500 !important; /* Naranja al pasar el mouse */
        }

        /* Estilo específico para la BARRA DE BÚSQUEDA en el header */
        /* Buscamos el input dentro de las columnas superiores */
        div[data-testid="stHorizontalBlock"] .stTextInput input {
            border-radius: 20px !important;
            border: none !important;
            padding: 10px 20px !important;
            background-color: white !important;
            color: #333 !important;
            box-shadow: inset 0 1px 3px rgba(0,0,0,0.1) !important;
        }
        
        /* Estilos para los botones de la derecha (Mi Cuenta / Carrito) */
        /* Usaremos una clase custom o identificaremos por el texto si es posible, 
           pero por ahora forzamos los botones en el bloque horizontal superior */
           
        /* Ajuste de alineación vertical para que todo quede centrado en la barra azul */
        div[data-testid="stVerticalBlock"] > div:first-child {
            z-index: 100; /* Asegura que los botones estén clickeables sobre la barra azul */
            padding-top: 15px; /* Baja un poco los controles para centrarlos en la barra de 80px */
        }

        /* --- ESTILOS GENERALES (Resto de la app) --- */
        .custom-card {
            background-color: white;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.05);
            border: 1px solid #E5E7EB;
        }
        
        /* Botones Naranjas (Acción Principal) */
        button[kind="primary"] {
            background-color: #FF4500 !important;
            color: white !important;
            border: none !important;
            border-radius: 12px !important;
            transition: transform 0.1s !important;
        }
        button[kind="primary"]:hover {
            background-color: #CC3700 !important;
            transform: scale(1.02) !important;
        }

    </style>
    """
