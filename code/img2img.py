import base64
import os
import requests
from dotenv import load_dotenv

load_dotenv('.env')

engine_id = "stable-diffusion-xl-1024-v1-0"
api_host = os.getenv("API_HOST", "https://api.stability.ai")
api_key = os.getenv("STABILITY_API_KEY")

if api_key is None:
    raise Exception("Missing Stability API key.")

def reimagine(engine_id, api_host, api_key):
    response = requests.post(
    f"{api_host}/v1/generation/{engine_id}/image-to-image",
    headers={
        "Accept": "application/json",
        "Authorization": f"Bearer {api_key}"
    },
    files={
        "init_image": open("image_path", "rb")
    },
    data = {
        "step_schedule_start": 0.65, # 0 = original, 1 = new image
        "init_image_mode": "STEP_SCHEDULE",
        "steps": 40,
        "cfg_scale": 5.5,
        "samples": 1,
        "style_preset": "fantasy-art",
        "text_prompts[0][text]":  "goddess of the forest",
        "text_prompts[0][weight]": 0.9,
        "text_prompts[1][text]":  "The artwork showcases excellent anatomy with a clear, complete, and appealing "
                                  "depiction. It has well-proportioned and polished details, presenting a unique "
                                  "and balanced composition. The high-resolution image is undamaged and well-formed, "
                                  "conveying a healthy and natural appearance without mutations or blemishes. The "
                                  "positive aspect of the artwork is highlighted by its skillful framing and realistic "
                                  "features, including a well-drawn face and hands. The absence of signatures contributes "
                                  "to its seamless and authentic quality, and the depiction of straight fingers adds to "
                                  "its overall attractiveness.",
        "text_prompts[1][weight]": 0.3,
        "text_prompts[2][text]":  "2 faces, 2 heads, bad anatomy, blurry, cloned face, cropped image, cut-off, deformed hands, "
                                  "disconnected limbs, disgusting, disfigured, draft, duplicate artifact, extra fingers, extra limb, "
                                  "floating limbs, gloss proportions, grain, gross proportions, long body, long neck, low-res, mangled, "
                                  "malformed, malformed hands, missing arms, missing limb, morbid, mutation, mutated, mutated hands, "
                                  "mutilated, mutilated hands, multiple heads, negative aspect, out of frame, poorly drawn, poorly drawn "
                                  "face, poorly drawn hands, signatures, surreal, tiling, twisted fingers, ugly",
        "text_prompts[2][weight]": -1,
    }
)
    return response

response = reimagine(engine_id, api_host, api_key)

if response.status_code != 200:
    raise Exception("Non-200 response: " + str(response.text))
else :
    data = response.json()
    if not os.path.exists("./out"):
        os.makedirs("./out")
    for i, image in enumerate(data["artifacts"]):
        with open(f'./out/img2img_{image["seed"]}.png', "wb") as f:
            f.write(base64.b64decode(image["base64"]))
        print("Image successfully generated and saved.")
