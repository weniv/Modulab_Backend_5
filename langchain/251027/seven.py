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


# LLM 설정
llm = ChatOpenAI(model="gpt-5-mini")

# 프롬프트 템플릿 (대화 히스토리 포함)
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "당신은 친절한 AI 어시스턴트입니다."),
        MessagesPlaceholder(variable_name="history"),
        ("human", "{input}"),
    ]
)

# 체인 구성
chain = prompt | llm

# 메모리가 포함된 체인
with_message_history = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="history",
)

# 설정
config = {"configurable": {"session_id": "user1"}}


# 여러 대화 진행
with_message_history.invoke({"input": "안녕! 내 이름은 홍길동이야"}, config=config)
with_message_history.invoke({"input": "나는 FastAPI를 배우고 있어"}, config=config)
with_message_history.invoke({"input": "오늘 날씨가 좋네"}, config=config)

print("=== 대화 히스토리 확인 ===")
history = get_session_history("user1")
print(f"총 메세지수: {len(history.messages)}")
print(f"메세지", history.messages)
print()

for i, msg in enumerate(history.messages):
    role = "Human" if msg.type == "human" else "AI"
    print(f"[{i+1}] {role}: {msg.content}")
    print()
