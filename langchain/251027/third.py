from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv

# .env 파일에서 API 키 로드
load_dotenv()

question = "하늘이 파란 이유를 창의적으로 설명해줘"

# Temperature 비교
temperatures = [0, 0.7, 1.5]

for temp in temperatures:
    print(f"=== Temperature: {temp} ===")

    llm = ChatOpenAI(model="gpt-5-mini", temperature=temp)

    # 2번 반복 실행
    for i in range(2):
        response = llm.invoke(question)
        print(f"시도 {i+1}: {response.content[:100]}...")
    print()
