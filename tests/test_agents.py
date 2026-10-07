from core.state import EmergencyState
from agents.patient_agent import PatientAgent
from agents.triage_agent import TriageAgent
from agents.hospital_agent import HospitalAgent
from agents.capacity_agent import CapacityAgent
from agents.selection_agent import SelectionAgent


def test_patient_agent():

    agent = PatientAgent()

    result = agent.collect_information(
        "I have severe chest pain"
    )

    assert result["symptoms"] == "I have severe chest pain"


def test_triage_agent():

    agent = TriageAgent()

    patient = {
        "symptoms": "I have severe chest pain"
    }

    result = agent.analyze(patient)

    assert result["severity"] == "CRITICAL"


def test_hospital_agent():

    agent = HospitalAgent()

    hospitals = agent.find_hospitals("Chennai")

    assert len(hospitals) > 0


def test_capacity_agent():

    hospital_agent = HospitalAgent()
    capacity_agent = CapacityAgent()

    hospitals = hospital_agent.find_hospitals("Chennai")
    capacity = capacity_agent.check_capacity(hospitals)

    assert len(capacity) > 0


def test_selection_agent():

    hospital_agent = HospitalAgent()
    capacity_agent = CapacityAgent()
    selection_agent = SelectionAgent()

    hospitals = hospital_agent.find_hospitals("Chennai")
    capacity = capacity_agent.check_capacity(hospitals)

    selected = selection_agent.select_hospital(
        hospitals,
        capacity
    )

    assert selected is not None