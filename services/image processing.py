
from io import BytesIO

from PIL import Image, ImageOps, UnidentifiedImageError


# Image upload configuration
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10 MB
MAX_IMAGE_PIXELS = 20_000_000

ALLOWED_FORMATS = {"JPEG", "PNG"}


class ImageProcessingError(Exception):
    """Raised when an uploaded image is invalid."""
    pass


def process_image(file_bytes: bytes) -> Image.Image:
    """
    Validate and prepare an uploaded water sample image.

    Args:
        file_bytes: Raw uploaded image bytes.

    Returns:
        A processed RGB PIL image.

    Raises:
        ImageProcessingError: If the image is invalid or unsupported.
    """

    # 1. Check whether the file is empty
    if not file_bytes:
        raise ImageProcessingError("No image was uploaded.")

    # 2. Check file size
    if len(file_bytes) > MAX_FILE_SIZE:
        raise ImageProcessingError(
            "Image size exceeds the 10 MB limit."
        )

    try:
        # 3. Open and verify the image
        with Image.open(BytesIO(file_bytes)) as image:

            # Check actual image format
            if image.format not in ALLOWED_FORMATS:
                raise ImageProcessingError(
                    "Only JPG and PNG images are supported."
                )

            # Check image dimensions
            width, height = image.size

            if width <= 0 or height <= 0:
                raise ImageProcessingError(
                    "Invalid image dimensions."
                )

            if width * height > MAX_IMAGE_PIXELS:
                raise ImageProcessingError(
                    "Image resolution is too large."
                )

            image.verify()

        # 4. Reopen image after verification
        with Image.open(BytesIO(file_bytes)) as image:

            # Correct orientation using EXIF metadata
            image = ImageOps.exif_transpose(image)

            # Convert image to RGB
            image = image.convert("RGB")

            # Return an independent image object
            return image.copy()

    except ImageProcessingError:
        raise

    except (
        UnidentifiedImageError,
        OSError,
        ValueError
    ) as error:
        raise ImageProcessingError(
            f"Unable to process image: {error}"
        ) from error
