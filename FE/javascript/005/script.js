console.log("Hello World");

// DOM (Document Object Model)
// HTML 문서에서 화면에 보이는 요소를 조작하는 기능

// 1. 요소를 선택 -> 2. 요소를 수정/조작
const btnClick = document.getElementById("btn-click");
const title = document.querySelector("h1"); // css selector
console.log(btnClick);

btnClick.addEventListener("click", () => {
  // 2-1. 스타일 수정
  // css 스타일 속성 kebab-case -> camelCase
  console.log("클릭됨!");
  // btnClick.style.backgroundColor = "dodgerblue";

  // 2-2. 클래스 사용
  // add 추가, remove 삭제, toggle 껐다켰다, contains 포함되었는지
  btnClick.classList.toggle("clicked");
  // btnClick.classList.remove("tada");

  console.log(btnClick.classList.contains("clicked"));
  if (btnClick.classList.contains("clicked")) {
    // innerHTML: html 코드가 포함되어 있으면 해당 태그 파싱해서 화면에 출력
    btnClick.innerHTML = "클릭되었습니다 <strong>짜잔!</strong>";

    // textContent: 텍스트를 그대로 화면에 보여주는 역할
    btnClick.textContent = "클릭되었습니다 <strong>짜잔!</strong>";

    // 다른 요소 조작도 가능
    title.style.color = "red";
  } else {
    btnClick.innerHTML = "클릭해주세요";
    title.style.color = "black";
  }
});

//------- form 입력 --------
const $todoForm = document.getElementById("todo-form");
const $todoInput = document.getElementById("todo-input");
const $todoList = document.getElementById("todo-list");

$todoForm.addEventListener("submit", (e) => {
  e.preventDefault(); // 이벤트의 기본동작을 막음.

  console.log($todoInput.value); // input 요소의 입력값을 가져옴
  if ($todoInput.value.trim() === "") {
    alert("값을 입력하세요");
    return;
  }
  /* $todoList.innerHTML =
    $todoList.innerHTML + `<li>${$todoInput.value.trim()}</li>`;
    */
  const $todoItem = document.createElement("li");
  $todoItem.textContent = $todoInput.value.trim();
  $todoItem.classList.add("todo-item");
  $todoItem.addEventListener("click", () => {
    $todoItem.classList.toggle("completed");
  });
  $todoList.appendChild($todoItem);

  $todoInput.value = "";
});
