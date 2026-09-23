import argparse
import asyncio
import csv
import json
from pathlib import Path

from dotenv import load_dotenv

from src.models import CopyRequest
from src.generator import CopyGenerator


def parse_args():
    parser = argparse.ArgumentParser(
        description="Automated Copywriting & Tone Transformer"
    )

    parser.add_argument("--product-name")
    parser.add_argument("--description")
    parser.add_argument(
        "--platform",
        choices=["LinkedIn", "Instagram", "Email"]
    )
    parser.add_argument(
        "--tone",
        default="professional"
    )
    parser.add_argument(
        "--temperature",
        type=float,
        default=0.5
    )
    parser.add_argument(
        "--top-p",
        type=float,
        default=0.9
    )

    parser.add_argument(
        "--csv",
        help="CSV file for bulk generation"
    )

    parser.add_argument(
        "--concurrency",
        type=int,
        default=5
    )

    parser.add_argument(
        "--output",
        default="output.json"
    )

    return parser.parse_args()


def build_request(row, args=None):
    return CopyRequest(
        product_name=row["product_name"],
        description=row["description"],
        platform=row["platform"],
        tone=row.get("tone", "professional"),
        temperature=float(
            row.get(
                "temperature",
                args.temperature if args else 0.5
            )
        ),
        top_p=float(
            row.get(
                "top_p",
                args.top_p if args else 0.9
            )
        ),
    )


async def main():

    # Load .env
    load_dotenv()

    args = parse_args()

    # Create AI generator
    generator = CopyGenerator(
        concurrency=args.concurrency
    )

    # -----------------------------
    # BULK CSV MODE
    # -----------------------------
    if args.csv:

        requests = []

        with open(
            args.csv,
            newline="",
            encoding="utf-8"
        ) as file:

            reader = csv.DictReader(file)

            for row in reader:
                requests.append(
                    build_request(row, args)
                )

        results = await generator.generate_bulk(
            requests
        )

        Path(args.output).write_text(
            json.dumps(
                results,
                indent=2,
                ensure_ascii=False
            ),
            encoding="utf-8"
        )

        print(
            f"Generated {len(results)} items -> {args.output}"
        )

        return

    # -----------------------------
    # SINGLE GENERATION MODE
    # -----------------------------

    if not all([
        args.product_name,
        args.description,
        args.platform
    ]):

        raise SystemExit(
            "Please provide --product-name, "
            "--description and --platform."
        )

    request = CopyRequest(
        product_name=args.product_name,
        description=args.description,
        platform=args.platform,
        tone=args.tone,
        temperature=args.temperature,
        top_p=args.top_p,
    )

    print("\nGenerating marketing copy...\n")

    result = await generator.generate(
        request
    )

    print("--------------------------------")
    print("GENERATED MARKETING COPY")
    print("--------------------------------")
    print(result["copy"])
    print("--------------------------------")


if __name__ == "__main__":
    asyncio.run(main())