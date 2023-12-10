# Image Processing Toolkit (IPT)

## Overview

The Image Processing Toolkit (IPT) is a versatile project featuring five Python scripts that leverage the Stability AI API. Each script is tailored for specific image-related tasks, including image creation, modification through textual prompts, high-quality upscaling, and interacting with the Stability AI API to check account balance and list available engines.

### 1. Text-to-Image Generation

#### File: `text2img.py`

This script generates vibrant and unique images based on textual prompts. Here's a more detailed breakdown:

- **API Interaction:**
  - Utilizes the Stability AI API for text-to-image generation.
  - The `imagine` function initiates a POST request, incorporating parameters such as engine ID, text prompts, and image dimensions.

- **Text Prompts:**
  - Three carefully crafted text prompts guide the generation process.
  - Positive and negative aspects are strategically weighted to influence the AI's creative process.

- **Output Handling:**
  - Images are saved in the `./out` directory with filenames reflecting the seed values.
  - The script automatically creates the `./out` directory if it doesn't exist.

- **Potential Use Cases:**
  - Ideal for generating artistic and imaginative images based on specific textual descriptions.

### 2. Image-to-Image Transformation

#### File: `img2img.py`

This script transforms existing images based on textual prompts. Let's delve deeper:

- **API Interaction:**
  - Leverages the Stability AI API for image-to-image transformation.
  - The `reimagine` function orchestrates a POST request, incorporating the initial image and parameters for style, text prompts, and transformation steps.

- **Text Prompts:**
  - The same three text prompts, now applied to the initial image, influence the transformation process.

- **Output Handling:**
  - Resulting images are stored in the `./out` directory, preserving seed-based filenames.

- **Potential Use Cases:**
  - Useful for altering existing images according to specific themes or artistic styles.

### 3. Image Upscaling

#### File: `img2ups.py`

This script enhances image resolution through advanced upscaling techniques. Let's explore its features:

- **API Interaction:**
  - Employs the Stability AI API, specifically utilizing the ESRGAN engine for image upscaling.
  - The `image_upscaling` function orchestrates a POST request, incorporating the target image and desired height.

- **Output Handling:**
  - The upscaled image is saved in the `./out` directory as `img2ups.png`.

### 4. Check Account Balance

#### File: `check_balance.py`

This script interacts with the Stability AI API to check the account balance. Here are the key features:

- **API Interaction:**
  - Sends a GET request to the `/v1/user/balance` endpoint to retrieve the account balance.

- **Output Handling:**
  - The response payload is printed, providing information about the account balance.

### 5. List Available Engines

#### File: `list_engines.py`

This script interacts with the Stability AI API to list available engines. Let's explore its features:

- **API Interaction:**
  - Sends a GET request to the `/v1/engines/list` endpoint to retrieve the list of available engines.

- **Output Handling:**
  - The response payload is printed, providing information about the available engines.

## Getting Started

### 1. Obtain the Stability API Key

Before running the scripts, ensure you have a Stability API key. If you don't have one, you can obtain it by visiting [https://platform.stability.ai/account/keys](https://platform.stability.ai/account/keys).

### 2. Create the `.env` File

Create a file named `.env` in the root directory of the project. Add the following content to the `.env` file:

```env
API_HOST=https://api.stability.ai
STABILITY_API_KEY=YOUR_STABILITY_API_KEY
```

Replace `YOUR_STABILITY_API_KEY` with the API key you obtained from the Stability AI platform.

## Usage

1. **Dependencies Installation:**
   - Ensure you have the required dependencies installed. You can install them using:

     ```bash
     pip install -r requirements.txt
     ```

2. **Script Execution:**
   - Run each script individually based on your requirements.
     Example:

     ```bash
     python check_balance.py
     ```

## Important Considerations

- **Security:**
  - Handle API keys securely. Keep the `.env` file confidential to prevent unauthorized access.

- **Output Directory:**
  - The `./out` directory is automatically created to store generated and modified images. Ensure the script has write permissions in this directory.

- **Customization:**
  - Feel free to customize the scripts or integrate them into larger workflows based on your project's needs.

---

The Image Processing Toolkit (IPT) is designed to simplify image-related tasks with ease. If you have any specific requirements or additional details to include, please let me know!
