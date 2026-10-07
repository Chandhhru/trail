class PatientAgent:

    def collect_information(self, patient_request):

        information = {
            "request": patient_request,
            "patient_name": "Unknown",
            "age": "Unknown",
            "symptoms": patient_request,
            "location": "Chennai"
        }

        return information