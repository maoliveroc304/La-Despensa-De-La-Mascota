import streamlit as st
from state import navigate_to

def render_login():
    st.markdown("""
    <div style="display: flex; justify-content: center; padding: 2rem 1rem;">
        <div style="width: 100%; max-width: 450px; background-color: white; border-radius: 1rem; overflow: hidden; box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1); border: 1px solid #f3f4f6;">
            <div style="background-color: #001f3f; padding: 2rem; text-align: center; color: white;">
                <div style="background-color: rgba(255,255,255,0.1); padding: 0.75rem; border-radius: 9999px; display: inline-flex; margin-bottom: 1rem;">
                    <span style="font-size: 2.5rem;">🐾</span>
                </div>
                <h1 style="font-size: 1.25rem; font-weight: bold; margin: 0; line-height: 1.2;">La Despensa de la Mascota</h1>
                <p style="font-size: 0.875rem; opacity: 0.8; font-weight: 300; margin-top: 0.25rem;">por Tienda Buendía</p>
            </div>
            <div style="padding: 2rem;">
                <h2 style="font-size: 1.5rem; font-weight: bold; text-align: center; color: #001f3f; margin-bottom: 2rem;">Bienvenido de nuevo</h2>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Renderizamos los inputs usando columnas para centrarlos visualmente dentro del ancho del contenedor
    # Nota: En Streamlit puro, los inputs ocupan el ancho del contenedor padre (la columna).
    
    col_izq, col_centro, col_der = st.columns([1, 2, 1])
    
    with col_centro:
        with st.form("login_form"):
            st.text_input("Correo electrónico o celular", placeholder="tu@correo.com")
            st.text_input("Contraseña", type="password", placeholder="••••••••")
            
            st.markdown("""
                <div style="text-align: right; margin-bottom: 1rem;">
                    <a href="#" style="font-size: 0.875rem; font-weight: 500; color: #FF4500; text-decoration: none;">¿Olvidaste contraseña?</a>
                </div>
            """, unsafe_allow_html=True)
            
            submitted = st.form_submit_button("Ingresar", type="primary", use_container_width=True)
            
            if submitted:
                # Aquí iría tu lógica de autenticación real
                st.toast("Inicio de sesión exitoso", icon="✅")
                navigate_to('home')

        st.markdown("""
            <div style="text-align: center; margin-top: 2rem; padding-top: 1.5rem; border-top: 1px solid #f3f4f6;">
                <p style="font-size: 0.875rem; color: #4b5563;">
                    ¿No tienes cuenta?
                </p>
            </div>
        """, unsafe_allow_html=True)
        
        if st.button("Regístrate aquí", type="secondary", use_container_width=True):
            navigate_to('register')


def render_register():
    st.markdown("""
    <div style="display: flex; justify-content: center; padding: 2rem 1rem;">
        <div style="width: 100%; max-width: 450px; text-align: center;">
            <div style="display: inline-flex; align-items: center; justify-content: center; width: 4rem; height: 4rem; border-radius: 9999px; background-color: rgba(0, 31, 63, 0.1); margin-bottom: 1rem;">
                <span style="font-size: 2rem; color: #001f3f;">👤</span>
            </div>
            <h2 style="font-size: 1.875rem; font-weight: bold; color: #001f3f;">Registro de Nuevo Usuario</h2>
            <p style="margin-top: 0.5rem; font-size: 0.875rem; color: #4b5563;">
                Crea tu cuenta en minutos y empieza a engreír a tu mascota.
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    col_izq, col_centro, col_der = st.columns([1, 2, 1])

    with col_centro:
        with st.form("register_form"):
            st.text_input("Nombres", placeholder="Ej. María García")
            st.text_input("Celular (Para contacto WhatsApp)", placeholder="999 999 999")
            st.text_input("Correo Electrónico", placeholder="correo@ejemplo.com")
            st.text_input("Crear Contraseña", type="password", placeholder="Mínimo 8 caracteres")
            
            st.checkbox("He leído y acepto los Términos y Condiciones y la Política de Privacidad.")
            
            submitted = st.form_submit_button("Crear Cuenta", type="primary", use_container_width=True)
            
            if submitted:
                st.toast("Cuenta creada correctamente", icon="🎉")
                navigate_to('home')

        st.markdown("""
            <div style="text-align: center; margin-top: 1.5rem; border-top: 1px solid #e5e7eb; padding-top: 1.5rem;">
                <p style="font-size: 0.875rem; color: #4b5563;">
                    ¿Ya tienes una cuenta?
                </p>
            </div>
        """, unsafe_allow_html=True)
        
        if st.button("Inicia Sesión aquí", type="secondary", use_container_width=True):
            navigate_to('login')
