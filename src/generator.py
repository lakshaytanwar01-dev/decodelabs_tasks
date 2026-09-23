import asyncio
import os
from typing import Iterable

from google import genai
from tenacity import (
    retry,
    stop_after_attempt,
    wait_exponential,
    retry_if_exception_type,
)

from src.models import CopyRequest, CopyResponse
from src.prompt_compiler import compile_prompt


class CopyGenerator:

    def __init__(self, concurrency: int = 5):

        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise RuntimeError(
                "GEMINI_API_KEY is missing. Put it in your .env file."
            )

        self.client = genai.Client(api_key=api_key)

        self.model = os.getenv(
            "GEMINI_MODEL",
            "gemini-3.6-flash"
        )

        self.semaphore = asyncio.Semaphore(
            max(1, concurrency)
        )

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(
            multiplier=1,
            min=1,
            max=8
        ),
        retry=retry_if_exception_type(Exception),
        reraise=True,
    )
    async def _request(self, request: CopyRequest):

        prompt = compile_prompt(request)

        response = await self.client.aio.models.generate_content(
            model=self.model,
            contents=prompt,
            config={
                "temperature": request.temperature,
                "top_p": request.top_p,
            },
        )

        return response.text.strip()

    async def generate(self, request: CopyRequest):

        async with self.semaphore:

            copy = await self._request(request)

        result = CopyResponse(
            product_name=request.product_name,
            platform=request.platform,
            tone=request.tone,
            copy=copy,
        )

        return result.model_dump()

    async def generate_bulk(
        self,
        requests: Iterable[CopyRequest]
    ):

        async def worker(request):

            try:
                return await self.generate(request)

            except Exception as exc:

                return {
                    "product_name": request.product_name,
                    "platform": request.platform,
                    "tone": request.tone,
                    "error": str(exc),
                }

        return await asyncio.gather(
            *(worker(request) for request in requests)
        )
    