
from io import BytesIO

from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image, ImageOps, UnidentifiedImageError

from services.gemini_service import analyze_water_sample
from services.limits import limits, classify


app = FastAPI(
    title="Detox API",
    description="AI-assisted visual water assessment tool",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://localhost:3000"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

ALLOWED_TYPES = {"image/jpeg", "image/png"}
MAX_FILE_SIZE = 10 * 1024 * 1024
MAX_IMAGE_PIXELS = 20_000_000


@app.get("/")
async def home():
    return {
        "message": "Detox API is running",
        "status": "online"
    }


@app.post("/api/analyze")
async def analyze_water(file: UploadFile = File(...)):

    # Check file type
    if file.content_type not in ALLOWED_TYPES:
        raise HTTPException(
            status_code=400,
            detail="Please upload a JPG or PNG image."
        )

    # Read uploaded file
    contents = await file.read()

    if len(contents) > MAX_FILE_SIZE:
        raise HTTPException(
            status_code=413,
            detail="Image must be smaller than 10 MB."
        )

    # Validate and process image
    try:
        with Image.open(BytesIO(contents)) as original:
            if original.format not in {"JPEG", "PNG"}:
                raise HTTPException(
                    status_code=400,
                    detail="Only JPG and PNG images are supported."
                )

            if original.width * original.height > MAX_IMAGE_PIXELS:
                raise HTTPException(
                    status_code=400,
                    detail="Image resolution is too large."
                )

            original.verify()

        with Image.open(BytesIO(contents)) as original:
            image = ImageOps.exif_transpose(original)
            image.load()
            image = image.convert("RGB")

    except HTTPException:
        raise

    except (UnidentifiedImageError, OSError, ValueError):
        raise HTTPException(
            status_code=400,
            detail="Invalid or corrupted image."
        )

    # Send image to Gemini
    try:
        observation = analyze_water_sample(image)

    except Exception as error:
        print("GEMINI ERROR:", repr(error), flush=True)

        raise HTTPException(
            status_code=502,
            detail="AI image analysis failed. Check backend terminal."
        )

    # Return structured analysis
    return {
        "status": "success",
        "filename": file.filename,
        "image_dimensions": {
            "width": image.width,
            "height": image.height
        },
        "analysis": observation,
        "available_reference_limits": limits,
        "disclaimer": (
            "Photographic analysis cannot establish actual water "
            "quality or drinking-water safety. Reference limits "
            "apply only to appropriate measured values."
        )
    }
