from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from aiosmtplib import send

from .settings_utils import get_settings

config = get_settings()


async def send_mail(to, subj, msg, text_type="plain"):
    """
    This function sends an email using SMTP.

    Args:
        to (str): Email recipient
        subj (str): Email subject
        msg (str): Email body
        text_type (str): Can be html or plain
    """
    message = MIMEMultipart("alternative")
    message["From"] = config.SMTP_FROM
    message["To"] = to
    message["Subject"] = subj
    mime_text = MIMEText(msg, text_type, "utf-8")
    message.attach(mime_text)

    await send(
        message,
        hostname=config.SMTP_HOST,
        port=config.SMTP_PORT,
        username=config.SMTP_USERNAME,
        password=config.SMTP_PASSWORD,
        use_tls=config.SMTP_TLS,
        #    start_tls = config.SMTP_START_TLS,
    )
