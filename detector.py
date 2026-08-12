import re
from urllib.parse import unquote

class ThreatDetector:
    def __init__(self):
        self.patterns = {
            "sqli": [
                r"(\%27)|(\')|(\-\-)|(\%23)|(#)",
                r"((\%3D)|(=))[^\n]*((\%27)|(\')|(\-\-)|(\%3B)|(;))",
                r"\b(union|select|insert|update|delete|drop|truncate)\b",
                r"1\s*=\s*1",
                r"or\s+1\s*=\s*1",
            ],
            "xss": [
                r"<script.*?>",
                r"javascript:",
                r"onerror\s*=",
                r"onload\s*=",
                r"alert\s*\(",
            ],
            "path_traversal": [
                r"\.\./",
                r"\.\.\\",
                r"%2e%2e%2f",
                r"%2e%2e/",
            ],
            "scanner": [
                r"nikto",
                r"sqlmap",
                r"nmap",
                r"masscan",
                r"dirbuster",
                r"gobuster",
                r"wfuzz",
                r"burpsuite",
            ],
            "sensitive": [
                r"passwd",
                r"shadow",
                r"\.env",
                r"wp-config",
                r"phpinfo",
                r"admin",
                r"administrator",
            ]
        }

        self.compiled = {
            cat: [re.compile(p, re.IGNORECASE) for p in pats]
            for cat, pats in self.patterns.items()
        }

    def analyze(self, request_data: dict) -> dict:
        text_to_scan = " ".join([
            request_data.get("path", ""),
            request_data.get("query", ""),
            request_data.get("body", ""),
            request_data.get("user_agent", ""),
            request_data.get("referer", ""),
        ]).lower()

        text_to_scan = unquote(text_to_scan)

        matched = []
        categories = set()
        score = 0.0

        for category, patterns in self.compiled.items():
            for pattern in patterns:
                if pattern.search(text_to_scan):
                    matched.append(pattern.pattern)
                    categories.add(category)
                    if category in ["sqli", "xss"]:
                        score += 0.45
                    elif category == "scanner":
                        score += 0.6
                    else:
                        score += 0.3

        score = min(score, 1.0)

        return {
            "is_threat": score >= 0.6,
            "score": round(score, 2),
            "matched": matched[:8],
            "categories": list(categories)
        }
