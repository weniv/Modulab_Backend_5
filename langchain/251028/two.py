from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory
from dotenv import load_dotenv

# .env 파일에서 API 키 로드
load_dotenv()

# 세션 저장소
store = {}


def get_session_history(session_id: str):
    if session_id not in store:
        store[session_id] = ChatMessageHistory()
    return store[session_id]


llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7, streaming=True)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "당신은 코딩 초보자들도 이해하기 쉽게 코드를 설명할 수 있는 개발자입니다. 코드를 주면 분석해주세요."),
        MessagesPlaceholder(variable_name="history"),
        ("human", "{input}"),
    ]
)

chain = prompt | llm

with_message_history = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="history",
)

config = {"configurable": {"session_id": "user1"}}

print("=" * 50)
print("  Streaming + Memory 챗봇")
print("=" * 50)

while True:
    user_input = input("You: ")

    if user_input.strip().lower() in ["끝", "exit"]:
        break

    print()
    print("AI: ", end="", flush=True)

    for chunk in with_message_history.stream({"input": user_input}, config=config):
        print(chunk.content, end="", flush=True)

    print()
