from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from langchain_openai import ChatOpenAI
import asyncio
from dotenv import load_dotenv
import os

# .env 파일에서 API 키 로드
load_dotenv()

app = FastAPI()


@app.get("/stream")
async def stream_chat(message: str):  # http://localhost:8000/stream?message=안녕하세요

    async def generate():
        llm = ChatOpenAI(model="gpt-4o-mini", streaming=True, temperature=0.7)

        # 출력
        for chunk in llm.stream(message):
            if chunk.content:
                # SSE (Server-Sent Events 방식)
                yield f"{chunk.content}"
                await asyncio.sleep(0.01)

    return StreamingResponse(generate(), media_type="text/event-stream")
