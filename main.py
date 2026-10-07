from agents.orchestrator import Orchestrator


def main():
    orchestrator = Orchestrator()

    patient_request = "I have severe chest pain"

    orchestrator.start(patient_request)


if __name__ == "__main__":
    main()