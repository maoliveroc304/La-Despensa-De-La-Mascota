import streamlit as st
from state import navigate_to

def render_login():
    # Contenedor centralizado
    c1, c2, c3 = st.columns([1, 2, 1])
    
    with c2:
        # Inicio de la tarjeta visual
        st.markdown('<div class="custom-card">', unsafe_allow_html=True)
        
        st.markdown("""
            <div style="text-align: center; margin-bottom: 30px;">
                <div style="font-size: 40px; margin-bottom: 10px;">🐾</div>
                <h2 class="text-navy" style="margin:0;">Iniciar Sesión</h2>
                <p style="color: gray; font-size: 14px;">Ingresa a tu cuenta para continuar</p>
            </div>
        """, unsafe_allow_html=True)

        with st.form("login_form", clear_on_submit=False):
            st.text_input("Usuario o Correo", placeholder="ej. juan@gmail.com")
            st.text_input("Contraseña", type="password", placeholder="••••••••")
            
            # Espaciador
            st.markdown("<br>", unsafe_allow_html=True)
            
            # Botón Submit (ahora naranja por CSS global)
            submitted = st.form_submit_button("INGRESAR")
            
            if submitted:
                # Simular login
                st.session_state['user_logged_in'] = True
                st.toast("¡Bienvenido de nuevo!", icon="👋")
                navigate_to('home')

        # Pie de la tarjeta con Link a Registro
        st.markdown("""
            <div style="text-align: center; margin-top: 20px; padding-top: 20px; border-top: 1px solid #eee;">
                <span style="color: gray;">¿No tienes cuenta?</span>
            </div>
        """, unsafe_allow_html=True)
        
        # Botón secundario para ir a registro
        if st.button("Crear Cuenta Nueva", key="goto_register"):
            navigate_to('register')
            
        st.markdown('</div>', unsafe_allow_html=True) # Fin custom-card


def render_register():
    c1, c2, c3 = st.columns([1, 2, 1])
    
    with c2:
        st.markdown('<div class="custom-card">', unsafe_allow_html=True)
        
        st.markdown("""
            <div style="text-align: center; margin-bottom: 20px;">
                <h2 class="text-navy">Registro de Usuario</h2>
                <p style="color: gray;">Crea tu cuenta en minutos.</p>
            </div>
        """, unsafe_allow_html=True)

        with st.form("register_form"):
            col_a, col_b = st.columns(2)
            with col_a:
                st.text_input("Nombres", placeholder="Ej. María")
            with col_b:
                st.text_input("Apellidos", placeholder="García")
                
            st.text_input("Celular", placeholder="999 999 999")
            st.text_input("Correo Electrónico", placeholder="correo@ejemplo.com")
            st.text_input("Crear Contraseña", type="password")
            
            st.checkbox("Acepto los Términos y Condiciones")
            
            st.markdown("<br>", unsafe_allow_html=True)
            if st.form_submit_button("CREAR CUENTA"):
                st.toast("Cuenta creada con éxito", icon="🎉")
                navigate_to('home')
        
        st.markdown("""
            <div style="text-align: center; margin-top: 20px;">
                <span style="color: gray;">¿Ya tienes cuenta?</span>
            </div>
        """, unsafe_allow_html=True)
        
        if st.button("Iniciar Sesión", key="goto_login"):
            navigate_to('login')

        st.markdown('</div>', unsafe_allow_html=True)
