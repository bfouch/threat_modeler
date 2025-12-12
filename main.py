from stride_rules import STRIDE_RULES
from risk_scoring import calculate_risk
from mitigations import MITIGATIONS

def main():
    print("=== Threat Modeling Automation Tool ===\n")

    system_name = input ("System name: ")
    handles_pii = input("Does the system handle PII? (yes/no): ").lower() == "yes"
    public_facing = input("Is the system public-facing? (yes/no): ").lower() == "yes"

    print("\nSelect components (comma-separated):")
    print("Authentication, Backend, Database")
    components = input("> ").split(",")

    report =[]
    report.append(f"Threat Model Report for: {system_name}\n")

    for component in components:
        component = component.strip()
        if component not in STRIDE_RULES:
            continue

        report.append(F"\nComponent: {component}")

        for threat, description in STRIDE_RULES[component].items():
            risk = calculate_risk(handles_pii, public-facing, threat)
            mitigation = MITIGATIONS.get(threat, "Review security controls")

            report.append(
                f"- {threat}: {description}\n"
                f"  Risk Level: {risk}\n"
                f"  Mitigation: {mitigation}"
                )

    filename = f"{system__name.replace(' ', '_').lower()}_threat_model.txt"
    with open(filename, "w") as f:
        f.write("\n".join(report))

    print(f"\n Threat model generate: {filename}")

if __name__ == "__main__":
    main()