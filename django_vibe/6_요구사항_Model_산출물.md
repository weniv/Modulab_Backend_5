# ICT 교육 동영상 스트리밍 플랫폼 - Model 설계 산출물

## 1. ERD (Entity Relationship Diagram)

```mermaid
erDiagram
    User ||--o{ Enrollment : "수강"
    User ||--o{ Review : "작성"
    User ||--o{ LessonProgress : "학습"
    User ||--o{ Course : "강의(강사)"
    User ||--o{ Lesson : "강의(강사)"

    Category ||--o{ Course : "분류"

    Course ||--o{ Enrollment : "수강생"
    Course ||--o{ Review : "리뷰"
    Course ||--o{ Lesson : "커리큘럼"

    Lesson ||--o{ LessonProgress : "진도"

    User {
        int id PK
        string email UK "로그인용 이메일"
        string password "암호화된 비밀번호"
        string username UK "사용자 이름"
        string profile_image "프로필 이미지"
        text bio "자기소개"
        datetime created_at "가입일시"
        datetime updated_at "수정일시"
        boolean is_active "활성 상태"
        boolean is_instructor "강사 여부"
    }

    Category {
        int id PK
        string name UK "카테고리명"
        string slug UK "URL용 슬러그"
        text description "카테고리 설명"
        datetime created_at "생성일시"
    }

    Course {
        int id PK
        string title "강의 제목"
        string slug UK "URL용 슬러그"
        text description "강의 상세 설명"
        string thumbnail "썸네일 이미지"
        int instructor_id FK "강사"
        int category_id FK "카테고리"
        decimal price "가격"
        string level "난이도"
        boolean is_published "공개 여부"
        datetime created_at "생성일시"
        datetime updated_at "수정일시"
    }

    Enrollment {
        int id PK
        int user_id FK "수강생"
        int course_id FK "강의"
        datetime enrolled_at "수강 신청일"
        boolean is_completed "수강 완료 여부"
    }

    Review {
        int id PK
        int user_id FK "작성자"
        int course_id FK "강의"
        int rating "평점 1-5"
        text content "리뷰 내용"
        datetime created_at "작성일시"
        datetime updated_at "수정일시"
    }

    Lesson {
        int id PK
        int course_id FK "소속 강의"
        int instructor_id FK "강사"
        string title "레슨 제목"
        text description "레슨 설명"
        string video_url "동영상 URL"
        duration duration "영상 길이"
        int order "순서"
        boolean is_preview "미리보기 허용"
        datetime created_at "생성일시"
    }

    LessonProgress {
        int id PK
        int user_id FK "수강생"
        int lesson_id FK "레슨"
        duration watched_duration "시청한 시간"
        duration last_position "마지막 재생 위치"
        boolean is_completed "완료 여부"
        datetime updated_at "마지막 시청일"
    }
```

## 2. 제약조건 요약

| Model | 제약조건 | 설명 |
|-------|----------|------|
| Enrollment | `unique_together = ['user', 'course']` | 중복 수강 방지 |
| Review | `unique_together = ['user', 'course']` | 강의당 1개 리뷰 |
| Lesson | `unique_together = ['course', 'order']` | 강의 내 순서 중복 방지 |
| LessonProgress | `unique_together = ['user', 'lesson']` | 사용자별 레슨 진도 1개 |
