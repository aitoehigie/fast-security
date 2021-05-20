import httpx
from .settings_utils import get_settings

async def send_sms(to, msg):
    """
    Sends a text directly to a phone number using Twilio

    Args:
        to (str): Phone number to receive the text
        msg (str): Message to be sent.
    """
