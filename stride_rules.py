STRIDE_RULES = {
    "Authentication": {
        "Spoofing": "Weak authentication mechanisms",
        "Tampering": "Session or token manipulation",
        "Repudiation": "Lack of authentication logs",
        "Information Disclosure": "Credential leakage",
        "Denial of Service": "Brute-force login attempts",
        "Elevation of Privilege": "Privilege escalation via auth flaws"
    },
    "Backend": {
        "Tampering": "Injection attacks (SQL, command)",
        "Repudiation": "Insufficient request logging",
        "Information Disclosure": "Verbose error messages",
        "Denial of Service": "Resource exhaustion",
        "Elevation of Privilege": "Insecure role enforcement"
    },
    "Database": {
        "Tampering": "Unauthorized data modification",
        "Information Disclosure": "Unencrypted sensitive data",
        "Denial of Service": "Database locking or flooding",
        "Elevation of Privilege": "Excessive database permissions"
    }
}