class ResponseAgent:

    def generate_response(self, state):

        hospital = state.selected_hospital

        return {
            "message": "Emergency response successfully coordinated.",

            "severity": state.triage_result["severity"],

            "reason": state.triage_result["reason"],

            "hospital": hospital["name"],

            "distance_km": hospital["distance_km"],

            "available_beds": (
                state.hospital_capacity[
                    hospital["name"]
                ]["available_beds"]
            ),

            "case_id": state.emergency_case["case_id"],

            "verification_passed": (
                state.verification_result["passed"]
            ),

            "status": "READY_FOR_EMERGENCY_RESPONSE"
        }