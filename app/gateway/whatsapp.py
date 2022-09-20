# coding: utf-8

import logging
from typing import Dict
import requests
from urllib.parse import urljoin

from app import settings


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)



class WhatsappAPI:
    _base_url: str
    _phone_id: str
    _headers: Dict[str, str]

    def __init__(self, base_url: str, phone_id: str, token: str) -> None:
        self._base_url = base_url
        self._phone_id = phone_id
        self._headers = {
            'Authorization': f'Bearer {settings.TOKEN}',
            'Content-Type': 'application/json'
        }

    def send_text(self, to: str, message: str) -> bool:
        url = urljoin(self._base_url, f'{self._phone_id}/messages' )
        logger.debug(url)
        data = {
            	"messaging_product": "whatsapp",
	            "to": to,
	            "type": "text",
	            "text": {"body": message, "preview_url": "false"}
        }
        r = requests.post(url, json=data, headers=self._headers)
        logger.debug(r.json())
        status = r.status_code == 200
        return status
