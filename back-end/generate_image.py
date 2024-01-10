from openai import OpenAI
from dotenv import load_dotenv
import os
from pathlib import Path
import json
import requests


DATA_DIR = Path.cwd() / "Download"
subfolder_name = "Certificates"
subfolder_path = DATA_DIR / subfolder_name
file_path = DATA_DIR.joinpath("base_certificate_image_url.json")

DATA_DIR.mkdir(exist_ok=True)
subfolder_path.mkdir(parents=True, exist_ok=True)
certificate_path = subfolder_path.joinpath("certificate_1.png")


load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


def generate_cretificate_background(prompt):
    client = OpenAI(api_key=OPENAI_API_KEY)

    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size="1024x1024",
        quality="standard",
        n=1,
        response_format="url",
    )
    data_to_save = {"url": response.data[0].url}
    with open(file_path, mode="w", encoding="utf-8") as file:
        json.dump(data_to_save, file)


# generate_cretificate_background(
#     "Clean, beautiful, elegant, and simple \
#     certificate background with combination of black and gold colors with \
#     placeholder to write name and other information with the corect spelling"
#     )

with open(file_path, "r", encoding="utf-8") as file:
    data = json.load(file)

image_url = data["url"]


def download_generated_image(image_url, path):
    image_data = requests.get(image_url)
    with open(path, "wb") as file:
        file.write(image_data.content)


download_generated_image(image_url, certificate_path)
