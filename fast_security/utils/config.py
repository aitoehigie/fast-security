from pydantic import BaseSettings


class Settings(BaseSettings):
    # Database settings
    DB_SCHEME: str
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: str
    DB_NAME: str

    # JWT settings
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
