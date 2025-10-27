from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model="gpt-5-mini")

# response = llm.invoke("랭체인이 뭐야?")

# print(response.content)

questions = [
    "Python의 특징을 알려줘",
    "Python과 Java의 속도를 비교해줘"
]

for q in questions:

    response = llm.invoke(q)
    print(f"Q: {q}")
    print(f"A: {response.content}")
    print()