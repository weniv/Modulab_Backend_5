from fastapi import FastAPI
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os

# .env 파일에서 API 키 로드
load_dotenv()

app = FastAPI(title="번역 API 서비스")


class TranslateRequest(BaseModel):
    text: str
    target_lang: str = "영어"


class TranslateResponse(BaseModel):
    original: str
    translated: str
    target_lang: str


@app.post("/translate", response_model=TranslateResponse)
def translate(req: TranslateRequest):

    template = ChatPromptTemplate(
        [
            ("system", "당신은 전문 번역가입니다. 번역문만 출력하세요."),
            ("user", "다음을 {target_lang}으로 번역하세요: {text}"),
        ]
    )

    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.3)
    chain = template | llm

    result = chain.invoke({"target_lang": req.target_lang, "text": req.text})

    return TranslateResponse(
        original=req.text,
        translated=result.content,
        target_lang=req.target_lang
    )

# 다중 번역 API
class MultiTranslateRequest(BaseModel):
    text: str
    target_langs: list[str]

@app.post("/translate/multi")
def translate_multi(req: MultiTranslateRequest):
    """여러 언어로 한 번에 번역"""
    template = ChatPromptTemplate.from_messages([
        ("system", "번역문만 출력하세요."),
        ("user", "{target_lang}로 번역: {text}")
    ])

    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.3)
    chain = template | llm

    results = {}
    for lang in req.target_langs:
        result = chain.invoke({"text": req.text, "target_lang": lang})
        results[lang] = result.content

    return {
        "original": req.text,
        "translations": results
    }
