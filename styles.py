def get_css():
    return """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Spline+Sans:wght@300;400;500;600;700&family=Noto+Sans:wght@400;500;600;700&display=swap');
        
        html, body, [class*="css"] {
            font-family: 'Spline Sans', sans-serif;
            background-color: #f8f6f6; /* bg-background-light */
            color: #181111;
        }
        
        /* Ocultar elementos nativos de Streamlit que rompen el diseño */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;} 
        .block-container {
            padding-top: 0rem;
            padding-bottom: 0rem;
            padding-left: 0rem;
            padding-right: 0rem;
            max-width: 100%;
        }

        /* --- CLASES PERSONALIZADAS TIPO TAILWIND --- */
        
        .nav-container {
            background-color: #001f3f; /* secondary-nav */
            color: white;
            padding: 1rem 2rem;
            position: sticky;
            top: 0;
            z-index: 999;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        }

        .hero-section {
            background-image: linear-gradient(rgba(0, 31, 63, 0.4), rgba(0, 31, 63, 0.2)), url('https://lh3.googleusercontent.com/aida-public/AB6AXuCGkOYn4A1tEQ3SppVa5eQHIcaxgAZMf9RJkkuKPi_bvVykVlCMuyubXd66sv_42V9Pwi7ABWyieP0D24ZOBxQp07cC5cxYhgsG04atJblcvb3WV532VV4l7QTv6dCmCtaqwwqBoQ6YQ0WhEQdvbewahVd4qxq4jzJoFcjUyrg08NQXd8I_Xr_z2BoMokoc2ULMHrFnrsq2XQFFlOtT8CBdcSSb8-dm8vEaqIjn8KKZZCCTB_t2zbbUVaRp3elNyMj8QNzMHG9XdKc');
            background-size: cover;
            background-position: center;
            height: 500px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            padding: 0 5%;
            color: white;
            margin-bottom: 2rem;
        }

        .category-card {
            background-color: white;
            border-radius: 12px;
            padding: 1rem;
            text-align: center;
            transition: transform 0.2s;
            cursor: pointer;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
            height: 100%;
        }
        .category-card:hover {
            transform: scale(1.05);
            box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
        }

        .product-card {
            background-color: white;
            border-radius: 12px;
            overflow: hidden;
            box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
            transition: all 0.3s;
            margin-bottom: 1rem;
            height: 100%;
            display: flex;
            flex-direction: column;
        }
        .product-card:hover {
            box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1);
            transform: translateY(-4px);
        }

        .badge {
            background-color: #ef4444; /* red-500 */
            color: white;
            font-size: 0.75rem;
            font-weight: bold;
            padding: 0.25rem 0.5rem;
            border-radius: 0.25rem;
            position: absolute;
            top: 0.5rem;
            left: 0.5rem;
            z-index: 10;
        }

        .price-text {
            color: #FF4500; /* primary */
            font-weight: 900;
            font-size: 1.25rem;
        }
        
        .btn-primary {
            background-color: #FF4500 !important;
            color: white !important;
            border: none !important;
            border-radius: 9999px !important; /* rounded-full */
            font-weight: bold !important;
            padding: 0.5rem 1rem !important;
        }
        
        /* Estilizar botones de Streamlit para que parezcan los del diseño */
        div.stButton > button {
            background-color: white;
            color: #001f3f;
            border: 1px solid #e5e7eb;
            border-radius: 0.75rem;
            transition: all 0.2s;
        }
        div.stButton > button:hover {
            border-color: #FF4500;
            color: #FF4500;
        }
        
        /* Botones específicos 'Agregar' o 'Pagar' */
        div.stButton > button:focus {
            box-shadow: 0 0 0 2px rgba(255, 69, 0, 0.5);
        }

        .footer-sec {
            background-color: #001f3f;
            color: white;
            padding: 4rem 2rem;
            margin-top: 4rem;
        }
    </style>
    """
