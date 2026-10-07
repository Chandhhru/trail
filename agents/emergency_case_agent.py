class EmergencyCaseAgent:

    def create_case(self, state):

        case = {
            "case_id": "EMG-001",
            "patient_request": state.patient_request,
            "patient_information": state.patient_information,
            "severity": state.triage_result["severity"],
            "reason": state.triage_result["reason"],
            "selected_hospital": state.selected_hospital["name"],
            "hospital_distance_km": state.selected_hospital["distance_km"],
            "status": "EMERGENCY_CASE_CREATED"
        }

        return case