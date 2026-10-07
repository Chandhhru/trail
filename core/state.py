class EmergencyState:

    def __init__(self):
        self.patient_request = None
        self.patient_information = None
        self.triage_result = None
        self.location = None
        self.nearby_hospitals = []
        self.hospital_capacity = {}
        self.selected_hospital = None
        self.emergency_case = None
        self.verification_result = None
        self.current_step = None