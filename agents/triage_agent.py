class TriageAgent:

    def analyze(self, patient_information):

        symptoms = patient_information.get(
            "symptoms", ""
        ).lower()

        if "chest pain" in symptoms:
            severity = "CRITICAL"
            reason = "Possible cardiac emergency"

        elif "breathing" in symptoms or "breath" in symptoms:
            severity = "CRITICAL"
            reason = "Possible respiratory emergency"

        elif "bleeding" in symptoms:
            severity = "CRITICAL"
            reason = "Possible serious bleeding"

        elif "accident" in symptoms or "injury" in symptoms:
            severity = "HIGH"
            reason = "Possible trauma emergency"

        else:
            severity = "MEDIUM"
            reason = "Medical assessment required"

        return {
            "severity": severity,
            "reason": reason
        }