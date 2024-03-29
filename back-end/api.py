from fastapi import FastAPI, Path
from openai import OpenAI
from dotenv import load_dotenv
import os
from pathlib import Path
import requests
import concurrent.futures
import random
import string
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Prompts(BaseModel):
    prompts: List[str]


DATA_DIR = Path.cwd() / "Download"
subfolder_name = "Certificates"
subfolder_path = DATA_DIR / subfolder_name

DATA_DIR.mkdir(exist_ok=True)
subfolder_path.mkdir(parents=True, exist_ok=True)

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)

def generate_certificate_background(prompt: str):
    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size="1024x1024",
        n=1,
        response_format="url",
    )
    file_name = "".join(random.choices(string.ascii_letters, k=5))
    download_generated_image(
        response.data[0].url, subfolder_path.joinpath(f"certificate_{file_name}.png")
    )
def download_generated_image(image_url, path):
    try:
        image_data = requests.get(image_url)
        with open(path, "wb") as file:
            file.write(image_data.content)
    except requests.exceptions.RequestException as e:
        print(f"Error downloading image: {e}")

@app.get("/")
def index():
    return {"message": "This is a home route"}

@app.post("/generate-certificate")
async def generate_cerrtificte(prompts: Prompts):
    promts_to_be_generated = prompts.prompts
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(generate_certificate_background, promts_to_be_generated)