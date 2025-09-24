let accessToken = sessionStorage.getItem("accessToken") || ""; // 메모리

// DOM 요소
const $username = document.getElementById("username");
const $password = document.getElementById("password");

const $loginBtn = document.getElementById("login-btn");
const $signupBtn = document.getElementById("signup-btn");
const $tokenBtn = document.getElementById("token-btn");

$loginBtn.addEventListener("click", async () => {
  // 로그인 요청
  const loginResult = await login($username.value, $password.value);
  console.log("로그인", loginResult);
  accessToken = loginResult.access_token;
  sessionStorage.setItem("accessToken", accessToken);
  console.log(accessToken);
});
$signupBtn.addEventListener("click", async () => {
  // 회원가입 요청
  const signupResult = await signup($username.value, $password.value);
  console.log("회원가입", signupResult);
});
$tokenBtn.addEventListener("click", async () => {
  // 토큰 검증 요청
  const tokenResult = await tokenCheck();
  console.log("토큰 검증", tokenResult);
});

const API_URL = "https://dev.wenivops.co.kr/services/fastapi-crud";
async function login(username, password) {
  const response = await fetch(API_URL + "/1/login", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      username,
      password,
    }),
  });
  const data = await response.json();
  console.log(data);
  return data;
}

async function signup(username, password) {
  const response = await fetch(API_URL + "/1/signup", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      username,
      password,
    }),
  });
  const data = await response.json();
  console.log(data);
  return data;
}

async function tokenCheck() {
  const response = await fetch(API_URL + "/login_confirm", {
    method: "POST",
    headers: {
      Authorization: `Bearer ${accessToken}`,
    },
  });
  const data = await response.json();
  console.log(data);
  return data;
}
