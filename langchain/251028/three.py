from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import CommaSeparatedListOutputParser
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

# .env 파일에서 API 키 로드
load_dotenv()

parser = CommaSeparatedListOutputParser()

template = ChatPromptTemplate.from_messages(
    [
        ("system", "당신은 도움이 되는 AI입니다."),
        ("user", "{question} \n {format_instructions}"),
    ]
)

llm = ChatOpenAI(model="gpt-4o-mini")

chain = template | llm | parser

result = chain.invoke(
    {
        "question": "python의 특징을 알려줘",
        "format_instructions": parser.get_format_instructions(),
    }
)

print(f"데이터 타입: {type(result)}")

print("결과")

for i, reason in enumerate(result, 1):
    print(f"{i}. {reason}")
