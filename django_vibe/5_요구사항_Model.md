# ICT 교육 동영상 스트리밍 플랫폼 - Model 설계 요구사항

## 1. accounts 앱

### User (사용자)
| 필드명 | 타입 | 제약조건 | 설명 |
|--------|------|----------|------|
| email | EmailField | unique, 필수 | 로그인용 이메일 |
| password | CharField | 필수 | 암호화된 비밀번호 |
| username | CharField | unique, 필수 | 사용자 이름 |
| profile_image | ImageField | 선택 | 프로필 이미지 |
| bio | TextField | 선택 | 자기소개 |
| created_at | DateTimeField | auto_now_add | 가입일시 |
| updated_at | DateTimeField | auto_now | 수정일시 |
| is_active | BooleanField | default=True | 활성 상태 |
| is_instructor | BooleanField | default=False | 강사 여부 |

## 2. courses 앱

### Category (카테고리)
| 필드명 | 타입 | 제약조건 | 설명 |
|--------|------|----------|------|
| name | CharField | unique, 필수 | 카테고리명 |
| slug | SlugField | unique, 필수 | URL용 슬러그 |
| description | TextField | 선택 | 카테고리 설명 |
| created_at | DateTimeField | auto_now_add | 생성일시 |

### Course (강의)
| 필드명 | 타입 | 제약조건 | 설명 |
|--------|------|----------|------|
| title | CharField | 필수 | 강의 제목 |
| slug | SlugField | unique, 필수 | URL용 슬러그 |
| description | TextField | 필수 | 강의 상세 설명 |
| thumbnail | ImageField | 선택 | 강의 썸네일 이미지 |
| instructor | ForeignKey(User) | 필수 | 강사 (User 참조) |
| category | ForeignKey(Category) | 필수 | 카테고리 |
| price | DecimalField | 필수 | 가격 (0이면 무료) |
| level | CharField | 필수 | 난이도 (초급/중급/고급) |
| is_published | BooleanField | default=False | 공개 여부 |
| created_at | DateTimeField | auto_now_add | 생성일시 |
| updated_at | DateTimeField | auto_now | 수정일시 |

### Enrollment (수강 등록)
| 필드명 | 타입 | 제약조건 | 설명 |
|--------|------|----------|------|
| user | ForeignKey(User) | 필수 | 수강생 |
| course | ForeignKey(Course) | 필수 | 강의 |
| enrolled_at | DateTimeField | auto_now_add | 수강 신청일 |
| is_completed | BooleanField | default=False | 수강 완료 여부 |

**제약조건**: `unique_together = ['user', 'course']`

### Review (리뷰)
| 필드명 | 타입 | 제약조건 | 설명 |
|--------|------|----------|------|
| user | ForeignKey(User) | 필수 | 작성자 |
| course | ForeignKey(Course) | 필수 | 강의 |
| rating | IntegerField | 필수, 1-5 | 평점 |
| content | TextField | 필수 | 리뷰 내용 |
| created_at | DateTimeField | auto_now_add | 작성일시 |
| updated_at | DateTimeField | auto_now | 수정일시 |

**제약조건**: `unique_together = ['user', 'course']`

## 3. streaming 앱

### Lesson (레슨)
| 필드명 | 타입 | 제약조건 | 설명 |
|--------|------|----------|------|
| course | ForeignKey(Course) | 필수 | 소속 강의 |
| instructor | ForeignKey(User) | 필수 | 강사 |
| title | CharField | 필수 | 레슨 제목 |
| description | TextField | 선택 | 레슨 설명 |
| video_url | URLField | 필수 | 동영상 URL |
| duration | DurationField | 필수 | 영상 길이 |
| order | PositiveIntegerField | 필수 | 순서 |
| is_preview | BooleanField | default=False | 미리보기 허용 여부 |
| created_at | DateTimeField | auto_now_add | 생성일시 |

**제약조건**: `unique_together = ['course', 'order']`

### LessonProgress (학습 진도)
| 필드명 | 타입 | 제약조건 | 설명 |
|--------|------|----------|------|
| user | ForeignKey(User) | 필수 | 수강생 |
| lesson | ForeignKey(Lesson) | 필수 | 레슨 |
| watched_duration | DurationField | default=0 | 시청한 시간 |
| last_position | DurationField | default=0 | 마지막 재생 위치 |
| is_completed | BooleanField | default=False | 완료 여부 |
| updated_at | DateTimeField | auto_now | 마지막 시청일 |

**제약조건**: `unique_together = ['user', 'lesson']`

## 4. Model 관계도

```
User (accounts)
 |
 +--< Enrollment >-- Course --< Lesson
 |                      |          |
 +--< Review >---------+          |
 |                                 |
 +--< LessonProgress >------------+
                        |
                    Category
```

| 관계 | 타입 | 설명 |
|------|------|------|
| User - Course | M:N (through Enrollment) | 수강 관계 |
| User - Review | 1:N | 리뷰 작성 |
| User - LessonProgress | 1:N | 학습 진도 |
| Course - Category | N:1 | 카테고리 분류 |
| Course - User(instructor) | N:1 | 강사 |
| Course - Lesson | 1:N | 레슨 목록 |
| Lesson - LessonProgress | 1:N | 진도 기록 |
