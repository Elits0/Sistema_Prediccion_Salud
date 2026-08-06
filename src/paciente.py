class Paciente:

    def __init__(self, datos: dict):
        """
        Inicializa un paciente a partir de un diccionario.
        """

        self.edad = datos["edad"]
        self.sexo = datos["sexo"]

        self.altura = datos["altura"]
        self.peso = datos["peso"]

        self.presion_sistolica = datos["presion_sistolica"]
        self.presion_diastolica = datos["presion_diastolica"]

        self.colesterol = datos["colesterol"]
        self.glucosa = datos["glucosa"]

        self.fuma = datos["fuma"]
        self.alcohol = datos["alcohol"]
        self.actividad_fisica = datos["actividad_fisica"]

        self.frutas = datos["frutas"]
        self.verduras = datos["verduras"]

        self.salud_general = datos["salud_general"]
        self.salud_fisica = datos["salud_fisica"]
        self.salud_mental = datos["salud_mental"]

        self.dificultad_caminar = datos["dificultad_caminar"]

        self.educacion = datos["educacion"]
        self.ingresos = datos["ingresos"]

    @property
    def bmi(self):
        """
        Calcula automáticamente el IMC.
        """
        return self.peso / ((self.altura / 100) ** 2)

    def to_cardio(self):
        """
        Convierte los datos al formato esperado
        por el modelo cardiovascular.
        """

        return {

            "age": self.edad,
            "gender": self.sexo,
            "height": self.altura,
            "weight": self.peso,
            "ap_hi": self.presion_sistolica,
            "ap_lo": self.presion_diastolica,
            "cholesterol": self.colesterol,
            "gluc": self.glucosa,
            "smoke": self.fuma,
            "alco": self.alcohol,
            "active": self.actividad_fisica,
            "BMI": self.bmi

        }

    def to_diabetes(self):
        """
        Convierte los datos al formato esperado
        por el modelo de diabetes.
        """

        return {

            "HighBP": int(
                self.presion_sistolica >= 140 or
                self.presion_diastolica >= 90
            ),

            "HighChol": int(
                self.colesterol > 1
            ),

            "CholCheck": 1,

            "BMI": self.bmi,

            "Smoker": self.fuma,

            "Stroke": 0,

            "HeartDiseaseorAttack": 0,

            "PhysActivity": self.actividad_fisica,

            "Fruits": self.frutas,

            "Veggies": self.verduras,

            "HvyAlcoholConsump": self.alcohol,

            "AnyHealthcare": 1,

            "NoDocbcCost": 0,

            "GenHlth": self.salud_general,

            "MentHlth": self.salud_mental,

            "PhysHlth": self.salud_fisica,

            "DiffWalk": self.dificultad_caminar,

            "Sex": self.sexo,

            "Age": self.edad,

            "Education": self.educacion,

            "Income": self.ingresos

        }