from pydantic import BaseSettings


class Settings(BaseSettings):
    # Database settings
    SCHEME: str
    USER: str
    PASSWORD: str
    HOST: str
    PORT: str
    DB_NAME: str
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # Twilio settings
    #    TWILIO_SID: str
    #    TWILIO_TOKEN: str
    #    TWILIO_FROM: str

    # SMTP settings
    SMTP_HOST: str
    SMTP_PORT: int
    SMTP_USERNAME: str
    SMTP_PASSWORD: str
    SMTP_FROM: str
    SMTP_TLS: str = "true"
    SMTP_START_TLS: str = "true"

    class Config:
        env_file = ""  # Path to .env file
