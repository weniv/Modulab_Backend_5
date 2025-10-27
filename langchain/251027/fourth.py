from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

# .env 파일에서 API 키 로드
load_dotenv()

llm = ChatOpenAI(model="gpt-5-mini")

template = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "당신은 {subject} 전문가 입니다. 초보자도 이해할 수 있게 예시를 들어 설명해주세요.",
        ),
        ("user", "{question}"),
    ]
)

chain = template | llm

response = chain.invoke({"subject": "백엔드 개발", "question": "Restful API가 뭔가요?"})

print("백엔드 전문가의 답변")
print(response.content)