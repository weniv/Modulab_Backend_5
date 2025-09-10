# MPA 블로그 구현하기 - 쉬운 설명서

## 🌟 MPA가 무엇인가요?

**MPA(Multi Page Application)**는 "여러 페이지로 구성된 웹사이트"라는 뜻입니다. 

### 📚 책으로 비유하면
- **MPA**: 여러 장으로 나뉜 책 (1장, 2장, 3장...)
- 각 장을 보려면 페이지를 넘겨야 함 (새로운 페이지 로딩)
- **SPA**: 모든 내용이 한 장에 있는 긴 두루마리 (페이지 전환 없이 스크롤)

### 🏠 우리가 만들 블로그의 구조
우리는 4개의 방(페이지)이 있는 집(웹사이트)을 만들 예정입니다:

1. **거실** (`blog_list.html`) - 모든 블로그 글 목록을 보는 곳
2. **서재** (`blog_detail.html`) - 하나의 글을 자세히 읽는 곳  
3. **작업실** (`blog_create.html`) - 새 글을 쓰는 곳
4. **편집실** (`blog_edit.html`) - 기존 글을 수정하는 곳

---

## 🔧 웹페이지는 어떻게 만들어지나요?

### HTML - 웹페이지의 뼈대
HTML은 웹페이지의 구조를 만드는 언어입니다. 집을 지을 때 기둥과 벽을 세우는 것과 같습니다.

```html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
</head>
<body>
    <h1>제목</h1>
    <p>내용</p>
</body>
</html>
```

**이 코드의 의미:**
- `<!DOCTYPE html>`: "이것은 HTML 문서입니다"라고 선언
- `<html lang="ko">`: 한국어로 된 웹페이지 시작
- `<head>`: 웹페이지의 설정 정보 (사용자에게는 보이지 않음)
- `<body>`: 실제로 사용자가 보는 내용
- `<h1>`: 큰 제목
- `<p>`: 일반 문단

### JavaScript - 웹페이지의 두뇌
JavaScript는 웹페이지가 사용자와 소통할 수 있게 해주는 언어입니다. 버튼을 클릭하거나 데이터를 가져오는 모든 동작을 담당합니다.

---

## 📋 1. 블로그 목록 페이지 (`blog_list.html`)

### 🎯 이 페이지의 역할
- 모든 블로그 글 제목과 정보를 한눈에 보여줌
- 각 글을 클릭하면 상세 페이지로 이동
- 새 글 쓰기 버튼 제공

### 📝 코드 분석

```html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
</head>
<body>
    <h1>MPA</h1>
    <header>blog list</header>
    <main></main>
    <a href="http://127.0.0.1:5500/blog_create.html">블로그 생성하기</a>
    <script>
        // JavaScript 코드가 여기에 들어갑니다
    </script>
</body>
</html>
```

**구조 설명:**
- `<h1>MPA</h1>`: 페이지 제목
- `<header>blog list</header>`: 페이지 상단 헤더
- `<main></main>`: 블로그 글 목록이 들어갈 빈 공간
- `<a href="...">블로그 생성하기</a>`: 새 글 쓰기 페이지로 가는 링크

### 🔄 JavaScript 동작 원리

```javascript
const main = document.querySelector('main');
fetch('http://127.0.0.1:8000/blogs')
    .then(response => response.json())
    .then(data => {
        data.forEach(element => {
            main.innerHTML += `
                <a href=http://127.0.0.1:5500/blog_detail.html?id=${element.id}>
                    <h2>${element.title}</h2>
                    <p>${element.created_at}</p>
                    <p>${element.updated_at}</p>
                    <p>${element.id}</p>
                    <p>${element.author}</p>
                    <p>${element.content}</p>
                </a>
            `;
        });
    });
```

**단계별 설명:**

1. **`const main = document.querySelector('main');`**
   - "main이라는 태그를 찾아서 main이라는 상자에 담아라"
   - 마치 "거실을 찾아서 거실이라고 이름표를 붙여라"와 같음

2. **`fetch('http://127.0.0.1:8000/blogs')`**
   - "서버에 있는 블로그 데이터를 가져와라"
   - 마치 "도서관에 가서 모든 책 목록을 가져와라"와 같음

3. **`.then(response => response.json())`**
   - "가져온 데이터를 읽을 수 있는 형태로 변환해라"
   - 마치 "외국어로 된 책을 한국어로 번역해라"와 같음

4. **`.then(data => { ... })`**
   - "번역된 데이터로 뭔가를 해라"

5. **`data.forEach(element => { ... })`**
   - "데이터에 있는 각각의 블로그 글에 대해 다음을 반복해라"
   - 마치 "책 목록의 각 책에 대해 다음을 해라"와 같음

6. **`main.innerHTML += '...'`**
   - "main 공간에 HTML 코드를 추가해라"
   - 마치 "거실에 가구를 하나씩 배치해라"와 같음

---

## 📖 2. 블로그 상세 페이지 (`blog_detail.html`)

### 🎯 이 페이지의 역할
- 하나의 블로그 글을 자세히 보여줌
- 수정하기, 삭제하기 버튼 제공
- 목록으로 돌아가기 링크 제공

### 🔍 URL에서 정보 가져오기

```javascript
const urlParams = new URLSearchParams(location.search);
const id = urlParams.get('id');
```

**설명:**
- URL이 `blog_detail.html?id=3`이라면
- `location.search`는 `?id=3` 부분을 가져옴
- `urlParams.get('id')`는 `3`이라는 값을 가져옴
- 마치 "편지 봉투에서 받는 사람 주소를 확인하는 것"과 같음

### 📥 특정 글 데이터 가져오기

```javascript
fetch(`http://127.0.0.1:8000/blogs/${id}`)
    .then(response => response.json())
    .then(data => {
        main.innerHTML += `
            <h2>${data.title}</h2>
            <p>${data.content}</p>
            // ... 기타 정보
        `;
    });
```

**설명:**
- `${id}` 부분에 실제 글 번호가 들어감 (예: 3번 글이면 `/blogs/3`)
- 서버에서 해당 글의 정보만 가져옴
- 가져온 정보를 화면에 표시

### 🔧 수정하기 기능

```javascript
const editButton = document.querySelector('.edit');
editButton.addEventListener('click', () => {
    location.href = `http://127.0.0.1:5500/blog_edit.html?id=${id}`;
});
```

**설명:**
- 수정 버튼을 찾아서 클릭 이벤트를 등록
- 버튼을 클릭하면 수정 페이지로 이동
- 현재 글의 ID를 함께 전달

### 🗑️ 삭제하기 기능

```javascript
const deleteButton = document.querySelector('.delete');
deleteButton.addEventListener('click', () => {
    fetch(`http://127.0.0.1:8000/blogs/${id}`, {
        method: 'DELETE'
    })
    .then(response => response.json())
    .then(data => {
        location.href = `http://127.0.0.1:5500/blog_list.html`;
    });
});
```

**설명:**
- 삭제 버튼을 찾아서 클릭 이벤트를 등록
- 버튼을 클릭하면 서버에 삭제 요청을 보냄
- 삭제가 완료되면 목록 페이지로 이동

---

## ✍️ 3. 블로그 생성 페이지 (`blog_create.html`)

### 🎯 이 페이지의 역할
- 새로운 블로그 글을 작성할 수 있는 양식 제공
- 글을 작성하면 서버에 저장
- 작성 완료 후 상세 페이지로 이동

### 📝 입력 양식 (Form)

```html
<form action="127.0.0.1:8000/blogs" method="post">
    <input type="text" name="title" placeholder="제목">
    <textarea name="content" placeholder="내용"></textarea>
    <button>게시물 작성</button>
</form>
```

**설명:**
- `<form>`: 사용자 입력을 받는 양식
- `<input>`: 한 줄 텍스트 입력란 (제목용)
- `<textarea>`: 여러 줄 텍스트 입력란 (내용용)
- `<button>`: 양식을 제출하는 버튼
- `placeholder`: 입력란에 회색으로 표시되는 안내 텍스트

### 📤 데이터 전송 과정

```javascript
form.addEventListener('submit', (event) => {
    event.preventDefault(); // 기본 동작 중단
    const title = event.target.title.value;
    const content = event.target.content.value;
    
    fetch('http://127.0.0.1:8000/blogs', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            title: title,
            content: content
        })
    })
    .then(response => response.json())
    .then(data => {
        location.href = `http://127.0.0.1:5500/blog_detail.html?id=${data.id}`
    });
});
```

**단계별 설명:**

1. **`event.preventDefault()`**
   - 양식의 기본 동작(페이지 새로고침)을 막음
   - 마치 "잠깐, 기다려! 내가 직접 처리할게"라고 말하는 것

2. **데이터 수집**
   - `title`: 제목 입력란의 값
   - `content`: 내용 입력란의 값

3. **서버에 전송**
   - `method: 'POST'`: "새로운 데이터를 생성하라"는 의미
   - `JSON.stringify()`: 데이터를 서버가 이해할 수 있는 형태로 변환

4. **완료 후 이동**
   - 서버에서 생성된 글의 ID를 받아서
   - 해당 글의 상세 페이지로 이동

---

## ✏️ 4. 블로그 수정 페이지 (`blog_edit.html`)

### 🎯 이 페이지의 역할
- 기존 블로그 글을 수정할 수 있는 양식 제공
- 기존 내용을 양식에 미리 채워줌
- 수정 완료 후 상세 페이지로 이동

### 🔄 기존 데이터 불러오기

```javascript
const urlParams = new URLSearchParams(location.search);
const id = urlParams.get('id');

fetch(`http://127.0.0.1:8000/blogs/${id}`)
    .then(response => response.json())
    .then(data => {
        form.title.value = data.title;
        form.content.value = data.content;
    });
```

**설명:**
- URL에서 수정할 글의 ID를 가져옴
- 해당 글의 기존 데이터를 서버에서 가져옴
- 양식의 입력란에 기존 데이터를 미리 채워줌
- 마치 "편집하려는 문서를 열어서 내용을 확인하는 것"과 같음

### 📤 수정된 데이터 전송

```javascript
fetch(`http://127.0.0.1:8000/blogs/${id}`, {
    method: 'PUT',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({
        title: title,
        content: content
    })
})
.then(response => response.json())
.then(data => {
    location.href = `http://127.0.0.1:5500/blog_detail.html?id=${data.id}`
});
```

**생성과의 차이점:**
- `method: 'PUT'`: "기존 데이터를 수정하라"는 의미 (POST는 새로 생성)
- URL에 수정할 글의 ID가 포함됨
- 나머지 과정은 생성과 동일

---

## 🔄 전체 흐름 정리

### 사용자 여정

1. **목록 페이지 방문** → 모든 글 확인
2. **글 클릭** → 상세 페이지로 이동
3. **상세 페이지에서:**
   - 글 읽기
   - 수정하기 클릭 → 수정 페이지로 이동
   - 삭제하기 클릭 → 글 삭제 후 목록으로 이동
4. **새 글 쓰기 클릭** → 생성 페이지로 이동
5. **글 작성 완료** → 상세 페이지로 이동

### 데이터 흐름

```
브라우저 ←→ 우리의 HTML 파일들 ←→ 서버 (백엔드 API)
```

- **브라우저**: 사용자가 보는 화면
- **HTML 파일들**: 우리가 만든 4개의 페이지
- **서버**: 블로그 데이터를 저장하고 관리하는 곳

---

## 🌐 주요 개념 정리

### HTTP 메서드
- **GET**: 데이터 가져오기 (조회)
- **POST**: 새 데이터 생성
- **PUT**: 기존 데이터 수정
- **DELETE**: 데이터 삭제

### URL 구조
- `blog_detail.html?id=3`
  - `blog_detail.html`: 페이지 파일명
  - `?`: 매개변수 시작 표시
  - `id=3`: ID가 3이라는 정보 전달

### JSON
- 서버와 브라우저가 데이터를 주고받을 때 사용하는 형식
- 마치 "공통 언어"와 같은 역할

---

## 💡 핵심 포인트

1. **MPA는 페이지별로 파일이 분리됨** - 각각 독립적인 HTML 파일
2. **JavaScript가 동적 기능을 담당** - 버튼 클릭, 데이터 가져오기 등
3. **서버와의 통신은 fetch를 통해** - 데이터 주고받기
4. **URL 매개변수로 정보 전달** - 페이지 간 데이터 공유
5. **사용자 경험은 페이지 이동으로 구성** - 클릭할 때마다 새 페이지 로딩

이제 HTML, CSS, JavaScript를 몰라도 MPA 블로그가 어떻게 동작하는지 이해하실 수 있을 것입니다! 🎉