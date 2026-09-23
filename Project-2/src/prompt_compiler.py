from src.models import CopyRequest


MASTER_TEMPLATE = """
You are an expert marketing copywriter.

Create marketing copy for the product below.

Product Name: {product_name}
Raw Description: {description}
Target Platform: {platform}
Desired Tone: {tone}

Platform rules:
- LinkedIn: professional, useful, concise, business-friendly.
- Instagram: engaging, punchy, social-media friendly, optional short CTA.
- Email: clear subject line plus concise body and CTA.

Requirements:
1. Preserve factual claims from the description.
2. Do not invent prices, statistics, certifications, reviews or guarantees.
3. Match the requested tone.
4. Respect the target platform's communication style.
5. Return only the final marketing copy.
""".strip()


def compile_prompt(request: CopyRequest) -> str:
    return MASTER_TEMPLATE.format(
        product_name=request.product_name,
        description=request.description,
        platform=request.platform,
        tone=request.tone,
    )