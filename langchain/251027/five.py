from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

# .env 파일에서 API 키 로드
load_dotenv()

llm = ChatOpenAI(model="gpt-5-mini")

# 1단계: 영어 -> 한국어

step1 = ChatPromptTemplate.from_messages(
    [
        ("system", "당신은 번역전문가이며, 영어를 한국어로 정확하게 번역하세요."),
        ("user", "{english_text}"),
    ]
)

# 테스트 데이터
english_text = """
LangChain is a framework for developing applications powered by language models.
It enables applications that are context-aware and can reason about how to answer
based on provided context.
"""

step2 = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "당신은 요약전문가이며, 다음 한국어 텍스트를 한 문장으로 요약하세요. 그리고 요약문만 출력하세요.",
        ),
        ("user", "{korean_text}"),
    ]
)

step1_chain = step1 | llm

korean_result = step1_chain.invoke({"english_text": english_text})
korean_text = korean_result.content

print("1단계 번역")
print(korean_text)
print()

step2_chain = step2 | llm
summary_result = step2_chain.invoke({"korean_text":korean_text})

print("2단계 요약")
print(summary_result.content)
print()