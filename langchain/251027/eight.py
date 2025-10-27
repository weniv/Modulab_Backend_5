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
llm = ChatOpenAI(model="gpt-5-mini", temperature=0.7)

# 프롬프트 템플릿
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "당신은 친절하고 유용한 AI 어시스턴트입니다. 사용자의 질문에 친근하게 답변하세요.",
        ),
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

print("=" * 50)
print("  AI 챗봇 시작!")
print("  종료하려면 '끝', '종료', 'exit' 입력")
print("=" * 50)
print()

while True:
    user_input = input("You: ")

    # 종료 조건
    if user_input.strip().lower() in ["끝", "종료", "exit", "quit"]:
        print()
        print("챗봇을 종료합니다.")
        break

    # 빈 입력이라면?
    if not user_input.strip():
        continue

    # AI 응답
    try:
        response = with_message_history.invoke({"input": user_input}, config=config)
        print(f"AI: {response.content}")
        print()
    except Exception as e:
        print(f"오류 발생: {str(e)}")
        print()


# 종료 시 대화 기록 표시
print()
print("=" * 50)
print("전체 대화 기록:")
print("=" * 50)

history = get_session_history("user1")
for i, msg in enumerate(history.messages):
    role = "You" if msg.type == "human" else "AI"
    print(f"{role}: {msg.content}")
    print()
