import json
import os
from datetime import datetime, timezone
from config import settings

class AuditLogger:
    def __init__(self, log_file: str = None):
        self.log_file = log_file or settings.LOG_FILE
        # Ensure file exists
        if not os.path.exists(self.log_file):
            with open(self.log_file, "w") as f:
                json.dump([], f)

    def log(self, event: dict):
        event["timestamp"] = datetime.now(timezone.utc).isoformat()

        try:
            with open(self.log_file, "r") as f:
                data = json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            data = []

        data.append(event)

        # Keep last 1000 entries
        if len(data) > 1000:
            data = data[-1000:]

        with open(self.log_file, "w") as f:
            json.dump(data, f, indent=2)

    def threat(self, ip: str, path: str, details: dict):
        self.log({
            "type": "THREAT",
            "ip": ip,
            "path": path,
            "score": details.get("score"),
            "categories": details.get("categories"),
            "matched": details.get("matched"),
        })

    def access(self, ip: str, path: str, target: str):
        self.log({
            "type": "ACCESS",
            "ip": ip,
            "path": path,
            "routed_to": target
        })
