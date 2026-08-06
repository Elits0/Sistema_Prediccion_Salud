import streamlit as st

from src.paciente import Paciente
from src.predict import predecir_diabetes, predecir_cardio
from src.risk import calcular_riesgo

# ----------------------------------------------------
# Configuración
# ----------------------------------------------------

st.set_page_config(
    page_title="Sistema Inteligente de Salud",
    page_icon="🩺",
    layout="wide"
)

st.title("🩺 Sistema Inteligente de Evaluación de Riesgo")

st.markdown("""
Este sistema utiliza Inteligencia Artificial para estimar el riesgo de:

- 🩸 Diabetes
- ❤️ Enfermedad Cardiovascular

Complete la información del paciente y presione **Analizar Paciente**.
""")

st.divider()

# ====================================================
# INFORMACIÓN PERSONAL
# ====================================================

st.header("👤 Información Personal")

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

st.divider()

# ====================================================
# SIGNOS VITALES
# ====================================================

st.header("❤️ Signos Vitales")

col1, col2 = st.columns(2)

with col1:

    presion_sistolica = st.number_input(
        "Presión Sistólica",
        80,
        250,
        120
    )

    colesterol = st.selectbox(
        "Colesterol",
        [1,2,3],
        format_func=lambda x:
        {
            1:"Normal",
            2:"Por encima de lo normal",
            3:"Muy alto"
        }[x]
    )

with col2:

    presion_diastolica = st.number_input(
        "Presión Diastólica",
        40,
        180,
        80
    )

    glucosa = st.selectbox(
        "Glucosa",
        [1,2,3],
        format_func=lambda x:
        {
            1:"Normal",
            2:"Por encima de lo normal",
            3:"Muy alta"
        }[x]
    )

st.divider()

# ====================================================
# HÁBITOS
# ====================================================

st.header("🥗 Hábitos")

col1, col2, col3 = st.columns(3)

with col1:

    fuma = st.checkbox("Fuma")

    alcohol = st.checkbox("Consume Alcohol")

with col2:

    actividad = st.checkbox(
        "Actividad Física"
    )

with col3:

    frutas = st.checkbox(
        "Consume Frutas"
    )

    verduras = st.checkbox(
        "Consume Verduras"
    )

st.divider()

# ====================================================
# ESTADO GENERAL
# ====================================================

st.header("🩺 Estado General")

col1, col2 = st.columns(2)

with col1:

    salud_general = st.slider(
        "Estado General de Salud",
        1,
        5,
        3
    )

    salud_fisica = st.slider(
        "Días con mala salud física",
        0,
        30,
        0
    )

    salud_mental = st.slider(
        "Días con mala salud mental",
        0,
        30,
        0
    )

with col2:

    dificultad_caminar = st.checkbox(
        "Dificultad para caminar"
    )

    educacion = st.slider(
        "Nivel educativo",
        1,
        6,
        4
    )

    ingresos = st.slider(
        "Nivel de ingresos",
        1,
        8,
        5
    )

st.divider()

analizar = st.button(
    "🔍 Analizar Paciente",
    use_container_width=True
)

if analizar:

    datos = {

        "edad": edad,

        "sexo": 1 if sexo == "Hombre" else 0,

        "altura": altura,

        "peso": peso,

        "presion_sistolica": presion_sistolica,

        "presion_diastolica": presion_diastolica,

        "colesterol": colesterol,

        "glucosa": glucosa,

        "fuma": int(fuma),

        "alcohol": int(alcohol),

        "actividad_fisica": int(actividad),

        "frutas": int(frutas),

        "verduras": int(verduras),

        "salud_general": salud_general,

        "salud_fisica": salud_fisica,

        "salud_mental": salud_mental,

        "dificultad_caminar": int(dificultad_caminar),

        "educacion": educacion,

        "ingresos": ingresos

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

    st.header("📊 Resultados")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "🩸 Riesgo Diabetes",
            f"{prob_d*100:.2f}%"
        )

        st.progress(float(prob_d))

    with col2:

        st.metric(
            "❤️ Riesgo Cardiovascular",
            f"{prob_c*100:.2f}%"
        )

        st.progress(float(prob_c))

    with col3:

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