from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import List
from dotenv import load_dotenv

# .env 파일에서 API 키 로드
load_dotenv()


class Movie(BaseModel):
    title: str = Field(description="영화 제목")
    genre: str = Field(description="영화 장르")
    year: int = Field(description="개봉 연도")
    rating: float = Field(description="평점")
    summary: str = Field(description="한줄 요약")


class MovieList(BaseModel):
    movies: List[Movie] = Field(description="영화 리스트")


parser = PydanticOutputParser(pydantic_object=MovieList)

template = ChatPromptTemplate(
    [
        ("system", "당신은 영화 전문가 입니다. 모든 대답은 한국어로 해주세요."),
        ("user", "{question} \n {format_instructions}"),
    ]
)

llm = ChatOpenAI(model="gpt-4o-mini",temperature=0.1)
chain = template | llm | parser

result = chain.invoke(
    {
        "question": "2024년 기준 영화화 3가지를 추천해줘",
        "format_instructions": parser.get_format_instructions(),
    }
)

print(f"데이터 타입 확인 : {type(result)}")
print()
print(f"총 {len(result.movies)}편의 영화")
print()

for i, movie in enumerate(result.movies, 1):
    print(f"{i}. {movie.title} ({movie.year})")
    print(f"      장르: {movie.genre}")
    print(f"      평점: {movie.rating / 10}")
    print(f"      요약: {movie.summary}")
