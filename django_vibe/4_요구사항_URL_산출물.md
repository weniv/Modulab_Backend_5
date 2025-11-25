# ICT 교육 동영상 스트리밍 플랫폼 - Django URL 구조 설계 산출물

## 1. Django 앱 구조

```
project/
├── config/              # 프로젝트 설정
│   ├── urls.py          # 루트 URL 설정
│   └── settings.py
├── accounts/            # 사용자 인증 앱
│   └── urls.py
├── courses/             # 강의 관련 앱
│   └── urls.py
├── dashboard/           # 사용자 대시보드 앱
│   └── urls.py
└── streaming/           # 동영상 스트리밍 앱
    └── urls.py
```

## 2. URL 구조 설계

### 2.1 루트 URL 설정 (config/urls.py)

| URL 패턴 | Include | 설명 |
|----------|---------|------|
| `/` | - | 메인 홈페이지 |
| `/accounts/` | `accounts.urls` | 사용자 인증 관련 |
| `/courses/` | `courses.urls` | 강의 관련 |
| `/dashboard/` | `dashboard.urls` | 사용자 대시보드 |
| `/streaming/` | `streaming.urls` | 동영상 스트리밍 |

### 2.2 사용자 인증 URL (accounts/urls.py)

| URL 패턴 | View Name | HTTP Method | 설명 |
|----------|-----------|-------------|------|
| `/accounts/signup/` | `signup` | GET, POST | 회원가입 페이지 |
| `/accounts/login/` | `login` | GET, POST | 로그인 페이지 |
| `/accounts/logout/` | `logout` | POST | 로그아웃 처리 |


### 2.3 강의 관련 URL (courses/urls.py)

| URL 패턴 | View Name | HTTP Method | 설명 |
|----------|-----------|-------------|------|
| `/courses/` | `course_list` | GET | 강의 목록 조회 (페이지네이션) |
| `/courses/search/` | `course_search` | GET | 강의 검색 (키워드, 카테고리) |
| `/courses/<int:course_id>/` | `course_detail` | GET | 강의 상세 보기 |
| `/courses/<int:course_id>/enroll/` | `course_enroll` | POST | 강의 수강 신청 |
| `/courses/<int:course_id>/reviews/` | `course_reviews` | GET | 강의 리뷰 목록 |
| `/courses/<int:course_id>/reviews/create/` | `review_create` | POST | 리뷰 작성 |
| `/courses/category/<slug:category_slug>/` | `course_by_category` | GET | 카테고리별 강의 목록 |

### 2.4 사용자 대시보드 URL (dashboard/urls.py)

| URL 패턴 | View Name | HTTP Method | 설명 |
|----------|-----------|-------------|------|
| `/dashboard/` | `dashboard_home` | GET | 대시보드 메인 |
| `/dashboard/my-courses/` | `my_courses` | GET | 내 수강 강의 목록 |
| `/dashboard/profile/` | `profile` | GET | 프로필 보기 |
| `/dashboard/profile/edit/` | `profile_edit` | GET, POST | 프로필 수정 |

### 2.5 동영상 스트리밍 URL (streaming/urls.py)

| URL 패턴 | View Name | HTTP Method | 설명 |
|----------|-----------|-------------|------|
| `/streaming/<int:course_id>/lessons/` | `lesson_list` | GET | 강의 커리큘럼(레슨 목록) |
| `/streaming/<int:course_id>/lessons/<int:lesson_id>/` | `lesson_detail` | GET | 레슨 상세 (영상 재생 페이지) |
| `/streaming/<int:course_id>/lessons/<int:lesson_id>/progress/` | `update_progress` | POST | 학습 진도 업데이트 |
| `/streaming/<int:course_id>/progress/` | `course_progress` | GET | 강의 전체 진도 조회 |


## 3. 전체 URL 맵 요약

```
/                                           # 메인 홈페이지
│
├── /accounts/
│   ├── signup/                             # 회원가입
│   ├── login/                              # 로그인
│   └── logout/                             # 로그아웃
│
├── /courses/
│   ├── /                                   # 강의 목록
│   ├── search/                             # 강의 검색
│   ├── category/<category_slug>/           # 카테고리별 강의
│   └── <course_id>/
│       ├── /                               # 강의 상세
│       ├── enroll/                         # 수강 신청
│       └── reviews/
│           ├── /                           # 리뷰 목록
│           └── create/                     # 리뷰 작성
│
├── /dashboard/
│   ├── /                                   # 대시보드 메인
│   ├── my-courses/                         # 내 강의 목록
│   └── profile/
│       ├── /                               # 프로필 보기
│       └── edit/                           # 프로필 수정
│
└── /streaming/
    └── <course_id>/
        ├── lessons/                        # 레슨 목록
        │   └── <lesson_id>/
        │       ├── /                       # 레슨 상세 (영상 재생)
        │       └── progress/               # 진도 업데이트
        └── progress/                       # 강의 진도 조회
```