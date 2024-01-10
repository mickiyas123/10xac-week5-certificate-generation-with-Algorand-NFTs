import cv2 as cv
from datetime import date
from pathlib import Path


DATA_DIR = Path.cwd() / "Download/Certificates/Final"
DATA_DIR.mkdir(parents=True, exist_ok=True)

gold_image = cv.imread("./Download/Certificates/certificate_aWxfb.png")
silver_image = cv.imread("./Download/Certificates/certificate_AUaHJ.png")
bronze_image = cv.imread("./Download/Certificates/certificate_LJZdo.png")
logo_image = cv.imread("./Download/Logo/TenxLogo.png")

params = {
    "name": "John Doe",
    "text": "challenge completion",
    "date": str(date.today()),
}


def edit_bronze_image(img, certificate_params):
    texts = [
        certificate_params["name"],
        certificate_params["text"],
        certificate_params["date"],
    ]
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
            img, text, position, font,
            font_scale, font_color, font_thickness)
    logo_width = 100  # Adjust as needed
    logo_height = 100  # Adjust as needed
    resized_logo = cv.resize(logo_image, (logo_width, logo_height))

    logo_position = (275, 180)
    img[
        logo_position[1]:logo_position[1] + logo_height,
        logo_position[0]:logo_position[0] + logo_width,
    ] = resized_logo

    cv.imwrite(str(DATA_DIR / "bronze_certificate.png"), img)
    cv.imshow("bronze_certificate", img)
    cv.waitKey(0)
    cv.destroyAllWindows()


def edit_gold_image(img, certificate_params):
    texts = [
        certificate_params["name"],
        certificate_params["text"],
        certificate_params["date"],
    ]
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
        cv.putText(img, text, position, font, 
                   font_scale, font_color, font_thickness)
    logo_width = 100  # Adjust as needed
    logo_height = 100  # Adjust as needed
    resized_logo = cv.resize(logo_image, (logo_width, logo_height))

    logo_position = (275, 180)
    img[
        logo_position[1]:logo_position[1] + logo_height,
        logo_position[0]:logo_position[0] + logo_width,
    ] = resized_logo
    cv.imwrite(str(DATA_DIR / "gold_certificate.png"), img)
    cv.imshow("gold_certificate", img)
    cv.waitKey(0)
    cv.destroyAllWindows()


def edit_silver_image(img, certificate_params):
    texts = [
        certificate_params["name"],
        certificate_params["text"],
        certificate_params["date"],
    ]
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
        cv.putText(img, text, position, font, 
                   font_scale, font_color, font_thickness)
    logo_width = 100  # Adjust as needed
    logo_height = 100  # Adjust as needed
    resized_logo = cv.resize(logo_image, (logo_width, logo_height))

    logo_position = (470, 200)
    img[
        logo_position[1]:logo_position[1] + logo_height,
        logo_position[0]:logo_position[0] + logo_width,
    ] = resized_logo
    cv.imwrite(str(DATA_DIR / "silver_certificate.png"), img)
    cv.imshow("gold_certificate", img)
    cv.waitKey(0)
    cv.destroyAllWindows()


# edit_bronze_image(bronze_image, params)
# edit_gold_image(gold_image, params)
# edit_silver_image(silver_image, params)
