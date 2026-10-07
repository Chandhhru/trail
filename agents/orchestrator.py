from core.state import EmergencyState
from agents.planner import Planner
from agents.patient_agent import PatientAgent
from agents.triage_agent import TriageAgent
from agents.hospital_agent import HospitalAgent
from agents.selection_agent import SelectionAgent
from agents.verification_agent import VerificationAgent
from agents.capacity_agent import CapacityAgent
from agents.emergency_case_agent import EmergencyCaseAgent
from agents.llm_agent import LLMAgent
from agents.response_agent import ResponseAgent


class Orchestrator:

    def __init__(self):
        self.state = EmergencyState()

        self.planner = Planner()
        self.patient_agent = PatientAgent()
        self.triage_agent = TriageAgent()
        self.hospital_agent = HospitalAgent()
        self.selection_agent = SelectionAgent()
        self.verification_agent = VerificationAgent()
        self.capacity_agent = CapacityAgent()
        self.emergency_case_agent = EmergencyCaseAgent()
        self.llm_agent = LLMAgent()
        self.response_agent = ResponseAgent()

    def start(self, patient_request):

        try:
            # 1. Start
            self.state.patient_request = patient_request
            self.state.current_step = "STARTED"

            print("ORCHESTRATOR STARTED")
            print("Patient:", patient_request)

            # 2. Create plan
            plan = self.planner.create_plan()

            self.state.current_step = "PLAN_CREATED"

            print("\nEmergency Response Plan:")

            for number, step in enumerate(plan, start=1):
                print(f"{number}. {step}")

            # 3. Patient information
            self.state.patient_information = (
                self.patient_agent.collect_information(
                    patient_request
                )
            )

            self.state.current_step = (
                "PATIENT_INFORMATION_COLLECTED"
            )

            print("\nPatient Information:")
            print(self.state.patient_information)

            # 4. Local AI analysis
            print("\nLLM Analysis:")

            llm_result = self.llm_agent.analyze(
                self.state.patient_information
            )

            print(llm_result)

            # 5. Triage
            self.state.triage_result = (
                self.triage_agent.analyze(
                    self.state.patient_information
                )
            )

            self.state.current_step = "TRIAGE_COMPLETED"

            print("\nTriage Result:")
            print(self.state.triage_result)

            # 6. Location
            self.state.location = "Chennai"

            # 7. Find hospitals
            self.state.nearby_hospitals = (
                self.hospital_agent.find_hospitals(
                    self.state.location
                )
            )

            if not self.state.nearby_hospitals:
                raise Exception("No hospitals found")

            self.state.current_step = "HOSPITALS_FOUND"

            print("\nNearby Hospitals:")

            for hospital in self.state.nearby_hospitals:
                print(
                    f"- {hospital['name']} "
                    f"({hospital['distance_km']} km)"
                )

            # 8. Hospital capacity
            self.state.hospital_capacity = (
                self.capacity_agent.check_capacity(
                    self.state.nearby_hospitals
                )
            )

            self.state.current_step = "CAPACITY_CHECKED"

            print("\nHospital Capacity:")
            print(self.state.hospital_capacity)

            # 9. Hospital selection
            self.state.selected_hospital = (
                self.selection_agent.select_hospital(
                    self.state.nearby_hospitals,
                    self.state.hospital_capacity
                )
            )

            if self.state.selected_hospital is None:
                raise Exception(
                    "No suitable hospital available"
                )

            self.state.current_step = "HOSPITAL_SELECTED"

            print("\nSelected Hospital:")
            print(self.state.selected_hospital)

            # 10. Emergency case
            self.state.emergency_case = (
                self.emergency_case_agent.create_case(
                    self.state
                )
            )

            self.state.current_step = (
                "EMERGENCY_CASE_CREATED"
            )

            print("\nEmergency Case:")
            print(self.state.emergency_case)

            # 11. Verification
            self.state.verification_result = (
                self.verification_agent.verify(
                    self.state
                )
            )

            self.state.current_step = (
                "VERIFICATION_COMPLETED"
            )

            print("\nVerification Result:")
            print(self.state.verification_result)

            # 12. Final response
            final_response = (
                self.response_agent.generate_response(
                    self.state
                )
            )

            self.state.current_step = "RESPONSE_GENERATED"

            print("\nFINAL RESPONSE:")
            print(final_response)

            print(
                "\nFinal Status:",
                self.state.current_step
            )

            return final_response

        except Exception as error:

            self.state.current_step = "ERROR"

            print("\nERROR:")
            print(error)

            return None