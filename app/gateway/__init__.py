# coding: utf-8

from app import settings
from app.gateway.whatsapp import WhatsappAPI

whatsapp_api = WhatsappAPI(
    base_url= settings.API_URL,
    phone_id=settings.PHONE_NUMBER_ID,
    token=settings.TOKEN
)