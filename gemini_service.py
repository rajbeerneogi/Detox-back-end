import os
from dotenv import load_dotenv
from google import genai
from PIL import Image

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
MODEL_ID = os.getenv("GEMINI_MODEL", "gemini-3.8-flash")

if not API_KEY:
    raise RuntimeError("GEMINI_API_KEY is missing from .env")

client = genai.Client(api_key=API_KEY)


def analyze_water_sample(image: Image.Image) -> str:
    """
    Analyse visible characteristics of a water-sample image.
    This function does not measure actual water quality.
    """

    prompt = """
    You are Detox, an AI assistant for visual water-sample analysis.

    Examine the supplied photograph and describe:

    1. Visible water colour.
    2. Apparent visual clarity.
    3. Visible floating particles.
    4. Possible visible sediment.
    5. Any algae-like visual appearance.
    6. Potential visual concerns and sensible next steps.

    IMPORTANT SCIENTIFIC LIMITATIONS:

    - Describe only what can reasonably be observed.
    - Do not invent pH, TDS, turbidity, or other measurements.
    - Do not claim to identify bacteria, heavy metals, or chemicals.
    - Do not determine whether the water is safe to drink.
    - Explain that clear-looking water is not necessarily safe.
    - Recommend appropriate physical or laboratory testing
      when necessary.

    Use clear, simple language.
    """

    try:
        response = client.models.generate_content(
            model=MODEL_ID,
            contents=[prompt, image]
        )

        if not response.text:
            raise RuntimeError("Gemini returned an empty response.")

        return response.text

    except Exception as error:
        raise RuntimeError(
            f"Gemini water analysis failed: {error}"
        ) from error