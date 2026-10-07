class VerificationAgent:

    def verify(self, state):

        checks = {
            "patient_information": state.patient_information is not None,
            "triage": state.triage_result is not None,
            "hospitals_found": len(state.nearby_hospitals) > 0,
            "hospital_selected": state.selected_hospital is not None
        }

        passed = all(checks.values())

        return {
            "passed": passed,
            "checks": checks
        }