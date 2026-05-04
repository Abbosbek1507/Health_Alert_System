# src/main.py

def health_alert_system(a, b, c, d):
    """Logic simulation based on CircuitVerse design."""
    A, B, C, D = bool(a), bool(b), bool(c), bool(d)

    # Y1 = (A AND B) OR C
    y1 = (A and B) or C

    # Y0 = NOT(Y1) AND (B OR D)
    y0 = (not y1) and (B or D)

    return int(y1), int(y0)


def generate_truth_table():
    print("\n" + "=" * 50)
    print(" TRUTH TABLE GENERATOR ")
    print("=" * 50)
    print("A(Sev.Symp) B(HighTemp) C(LowOxy) D(HighHR) | Y1(Help) Y0(Mon)")
    print("-" * 62)
    for i in range(16):
        a = (i >> 3) & 1
        b = (i >> 2) & 1
        c = (i >> 1) & 1
        d = i & 1
        y1, y0 = health_alert_system(a, b, c, d)
        print(f"     {a}           {b}            {c}          {d}     |   {y1}       {y0}")
    print("=" * 50 + "\n")


def interactive_mode():
    print("\n--- ENTER PATIENT SYMPTOMS ---")
    print("Type 1 for YES, 0 for NO")
    try:
        a = int(input("A - Severe Symptoms? [0/1]: "))
        b = int(input("B - High Temperature? [0/1]: "))
        c = int(input("C - Low Oxygen Level? [0/1]: "))
        d = int(input("D - High Heart Rate? [0/1]: "))

        if all(val in [0, 1] for val in [a, b, c, d]):
            y1, y0 = health_alert_system(a, b, c, d)
            print("\n>>> RESULTS <<<")
            print(f"Seek Medical Help (Y1) = {y1}")
            print(f"Monitor Patient (Y0)   = {y0}")

            if y1 == 1:
                print("STATUS: CRITICAL! Seek Medical Help Immediately.")
            elif y0 == 1:
                print("STATUS: WARNING! Monitor the patient closely.")
            else:
                print("STATUS: NORMAL. Patient is fine.")
        else:
            print("Error: Please enter only 0 or 1.")
    except ValueError:
        print("Error: Invalid input. Please enter numbers only.")


def main_menu():
    while True:
        print("\n=== HEALTH ALERT SYSTEM MENU ===")
        print("1. Enter Patient Data (Interactive Mode)")
        print("2. Generate Truth Table")
        print("3. Exit")
        choice = input("Select an option (1-3): ")

        if choice == '1':
            interactive_mode()
        elif choice == '2':
            generate_truth_table()
        elif choice == '3':
            print("Exiting program. Stay healthy!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main_menu()