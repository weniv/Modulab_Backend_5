from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory
from dotenv import load_dotenv

# .env 파일에서 API 키 로드
load_dotenv()

# 세션별 대화 기록 저장소
store = {}
"""
store = {
    "user_1": ChatMessageHistory([메시지1, 메시지2, ...]),
    "user_2": ChatMessageHistory([메시지1, 메시지2, ...]),
    "user_3": ChatMessageHistory([메시지1, 메시지2, ...]),
}
"""


def get_session_history(session_id: str):
    if session_id not in store:
        store[session_id] = ChatMessageHistory()
    return store[session_id]


llm = ChatOpenAI(model="gpt-5-mini", temperature=0.7)


prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "당신은 친절한 AI 어시스턴트입니다."),  # AI의 역할을 정의의
        MessagesPlaceholder(variable_name="history"),  # 이전 대화 기록이 들어갈 자리
        ("human", "{input}"),  # 사용자 입력
    ]
)

chain = prompt | llm

with_message_history = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="history",
)


# 세션 설정
config = {"configurable": {"session_id": "user1"}}

# 대화 1
print("=== 대화 1 ===")
print("사용자: 내 이름은 김철수야")
response1 = with_message_history.invoke(
    {"input": "내 이름은 김철수야"},
    config=config
)
print(f"AI: {response1.content}")
print()

# 대화 2
print("=== 대화 2 ===")
print("사용자: 나는 Python을 공부하고 있어")
response2 = with_message_history.invoke(
    {"input": "나는 Python을 공부하고 있어"},
    config=config
)
print(f"AI: {response2.content}")
print()

# 대화 3 (기억 테스트!)
print("=== 대화 3 (기억 테스트) ===")
print("사용자: 내 이름이 뭐였지?")
response3 = with_message_history.invoke(
    {"input": "내 이름이 뭐였지?"},
    config=config
)
print(f"AI: {response3.content}")
print()

# 대화 4
print("=== 대화 4 (기억 테스트) ===")
print("사용자: 내가 뭘 공부한다고 했지?")
response4 = with_message_history.invoke(
    {"input": "내가 뭘 공부한다고 했지?"},
    config=config
)
print(f"AI: {response4.content}")


'''
# 첫 번째 대화
invoke({"input": "내 이름은 김철수야"})
↓
프롬프트 생성:
- system: "당신은 친절한 AI 어시스턴트입니다."
- history: []  ← 비어있음
- human: "내 이름은 김철수야"
↓
AI 응답 후 자동으로 저장:
store["user1"] = [
    HumanMessage("내 이름은 김철수야"),
    AIMessage("안녕하세요 김철수님! 반갑습니다.")
]

# 두 번째 대화
invoke({"input": "내 이름이 뭐였지?"})
↓
프롬프트 생성:
- system: "당신은 친절한 AI 어시스턴트입니다."
- history: [
    HumanMessage("내 이름은 김철수야"),
    AIMessage("안녕하세요 김철수님! 반갑습니다.")
  ]  ← 이전 대화 자동 포함!
- human: "내 이름이 뭐였지?"
↓
AI가 이전 대화를 보고 답변: "김철수님이십니다!"

'''