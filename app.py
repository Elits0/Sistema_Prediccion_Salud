#----------------------
#Librerias
#----------------------
import streamlit as st
from src.paciente import Paciente
from src.predict import predecir_diabetes, predecir_cardio
from src.risk import calcular_riesgo
from pathlib import Path

#---------------
#CONFIG PAG
#---------------
st.set_page_config(
    page_title="HealthAI",
    page_icon="🩺",
    layout="wide"
)
#CARGAR CSS
css = Path("assets/style.css").read_text()
st.markdown(
    f"<style>{css}</style>",
    unsafe_allow_html=True
)

#HEADER ------------
st.markdown("""
<div class="card">

<div class="titulo">
🩺 HealthAI
</div>

<div class="subtitulo">

Sistema Inteligente para la Predicción de Diabetes
y Enfermedades Cardiovasculares mediante Machine Learning.

</div>

</div>
""",unsafe_allow_html=True)

# ============================================
# LAYOUT PRINCIPAL
# ============================================
col_form, col_dash = st.columns([1, 2], gap="large")

# ====================================================
# DATOS PERSONALES
# ====================================================

with col_form:

    st.markdown("""
    <div class="form-card">

    <div class="form-title">
    👤 Datos Personales
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:

        edad = st.number_input(
            "Edad",
            min_value=18,
            max_value=100,
            value=40
        )

        sexo = st.selectbox(
            "Sexo",
            ["Hombre", "Mujer"]
        )

    with col2:

        altura = st.number_input(
            "Altura (cm)",
            min_value=120,
            max_value=220,
            value=170
        )

        peso = st.number_input(
            "Peso (kg)",
            min_value=30,
            max_value=200,
            value=70
        )

    st.markdown("</div>", unsafe_allow_html=True)

    st.divider()

# ====================================================
# SIGNOS VITALES
# ====================================================

st.markdown("""
<div class="form-card">

<div class="form-title">
❤️ Signos Vitales
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:

    presion_sistolica = st.number_input(
        "Presión Sistólica",
        min_value=80,
        max_value=250,
        value=120
    )

    colesterol = st.selectbox(
        "Colesterol",
        [1, 2, 3],
        format_func=lambda x: {
            1: "Normal",
            2: "Por encima de lo normal",
            3: "Muy alto"
        }[x]
    )

with col2:

    presion_diastolica = st.number_input(
        "Presión Diastólica",
        min_value=40,
        max_value=180,
        value=80
    )

    glucosa = st.selectbox(
        "Glucosa",
        [1, 2, 3],
        format_func=lambda x: {
            1: "Normal",
            2: "Por encima de lo normal",
            3: "Muy alta"
        }[x]
    )

st.markdown("</div>", unsafe_allow_html=True)

st.divider()

# ====================================================
# HÁBITOS
# ====================================================

st.markdown("""
<div class="form-card">

<div class="form-title">
🥗 Hábitos
</div>
""", unsafe_allow_html=True)

fuma = st.selectbox(
    "¿Fuma actualmente?",
    ["No", "Sí"]
)

alcohol = st.selectbox(
    "¿Consume alcohol?",
    ["No", "Sí"]
)

actividad = st.selectbox(
    "¿Realiza actividad física?",
    ["Sí", "No"]
)

frutas = st.selectbox(
    "¿Consume frutas regularmente?",
    ["Sí", "No"]
)

verduras = st.selectbox(
    "¿Consume verduras regularmente?",
    ["Sí", "No"]
)

st.markdown("</div>", unsafe_allow_html=True)

st.divider()

# ====================================================
# ESTADO GENERAL
# ====================================================

st.markdown("""
<div class="form-card">

<div class="form-title">
🩺 Estado General
</div>
""", unsafe_allow_html=True)

salud_general = st.selectbox(
    "¿Cómo considera su estado general de salud?",
    [
        "Excelente",
        "Muy buena",
        "Buena",
        "Regular",
        "Mala"
    ]
)

dificultad_caminar = st.selectbox(
    "¿Tiene dificultad para caminar?",
    ["No", "Sí"]
)

st.markdown("</div>", unsafe_allow_html=True)

st.divider()

#desorden


analizar = st.button(
    "🔍 Analizar Paciente",
    use_container_width=True
)

if analizar:
    estado_map = {
    "Excelente": 1,
    "Muy buena": 2,
    "Buena": 3,
    "Regular": 4,
    "Mala": 5
}

    datos = {

    "edad": edad,

    "sexo": 1 if sexo == "Hombre" else 0,

    "altura": altura,

    "peso": peso,

    "presion_sistolica": presion_sistolica,

    "presion_diastolica": presion_diastolica,

    "colesterol": colesterol,

    "glucosa": glucosa,

    "fuma": 1 if fuma == "Sí" else 0,

    "alcohol": 1 if alcohol == "Sí" else 0,

    "actividad_fisica": 1 if actividad == "Sí" else 0,

    "frutas": 1 if frutas == "Sí" else 0,

    "verduras": 1 if verduras == "Sí" else 0,

    "salud_general": estado_map[salud_general],

    "salud_fisica": 0,

    "salud_mental": 0,

    "dificultad_caminar": 1 if dificultad_caminar == "Sí" else 0,

    "educacion": 4,

    "ingresos": 5
}

    paciente = Paciente(datos)

    pred_d, prob_d = predecir_diabetes(
        paciente.to_diabetes()
    )

    pred_c, prob_c = predecir_cardio(
        paciente.to_cardio()
    )

    riesgo, nivel = calcular_riesgo(
        prob_d,
        prob_c
    )

    st.divider()

    st.markdown("## 📊 Dashboard de Resultados")

    c1, c2, c3 = st.columns(3)

    with c1:

        st.metric(
            "🩸 Riesgo Diabetes",
            f"{prob_d*100:.2f}%"
        )

        st.progress(float(prob_d))

    with c2:

        st.metric(
            "❤️ Riesgo Cardiovascular",
            f"{prob_c*100:.2f}%"
        )

        st.progress(float(prob_c))

    with c3:

        st.metric(
            "🚦 Riesgo General",
            f"{riesgo*100:.2f}%"
        )

        st.success(nivel)

    st.divider()

    st.subheader("💡 Recomendaciones")

    recomendaciones = []

    if paciente.bmi >= 30:
        recomendaciones.append("• Reducir el IMC mediante alimentación saludable y ejercicio.")

    if paciente.presion_sistolica >= 140:
        recomendaciones.append("• Controlar la presión arterial.")

    if paciente.colesterol > 1:
        recomendaciones.append("• Reducir el colesterol mediante dieta y seguimiento médico.")

    if not paciente.actividad_fisica:
        recomendaciones.append("• Realizar actividad física regularmente.")

    if paciente.fuma:
        recomendaciones.append("• Evitar el consumo de tabaco.")

    if not recomendaciones:
        recomendaciones.append("• Mantener los hábitos saludables actuales.")

    for recomendacion in recomendaciones:
        st.write(recomendacion)