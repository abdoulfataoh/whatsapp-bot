# coding: utf-8

from typing import Dict
import requests
from urllib.parse import urljoin

from app import settings


_whatsapp_headers = {
    'Authorization': f'Bearer {settings.TOKEN}',
    'Content-Type': 'application/json'
}


def health() -> Dict[str, str]:
    return {'status': 'ok'}
