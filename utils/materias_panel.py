import streamlit as st

def panel_materias():
    st.subheader("📚 7° Semestre", divider="rainbow")

    materias = [
        {"nombre": "Análisis de Vulnerabilidades", "icono": "🛡️", "imagen": "https://cdn-icons-png.flaticon.com/512/2455/2455306.png"},
        {"nombre": "Comunidades y Redes Inalámbricas", "icono": "📶", "imagen": "https://cdn-icons-png.flaticon.com/512/2285/2285533.png"},
        {"nombre": "Desarrollo de Apps Web/Móviles", "icono": "📱", "imagen": "https://cdn-icons-png.flaticon.com/512/2704/2704059.png"},
        {"nombre": "Inteligencia Artificial", "icono": "🧠", "imagen": "https://cdn-icons-png.flaticon.com/512/2103/2103633.png"},
        {"nombre": "Seguridad en Cómputo", "icono": "🔐", "imagen": "https://cdn-icons-png.flaticon.com/512/6295/6295416.png"},
        {"nombre": "Sistemas Operativos", "icono": "💻", "imagen": "https://cdn-icons-png.flaticon.com/512/888/888954.png"},
    ]

    st.markdown("""
    <style>
        .materia-card {
            border: 1px solid #e0e0e0;
            border-radius: 12px;
            padding: 20px;
            margin-bottom: 20px;
            background: white;
            box-shadow: 0 3px 6px rgba(0,0,0,0.1);
            transition: all 0.3s;
            cursor: pointer;
            text-align: center;
        }
        .materia-card:hover {
            box-shadow: 0 5px 15px rgba(0,0,0,0.15);
            transform: translateY(-3px);
            border-color: #3498db;
        }
    </style>
    """, unsafe_allow_html=True)

    for materia in materias:
        st.markdown(f"""
        <div class="materia-card">
            <img src="{materia['imagen']}" class="materia-imagen" height="80"><br>
            <h4>{materia['icono']} {materia['nombre']}</h4>
        </div>
        """, unsafe_allow_html=True)
