class SelectionAgent:

    def select_hospital(self, hospitals, capacity):

        suitable_hospitals = []

        for hospital in hospitals:

            hospital_name = hospital["name"]

            hospital_capacity = capacity.get(
                hospital_name,
                {}
            )

            if (
                hospital["emergency_available"]
                and hospital_capacity.get("available_beds", 0) > 0
            ):
                suitable_hospitals.append(hospital)

        if not suitable_hospitals:
            return None

        suitable_hospitals.sort(
            key=lambda hospital: (
                -hospital["emergency_available"],
                -capacity[hospital["name"]]["available_beds"],
                hospital["distance_km"]
            )
        )

        return suitable_hospitals[0]