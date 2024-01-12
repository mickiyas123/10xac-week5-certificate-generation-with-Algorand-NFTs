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
import cv2 as cv
from datetime import date

app = FastAPI()


class Prompts(BaseModel):
    prompts: List[str]


class Certificate_Params(BaseModel):
    name: str
    text: str


DATA_DIR = Path.cwd() / "Download"
subfolder_name = "Certificates"
subfolder_path = DATA_DIR / subfolder_name

DATA_DIR.mkdir(exist_ok=True)
subfolder_path.mkdir(parents=True, exist_ok=True)

FINAL_DIR = Path.cwd() / "Download/Certificates/Final"
FINAL_DIR.mkdir(parents=True, exist_ok=True)

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)

gold_image = cv.imread("./Download/Certificates/certificate_aWxfb.png")
silver_image = cv.imread("./Download/Certificates/certificate_AUaHJ.png")
bronze_image = cv.imread("./Download/Certificates/certificate_LJZdo.png")
logo_image = cv.imread("./Download/Logo/TenxLogo.png")


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


@app.post("/generate-gold-certificate")
def generate_gold_certificate(certificate_params: Certificate_Params):
    try:
        img = gold_image
        texts = [certificate_params.name, certificate_params.text, str(date.today())]
        posiitons = [(360, 460), (370, 600), (410, 690)]
        font_scales = [2, 1, 1]
        font_thicknesses = [8, 2, 2]
        font = cv.FONT_HERSHEY_SIMPLEX
        font_scale = 2
        font_thickness = 8
        font_color = (0, 0, 0)
        for text, position, font_scale, font_thickness in zip(
            texts, posiitons, font_scales, font_thicknesses
        ):
            cv.putText(
                img, text, position, font, font_scale, font_color, font_thickness
            )
        logo_width = 100  # Adjust as needed
        logo_height = 100  # Adjust as needed
        resized_logo = cv.resize(logo_image, (logo_width, logo_height))

        logo_position = (275, 180)
        img[
            logo_position[1] : logo_position[1] + logo_height,
            logo_position[0] : logo_position[0] + logo_width,
        ] = resized_logo
        cv.imwrite(
            str(FINAL_DIR / f"{certificate_params.name}_gold_certificate.png"), img
        )
        return {"Message": "Succesfuly created gold certificate"}
    except Exception as e:
        return {"Error": f"Error editing gold certificate image: {e}"}


@app.post("/generate-silver-certificate")
def generate_silver_certificate(certificate_params: Certificate_Params):
    img = silver_image
    try:
        texts = [certificate_params.name, certificate_params.text, str(date.today())]

        posiitons = [(440, 380), (350, 460), (400, 520)]
        font_scales = [1, 1, 1]
        font_thicknesses = [4, 2, 2]
        font = cv.FONT_HERSHEY_SIMPLEX
        font_scale = 2
        font_thickness = 8
        font_color = (0, 0, 0)
        for text, position, font_scale, font_thickness in zip(
            texts, posiitons, font_scales, font_thicknesses
        ):
            cv.putText(
                img, text, position, font, font_scale, font_color, font_thickness
            )
        logo_width = 100  # Adjust as needed
        logo_height = 100  # Adjust as needed
        resized_logo = cv.resize(logo_image, (logo_width, logo_height))

        logo_position = (470, 200)
        img[
            logo_position[1] : logo_position[1] + logo_height,
            logo_position[0] : logo_position[0] + logo_width,
        ] = resized_logo
        cv.imwrite(
            str(FINAL_DIR / f"{certificate_params.name}_silver_certificate.png"), img
        )
        return {"Message": "Succesfuly created gold certificate"}
    except Exception as e:
        return {"Error": f"Error editing gold certificate image: {e}"}


@app.post("/generate-bronze-certificate")
def generate_bronze_certificate(certificate_params: Certificate_Params):
    try:
        img = bronze_image
        texts = [certificate_params.name, certificate_params.text, str(date.today())]
        posiitons = [(360, 460), (370, 600), (410, 690)]
        font_scales = [2, 1, 1]
        font_thicknesses = [8, 2, 2]
        font = cv.FONT_HERSHEY_SIMPLEX
        font_scale = 2
        font_thickness = 8
        font_color = (0, 0, 0)
        for text, position, font_scale, font_thickness in zip(
            texts, posiitons, font_scales, font_thicknesses
        ):
            cv.putText(
                img, text, position, font, font_scale, font_color, font_thickness
            )
        logo_width = 100  # Adjust as needed
        logo_height = 100  # Adjust as needed
        resized_logo = cv.resize(logo_image, (logo_width, logo_height))

        logo_position = (275, 180)
        img[
            logo_position[1] : logo_position[1] + logo_height,
            logo_position[0] : logo_position[0] + logo_width,
        ] = resized_logo

        cv.imwrite(
            str(FINAL_DIR / f"{certificate_params.name}_bronze_certificate.png"), img
        )
        return {"Message": "Succesfuly created gold certificate"}
    except Exception as e:
        return {"Error": f"Error editing gold certificate image: {e}"}
