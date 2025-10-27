from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from dotenv import load_dotenv

# .env 파일에서 API 키 로드
load_dotenv()

llm = ChatOpenAI(model="gpt-5-mini", temperature=0.7)

messages1 = [
    SystemMessage(
        content="당신은 친절하고 유능한 Python 선생님이에요. 초보자도 이해하기 쉽게 설명할 수 있습니다."
    ),
    HumanMessage(content="python에서의 async await 가 어떤 역할을 하나요?"),
]

response = llm.invoke(messages1)

print(response.content)
