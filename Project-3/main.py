import argparse
import os
import time
from pathlib import Path

from dotenv import load_dotenv
from huggingface_hub import InferenceClient
from huggingface_hub.utils import HfHubHTTPError
from PIL import Image


load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")
MODEL = os.getenv(
    "HF_IMAGE_MODEL",
    "black-forest-labs/FLUX.1-schnell"
)

if not HF_TOKEN:
    raise RuntimeError(
        "HF_TOKEN not found. Add your Hugging Face token to .env"
    )

client = InferenceClient(
    provider="auto",
    api_key=HF_TOKEN
)


def validate_prompt(prompt: str) -> str:
    prompt = prompt.strip()

    if not prompt:
        raise ValueError("Prompt cannot be empty.")

    if len(prompt) > 2000:
        raise ValueError("Prompt is too long. Maximum length is 2000 characters.")

    return prompt


def generate_single_image(
    prompt: str,
    output_dir: str,
    index: int,
    width: int,
    height: int,
    retries: int = 3
) -> Path:

    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    filename = f"generated_image_{index}.png"
    image_file = output_path / filename

    for attempt in range(1, retries + 1):
        try:
            print(
                f"Generating image {index} "
                f"(attempt {attempt}/{retries})..."
            )

            image = client.text_to_image(
                prompt=prompt,
                model=MODEL,
                width=width,
                height=height
            )

            image.save(image_file)

            # Verify generated image
            with Image.open(image_file) as verified_image:
                verified_image.verify()

            print(f"✓ Saved: {image_file}")

            return image_file

        except HfHubHTTPError as error:
            print(f"API error: {error}")

        except OSError as error:
            print(f"Image/file error: {error}")

        except Exception as error:
            print(f"Unexpected error: {error}")

        if attempt < retries:
            wait_time = 2 ** (attempt - 1)
            print(f"Retrying in {wait_time} seconds...")
            time.sleep(wait_time)

    raise RuntimeError(
        f"Failed to generate image {index} after {retries} attempts."
    )


def main():
    parser = argparse.ArgumentParser(
        description="Multimodal Image Generation Studio"
    )

    parser.add_argument(
        "--prompt",
        required=True,
        help="Natural-language image generation prompt"
    )

    parser.add_argument(
        "--width",
        type=int,
        default=1024,
        help="Image width in pixels"
    )

    parser.add_argument(
        "--height",
        type=int,
        default=1024,
        help="Image height in pixels"
    )

    parser.add_argument(
        "--count",
        type=int,
        default=1,
        help="Number of images to generate"
    )

    parser.add_argument(
        "--output",
        default="outputs",
        help="Directory for generated images"
    )

    args = parser.parse_args()

    # Input validation
    prompt = validate_prompt(args.prompt)

    if args.width < 256 or args.height < 256:
        raise ValueError(
            "Width and height must be at least 256 pixels."
        )

    if args.width > 2048 or args.height > 2048:
        raise ValueError(
            "Width and height cannot exceed 2048 pixels."
        )

    if args.count < 1 or args.count > 4:
        raise ValueError(
            "Count must be between 1 and 4."
        )

    print("\n=== Multimodal Image Generation Studio ===")
    print(f"Model: {MODEL}")
    print(f"Resolution: {args.width}x{args.height}")
    print(f"Images: {args.count}")
    print()

    generated_files = []

    for index in range(1, args.count + 1):
        file_path = generate_single_image(
            prompt=prompt,
            output_dir=args.output,
            index=index,
            width=args.width,
            height=args.height
        )

        generated_files.append(file_path)

    print("\n=== Generation Complete ===")

    for file_path in generated_files:
        print(f"✓ {file_path}")


if __name__ == "__main__":
    main()