class CapacityAgent:

    def check_capacity(self, hospitals):

        capacity = {}

        for hospital in hospitals:

            capacity[hospital["name"]] = {
                "available_beds": hospital["available_beds"],
                "emergency_ready": hospital["emergency_available"]
            }

        return capacity