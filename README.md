# Threat Modeling Automation Tool (CLI)

## Overview
This project is a Python-based command-line tool that assists with early-stage security threat modeling using the STRIDE framework. It gathers basic system information and automatically identifies potential threats, assigns qualitative risk levels, and suggests mitigations to support consistent and repeatable security analysis.

This tool is intended for educational and demonstration purposes and does not replace formal security assessments.

---

## Features
- STRIDE-based threat identification
- Component-level threat mapping
- Qualitative risk scoring (Low / Medium / High)
- Built-in mitigation recommendations
- Generates a structured threat model report
- Simple CLI interface with no external dependencies

---

## How It Works
1. The user provides high-level system details such as system name, exposure level, and data sensitivity.
2. The tool maps selected system components to STRIDE threat categories.
3. Each identified threat is evaluated using a rule-based risk scoring approach.
4. A threat model report is generated summarizing threats, risk levels, and recommended mitigations.

---

## Supported Components (V1)
- Authentication
- Backend
- Database

Additional components may be added in future versions.

---

## Getting Started

### Prerequisites
- Python 3.9 or higher
- Windows, macOS, or Linux

### Installation
Clone the repository:
git clone https://github.com/your-username/threat-modeling-cli.git

cd threat-modeling-cli

Run the tool:

python main.py
(On Windows, you may also use `py main.py`.)

---

## Example Usage
System name: Customer Banking Database
Does the system handle PII? yes
Is the system public-facing? no
Components: Database

Output:

Threat Model Report for: Customer Banking Database


Component: Database
- Tampering: Unauthorized data modification
  Risk Level: Medium
  Mitigation: Validate input and use integrity checks
- Information Disclosure: Unencrypted sensitive data
  Risk Level: Medium
  Mitigation: Encrypt sensitive data in transit and at rest
- Denial of Service: Database locking or flooding
  Risk Level: Medium
  Mitigation: Apply rate limiting and monitoring
- Elevation of Privilege: Excessive database permissions
  Risk Level: Medium
  Mitigation: Use least privilege and role-based access control


---

## Project Structure
threat-modeling-cli/
├── main.py
├── stride_rules.py
├── risk_scoring.py
├── mitigations.py
└── README.md

---

## Limitations
- This tool uses rule-based logic and does not perform live vulnerability scanning.
- Risk levels are qualitative and intended for guidance only.
- Results should be reviewed by a security professional as part of a formal threat modeling process.

---

## Future Enhancements
- Additional system components (API, Network, Cloud)
- CSV / PDF export
- OWASP Top 10 tagging
- Configurable risk scoring logic
- Optional web interface

---

## License
MIT License
