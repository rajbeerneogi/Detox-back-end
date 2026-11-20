import os

from dotenv import load_dotenv
from huggingface_hub import InferenceClient

# Load environment variables
load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")
HF_MODEL = os.getenv("HF_MODEL")

if not HF_TOKEN:
    raise RuntimeError("HF_TOKEN is missing from .env")

if not HF_MODEL:
    raise RuntimeError("HF_MODEL is missing from .env")


# Initialize Hugging Face client
client = InferenceClient(
    provider="auto",
    api_key=HF_TOKEN
)


def analyze_water_image(image):
    """
    Analyze a water sample image using a Hugging Face
    vision-language model.

    Returns a textual description of visible features.
    """

    prompt = """
    Analyze this water sample photograph.

    Describe:
    1. Visible water color.
    2. Visual clarity.
    3. Visible particles or sediment.
    4. Possible algae-like visual appearance.

    Do not invent pH, TDS, turbidity measurements,
    heavy metal concentrations, or bacteria results.

    Do not determine whether the water is safe to drink.

    Describe only what can reasonably be observed.
    """

    try:
        response = client.chat_completion(
            model=HF_MODEL,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": prompt
                        },
                        {
                            "type": "image",
                            "image": image
                        }
                    ]
                }
            ],
            max_tokens=300
        )

        return response.choices[0].message.content

    except Exception as error:
        raise RuntimeError(
            f"Hugging Face analysis failed: {error}"
        ) from error
