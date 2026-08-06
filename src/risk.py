def calcular_riesgo(prob_diabetes, prob_cardio):
    """
    Calcula un riesgo general a partir de las probabilidades
    de diabetes y enfermedad cardiovascular.
    """

    riesgo = (prob_diabetes + prob_cardio) / 2

    if riesgo < 0.30:
        nivel = "🟢 Bajo"

    elif riesgo < 0.60:
        nivel = "🟡 Moderado"

    else:
        nivel = "🔴 Alto"

    return riesgo, nivel