# SQL 연습 문제집 해설

## 문제 1 해설

### 문제 분석
- IT 부서 직원만 필터링: `WHERE department = 'IT'`
- 이름과 급여만 조회: `SELECT name, salary`
- 급여 높은 순 정렬: `ORDER BY salary DESC`

### 정답
```sql
SELECT name, salary
FROM employees
WHERE department = 'IT'
ORDER BY salary DESC;
```

### 실행 결과
| name | salary |
|------|--------|
| 박민수 | 6800000 |
| 김철수 | 5500000 |
| 정현우 | 5200000 |

### 핵심 포인트
- `WHERE` 절로 조건 필터링
- `ORDER BY` 절에서 `DESC`는 내림차순(높은 순), `ASC`는 오름차순(낮은 순)
- 여러 컬럼을 조회할 때는 쉼표(,)로 구분

---

## 문제 2 해설

### 문제 분석
- 급여 범위 조건: `salary BETWEEN 4500000 AND 6000000`
- 부서 조건: `department IN ('IT', 'Marketing')`
- 두 조건을 AND로 연결
- 정렬: `ORDER BY department, name`

### 정답
```sql
SELECT *
FROM employees
WHERE salary BETWEEN 4500000 AND 6000000
  AND department IN ('IT', 'Marketing')
ORDER BY department, name;
```

### 실행 결과
| emp_id | name | department | salary | hire_date | position |
|--------|------|------------|--------|-----------|----------|
| 1 | 김철수 | IT | 5500000 | 2020-03-15 | 개발자 |
| 5 | 정현우 | IT | 5200000 | 2020-09-03 | 개발자 |
| 4 | 최지영 | Marketing | 4800000 | 2021-01-12 | 마케터 |

### 핵심 포인트
- `BETWEEN A AND B`: A 이상 B 이하 범위 조건
- `IN (값1, 값2, ...)`: 여러 값 중 하나와 일치하는 조건
- `AND` 연산자로 여러 조건 결합
- `ORDER BY`에서 여러 컬럼 지정 시 첫 번째 기준으로 먼저 정렬, 같으면 두 번째 기준으로 정렬

---

## 문제 3 해설

### 문제 분석
- 이름에 '영' 포함: `WHERE name LIKE '%영%'`
- 급여를 만원 단위로: `salary / 10000 AS salary_만원`
- 입사년도 추출: `YEAR(hire_date) AS hire_year` (MySQL 기준)
- 입사년도순 정렬: `ORDER BY hire_year`

### 정답
```sql
SELECT name, 
       department, 
       salary / 10000 AS salary_만원, 
       YEAR(hire_date) AS hire_year
FROM employees
WHERE name LIKE '%영%'
ORDER BY hire_year;
```

### 실행 결과
| name | department | salary_만원 | hire_year |
|------|------------|-------------|-----------|
| 윤서현 | HR | 620 | 2016 |
| 이영희 | HR | 420 | 2019 |
| 최지영 | Marketing | 480 | 2021 |

### 핵심 포인트
- `LIKE '%문자%'`: 문자가 포함된 모든 레코드 찾기
  - `%영%`: '영'이 어디든 포함된 경우
  - `영%`: '영'으로 시작하는 경우
  - `%영`: '영'으로 끝나는 경우
- `AS`: 컬럼에 별칭(alias) 부여
- `YEAR()`: 날짜에서 연도 추출하는 함수
- 계산식도 별칭 사용 가능

---

## 주요 SQL 문법 정리

### SELECT 문 기본 구조
```sql
SELECT 컬럼명 [AS 별칭]
FROM 테이블명
WHERE 조건
ORDER BY 컬럼명 [ASC|DESC];
```

### WHERE 절 조건 연산자
- `=`, `!=`, `<>`: 같음, 다름
- `>`, `>=`, `<`, `<=`: 크기 비교
- `BETWEEN A AND B`: A 이상 B 이하
- `IN (값1, 값2, ...)`: 여러 값 중 일치
- `LIKE '패턴'`: 패턴 매칭
- `AND`, `OR`, `NOT`: 논리 연산자

### ORDER BY 절
- `ASC`: 오름차순 (기본값)
- `DESC`: 내림차순
- 여러 컬럼 정렬: `ORDER BY 컬럼1, 컬럼2`

### 연습 팁
1. 조건을 하나씩 추가하면서 결과 확인
2. 별칭은 의미있는 이름으로 설정
3. 정렬 조건을 명확히 이해하고 사용
4. LIKE 패턴 매칭에서 %(와일드카드) 위치 주의

---

**수고하셨습니다! 🎉**
각 문제를 통해 SQL의 기본 문법을 익히셨기를 바랍니다.
