class HospitalSystem:
    def __init__(self):
        self.doctors = {
            "1": {"name": "Dr. Singh", "spec": "Cardiology", "slots": ["09:00", "10:00", "11:00"]},
            "2": {"name": "Dr. Joshi", "spec": "Physician", "slots": ["14:00", "15:00", "16:00"]},
            "3": {"name": "Dr. Sharma", "spec": "Dermatology", "slots": ["10:30", "13:00"]},
            "4": {"name": "Dr. Patel", "spec": "Orthopedics", "slots": ["09:30", "11:30", "14:30"]}

        }
        self.appointments = []

    def run(self):
        print("--- Welcome to the Modern Hospital System ---")
        
        while True:
            print("\n[MAIN MENU]")
            print("1. View Availability")
            print("2. Book Appointment")
            print("3. View Confirmed Bookings")
            print("4. Exit")
            
            choice = input("\nSelect an option (1-4): ")

            if choice == "1":
                print("\n--- Available Doctors & Slots ---")
                for id, info in self.doctors.items():
                    slots_left = ", ".join(info["slots"]) if info["slots"] else "Booked Out"
                    print(f"ID: {id} | {info['name']} ({info['spec']}) | Slots: {slots_left}")

            elif choice == "2":
                doc_id = input("Enter Doctor ID: ")
                if doc_id in self.doctors:
                    patient_name = input("Enter Patient Name: ")
                    print(f"Available slots for {self.doctors[doc_id]['name']}: {self.doctors[doc_id]['slots']}")
                    time_choice = input("Enter the preferred time slot: ")

                    if time_choice in self.doctors[doc_id]["slots"]:
                        self.doctors[doc_id]["slots"].remove(time_choice)
                        self.appointments.append({
                            "patient": patient_name,
                            "doctor": self.doctors[doc_id]["name"],
                            "time": time_choice
                        })
                        print(f"Success! {patient_name} is booked with {self.doctors[doc_id]['name']} at {time_choice}.")
                    else:
                        print("Error: Invalid or unavailable time slot.")
                else:
                    print("Error: Doctor ID not found.")

            elif choice == "3":
                print("\n--- Confirmed Appointments ---")
                if not self.appointments:
                    print("No appointments yet.")
                for appt in self.appointments:
                    print(f"Patient: {appt['patient']} | Doctor: {appt['doctor']} | Time: {appt['time']}")

            elif choice == "4":
                print("Exiting Stay healthy!")
                break
            else:
                print("Invalid selection. Please try again.")

if __name__ == "__main__":
    app = HospitalSystem()
    app.run()
