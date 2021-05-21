from pydantic import BaseSettings


class Settings(BaseSettings):
    ENGINE: str
    USER: str
    PASSWORD: str
    HOST: str
    PORT: str
    DB_NAME: str
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # Twilio settings
    TWILIO_SID: str
    TWILIO_TOKEN: str
    TWILIO_FROM: str

    class Config:
        env_file = ".env"
