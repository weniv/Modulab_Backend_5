from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import time

# .env 파일에서 API 키 로드
load_dotenv()

llm = ChatOpenAI(model="gpt-5-mini", temperature=0.7)

question = "Python의 역사를 3문단으로 자세히 설명해주세요."

# print("===스트리밍X===")

# start_time = time.time()
# response = llm.invoke(question)
# end_time = time.time()

# print(response.content)

# print(f"Non 스트리밍 소요 시간: {end_time - start_time:.2f}초")

# print("===스트리밍O===")

# start_time = time.time()

# for chunk in llm.stream(question):
#     print(chunk.content, end="",flush=True)
#     time.sleep(0.02)

# end_time = time.time()

# print(f"스트리밍 소요 시간: {end_time - start_time:.2f}초")

for chunk in llm.stream(question):
    print(type(chunk))
    print(chunk.content)

full_response_text = ""

for chunk in llm.stream(question):
    full_response_text += chunk.content
    print(chunk.content, end="", flush=True)

print(f"전체답변 {full_response_text}")
