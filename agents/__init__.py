def __init__(self):
    self.state = EmergencyState()
    self.planner = Planner()
    self.patient_agent = PatientAgent()
    self.triage_agent = TriageAgent()
    self.hospital_agent = HospitalAgent()
    self.selection_agent = SelectionAgent()
    self.verification_agent = VerificationAgent()