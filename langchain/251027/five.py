from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

# .env 파일에서 API 키 로드
load_dotenv()

llm = ChatOpenAI(model="gpt-5-mini")