def calculate_risk(handles_pii, public_facing, threat_type):
    likelihood = 1
    impact = 1

    if public_facing:
        likelihood += 2

    if handles_pii:
        impact += 3

    if threat_type in ["Elevation of Privilege", "Information Disclosure"]:
        impact += 2

    score = likelihood * impact

    if score >= 7:
        return "High"
    elif score >= 4:
        return "Medium"
    else:
        return "Low"