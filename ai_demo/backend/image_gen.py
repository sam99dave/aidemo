import requests
import os
import io
import time
from PIL import Image
from dotenv import load_dotenv

load_dotenv()

API_URL = os.getenv('FLUX_HF_ENDPOINT', default=None)
HF_TOKEN = os.getenv('HF_TOKEN', default=False)

def generate_image(payload):
    print(f'HF API call....')
    headers={
        "Authorization": f"Bearer {HF_TOKEN}"
    }
   
    response = requests.post(
        API_URL,
        headers=headers,
        json=payload
    )
    
    print(f'HF API response: {response}')

    return Image.open(io.BytesIO(response.content))