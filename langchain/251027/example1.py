from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

# .env 파일에서 API 키 로드
load_dotenv()

llm = ChatOpenAI(model="gpt-5-mini")

# 1단계: 영어 -> 한국어

step1 = ChatPromptTemplate.from_messages(
    [
        ("system", "당신은 웹 프론트엔드 전문가이며, 코드를 이해하기 쉽게 설명해줄 수 있습니다."),
        ("user", "{english_text}"),
    ]
)

# 테스트 데이터
english_text = """
// API 사용
// (1)엔드포인트에 (2)요청을 보냄 (3)응답을 받아 (4)화면을 구성

// fetch(url, option);
// option을 생략하고 url만 가지고 요청 -> GET 요청

const API_URL = "https://dev.wenivops.co.kr/services/fastapi-crud";

const result = fetch(API_URL + "/1/blog");
console.log(result);
// Promise 객체 <pending, fulfilled, rejected>

result
  .then((response) => {
    console.log(result);
    console.log(response);

    const data = response.json(); // response.text(), response.formData();
    console.log("data", data);
    return data;
  })
  .then((data) => {
    console.log(data);
  })
  .catch((error) => {
    console.error(error);
  });

// async-await
async function getBlogPosts() {
  const response = await fetch(API_URL + "/1/blog");
  console.log("getBlogPosts: ", response);
  const data = await response.json();
  console.log("getBlogPosts: ", data);
  return data;
}
// getBlogPosts();

async function createBlogPost(title, content) {
  const response = await fetch(API_URL + "/1/blog", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      title: title,
      content: content,
    }),
  });
  const data = await response.json();
  console.log(data);
  await getBlogPosts();
}
// createBlogPost("테스트2", "테스트입니다.2");

async function updateBlogPost(id, title, content) {
  try {
    const response = await fetch(API_URL + "/1/blog/" + id, {
      method: "PUT",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        title, // title:title (키와 변수의 이름이 같으면 생략 가능)
        content, // content:content
      }),
    });
    console.log("update", response);
    if (!response.ok) {
      throw new Error(`HTTP 오류 발생 ${response.status}`);
    }
    const data = await response.json();
    console.log(data);
    await getBlogPosts();
  } catch (error) {
    console.error(error);
  }
}
// updateBlogPost(100, "변경했습니다!", "짜잔");

// fetch 데이터를 가져왔고 / DOM 화면에 뿌려줄 수 있음
const $blogList = document.getElementById("blog-list");
async function displayBlogPosts() {
  // 1. 데이터를 가져오고

  const posts = await getBlogPosts();
  console.log("데이터 가져오기!", posts);
  // 2. 데이터를 가공해서
  /*
  const post = posts[4];

  console.log("제목:", post.title);
  console.log("내용:", post.content);
  console.log("작가:", post.author);
  console.log("조회수:", post.views_count);
  console.log("날짜:", post.date);
  console.log("썸네일url:", post.thumbnail);
*/
  // 3. 화면에 보여주기
  posts.map((post) => {
    const $newItem = document.createElement("li");
    $newItem.classList.add("post-card");
    $newItem.innerHTML = `
    <img class="post-thumbnail" src="${API_URL}/${post.thumbnail}" alt="" />
    <h3 class='post-title'>${post.title}</h3>
    <p class='post-content'>${post.content}</p>
    <p class='post-author'>${post.author}</p>
    <div class='additional-cont'>
      <span class='view'>👀${post.views_count}</span>
      <span class='date'>${post.date}</span>
    </div>
  `;
    $blogList.appendChild($newItem);
  });
}
displayBlogPosts();

"""

step2 = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "당신은 요약전문가이며, 다음 한국어 텍스트를 한 문장으로 요약하세요. 그리고 요약문만 출력하세요.",
        ),
        ("user", "{korean_text}"),
    ]
)

step1_chain = step1 | llm

korean_result = step1_chain.invoke({"english_text": english_text})
korean_text = korean_result.content

print("1단계 번역")
print(korean_text)
print()

step2_chain = step2 | llm
summary_result = step2_chain.invoke({"korean_text":korean_text})

print("2단계 요약")
print(summary_result.content)
print()