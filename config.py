from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # Ports
    GATEWAY_PORT: int = 8080
    REAL_APP_PORT: int = 3000
    HONEYPOT_PORT: int = 4000

    # Internal URLs
    REAL_APP_URL: str = "http://127.0.0.1:3000"
    HONEYPOT_URL: str = "http://127.0.0.1:4000"

    # Logging
    LOG_FILE: str = "enterprise_audit.json"
    LOG_LEVEL: str = "INFO"

    # Detection sensitivity (0.0 - 1.0)
    THREAT_THRESHOLD: float = 0.6

    class Config:
        env_file = ".env"

settings = Settings()
