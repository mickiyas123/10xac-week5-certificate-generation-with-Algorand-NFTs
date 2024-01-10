from openai import OpenAI
from dotenv import load_dotenv
import os
from pathlib import Path
import json
import requests
import concurrent.futures
import random
import string

DATA_DIR = Path.cwd() / "Download"
subfolder_name = "Certificates"
subfolder_path = DATA_DIR / subfolder_name
file_path = DATA_DIR.joinpath("base_certificate_image_url.json")

DATA_DIR.mkdir(exist_ok=True)
subfolder_path.mkdir(parents=True, exist_ok=True)
certificate_path = subfolder_path.joinpath("certificate_1.png")


load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)


def generate_cretificate_background(prompt):
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


prompts = [
    "Clean, beautiful, elegant, and simple \
    certificate background with a combination \
    of black and gold colors with a placeholder \
    to write the name and other information.",
    "Clean, beautiful, elegant, and simple \
    certificate background with a combination \
    of black and silver colors with a placeholder \
    to write the name and other information.",
    "Clean, beautiful, elegant, and simple \
    certificate background with a combination \
    of black and bronze colors with a placeholder \
    to write the name and other information.",
]


def download_generated_image(image_url, path):
    try:
        image_data = requests.get(image_url)
        with open(path, "wb") as file:
            file.write(image_data.content)
    except requests.exceptions.RequestException as e:
        print(f"Error downloading image: {e}")


with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(generate_cretificate_background, prompts)
