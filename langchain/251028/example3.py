from fastapi import FastAPI
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory
from typing import Dict
from dotenv import load_dotenv

# .env 파일에서 API 키 로드
load_dotenv()

app = FastAPI()

sessions = {}


def get_session_history(session_id: str):
    if session_id not in sessions:
        sessions[session_id] = ChatMessageHistory()
    return sessions[session_id]


llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)

prompt = ChatPromptTemplate(
    [
        ("system", "당신은 친절하고 세심한 AI 어시스턴트입니다."),
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


class ChatRequest(BaseModel):
    session_id: str
    message: str


@app.post("/chat/session")
def chat_with_memory(req: ChatRequest):

    config = {"configurable": {"session_id": req.session_id}}

    response = with_message_history.invoke({"input": req.message}, config=config)

    history = get_session_history(req.session_id)

    return {
        "session_id": req.session_id,
        "response": response.content,
        "history_length": len(history.messages),
    }


@app.get("/chat/history/{session_id}")
def get_history(session_id: str):

    if session_id not in sessions:
        return {"error": "세션을 찾을 수 없습니다."}

    history = get_session_history(session_id)
    messages = []

    for msg in history.messages:
        messages.append({"role": msg.type, "content": msg.content})

    return {"session_id": session_id, "messages": messages, "count": len(messages)}


@app.delete("/chat/session/{session_id}")
def clear_session(session_id: str):

    if session_id in sessions:
        del sessions[session_id]
        return {"message": "세션이 삭제되었습니다."}
    return {"error": "세션은 찾을 수 없습니다."}
