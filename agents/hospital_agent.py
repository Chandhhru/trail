from core.hospital_data import HOSPITALS


class HospitalAgent:

    def find_hospitals(self, location):

        hospitals = []

        for hospital in HOSPITALS:

            if hospital["location"].lower() == location.lower():
                hospitals.append(hospital)

        return hospitals