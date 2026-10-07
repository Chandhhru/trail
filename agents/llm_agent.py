class LLMAgent:

    def analyze(self, patient_information):

        symptoms = patient_information.get(
            "symptoms", ""
        ).lower()

        if "chest pain" in symptoms:
            severity = "HIGH"
            concern = "Possible cardiac emergency"
            action = "Immediate emergency medical assessment required"

        elif "breathing" in symptoms or "breath" in symptoms:
            severity = "HIGH"
            concern = "Possible respiratory emergency"
            action = "Immediate emergency medical assessment required"

        elif "bleeding" in symptoms:
            severity = "HIGH"
            concern = "Possible serious bleeding"
            action = "Immediate emergency medical assessment required"

        else:
            severity = "MEDIUM"
            concern = "Medical assessment required"
            action = "Consult an appropriate medical professional"

        return {
            "severity": severity,
            "main_concern": concern,
            "recommended_action": action
        }