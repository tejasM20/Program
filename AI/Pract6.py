def hospital_expert_system():
    print("🏥 Hospital Expert System")
    print("Available symptoms:")
    print("1. fever")
    print("2. cough")
    print("3. chest pain")
    print("4. headache")
    print("5. stomach pain")
    print("6. skin rash")
    print("7. breathing problem")
    print("8. dizziness")
    print("9. weakness")
    print("\nType 'exit' to quit.")

    while True:
        symptom = input("\nEnter your symptom: ").lower()

        if symptom == "exit":
            print("Thank you! Stay healthy 😊")
            break

        elif symptom == "fever":
            print("Advice: Consult General Physician.")

        elif symptom == "cough":
            print("Advice: Visit Pulmonology Department.")

        elif symptom == "chest pain":
            print("Advice: Consult Cardiology Department immediately.")

        elif symptom == "headache":
            print("Advice: Visit Neurology Department.")

        elif symptom == "stomach pain":
            print("Advice: Visit Gastroenterology Department.")

        elif symptom == "skin rash":
            print("Advice: Consult Dermatology Department.")

        elif symptom == "breathing problem":
            print("Advice: Visit Emergency or Pulmonology immediately.")

        elif symptom == "dizziness":
            print("Advice: Consult Neurology or General Physician.")

        elif symptom == "weakness":
            print("Advice: Get blood test and consult General Physician.")

        else:
            print("Advice: Symptom not recognized. Please consult General Physician.")


# Run the expert system
hospital_expert_system()