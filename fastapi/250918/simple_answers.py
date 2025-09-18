import sqlite3

print("=== SQLite3 심플 CRUD 정답 ===")

# 1단계: 테이블 만들기
print("\n1단계: 테이블 만들기")
conn = sqlite3.connect('school.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER,
        grade TEXT
    )
''')
print("테이블 생성 완료!")

# 2단계: 학생 추가하기 (CREATE)
print("\n2단계: 학생 추가하기")
cursor.execute("INSERT INTO students (id, name, age, grade) VALUES (1, '김철수', 20, '3학년')")
cursor.execute("INSERT INTO students (id, name, age, grade) VALUES (2, '이영희', 19, '2학년')")
cursor.execute("INSERT INTO students (id, name, age, grade) VALUES (3, '박민수', 21, '4학년')")
conn.commit()
print("학생 추가 완료!")

# 3단계: 학생 조회하기 (READ)
print("\n3단계: 학생 조회하기")
cursor.execute("SELECT * FROM students")
students = cursor.fetchall()

print("=== 전체 학생 ===")
for student in students:
    print(student)

cursor.execute("SELECT * FROM students WHERE age >= 20")
older_students = cursor.fetchall()

print("\n=== 20살 이상 학생 ===")
for student in older_students:
    print(f"이름: {student[1]}, 나이: {student[2]}")

# 4단계: 정보 수정하기 (UPDATE)
print("\n4단계: 정보 수정하기")
cursor.execute("UPDATE students SET age = 22 WHERE name = '김철수'")
conn.commit()

cursor.execute("SELECT * FROM students WHERE name = '김철수'")
result = cursor.fetchone()
print(f"수정된 김철수 정보: {result}")

# 5단계: 학생 삭제하기 (DELETE)
print("\n5단계: 학생 삭제하기")
cursor.execute("DELETE FROM students WHERE name = '박민수'")
conn.commit()

cursor.execute("SELECT * FROM students")
remaining = cursor.fetchall()
print("남은 학생들:")
for student in remaining:
    print(student)

conn.close()

print("\n" + "="*50)

# 과제 1: 책 관리 정답
print("\n과제 1: 책 관리 정답")
conn = sqlite3.connect('bookstore.db')
cursor = conn.cursor()

# 1. books 테이블 만들기
cursor.execute('''
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY,
        title TEXT,
        author TEXT,
        price INTEGER
    )
''')
print("1. books 테이블 생성 완료")

# 2. 책 3권 추가하기
cursor.execute("INSERT INTO books (id, title, author, price) VALUES (1, '파이썬 기초', '김개발', 15000)")
cursor.execute("INSERT INTO books (id, title, author, price) VALUES (2, '웹 프로그래밍', '이코딩', 25000)")
cursor.execute("INSERT INTO books (id, title, author, price) VALUES (3, '데이터베이스', '박디비', 20000)")
conn.commit()
print("2. 책 3권 추가 완료")

# 3. 모든 책 조회하기
cursor.execute("SELECT * FROM books")
all_books = cursor.fetchall()
print("3. 전체 책 목록:")
for book in all_books:
    print(f"   {book}")

# 4. 가격이 20000원 이상인 책만 조회
cursor.execute("SELECT * FROM books WHERE price >= 20000")
expensive_books = cursor.fetchall()
print("4. 20000원 이상 책:")
for book in expensive_books:
    print(f"   {book[1]} - {book[3]}원")

# 5. 첫 번째 책의 가격을 25000원으로 수정
cursor.execute("UPDATE books SET price = 25000 WHERE id = 1")
conn.commit()
cursor.execute("SELECT * FROM books WHERE id = 1")
updated_book = cursor.fetchone()
print(f"5. 수정된 첫 번째 책: {updated_book}")

# 6. 마지막 책 삭제
cursor.execute("DELETE FROM books WHERE id = 3")
conn.commit()
cursor.execute("SELECT * FROM books")
final_books = cursor.fetchall()
print("6. 삭제 후 남은 책들:")
for book in final_books:
    print(f"   {book}")

conn.close()

print("\n" + "="*50)

# 과제 2: 카페 메뉴 정답
print("\n과제 2: 카페 메뉴 정답")
conn = sqlite3.connect('cafe.db')
cursor = conn.cursor()

# 1. menu 테이블 만들기
cursor.execute('''
    CREATE TABLE IF NOT EXISTS menu (
        id INTEGER PRIMARY KEY,
        name TEXT,
        price INTEGER,
        category TEXT
    )
''')
print("1. menu 테이블 생성 완료")

# 2. 음료 4개 추가하기
cursor.execute("INSERT INTO menu (id, name, price, category) VALUES (1, '아메리카노', 4000, '커피')")
cursor.execute("INSERT INTO menu (id, name, price, category) VALUES (2, '카페라떼', 4500, '커피')")
cursor.execute("INSERT INTO menu (id, name, price, category) VALUES (3, '자몽에이드', 5000, '음료')")
cursor.execute("INSERT INTO menu (id, name, price, category) VALUES (4, '치즈케이크', 6000, '디저트')")
conn.commit()
print("2. 메뉴 4개 추가 완료")

# 3. 커피 카테고리만 조회하기
cursor.execute("SELECT * FROM menu WHERE category = '커피'")
coffee_menu = cursor.fetchall()
print("3. 커피 메뉴:")
for item in coffee_menu:
    print(f"   {item[1]} - {item[2]}원")

# 4. 가격이 5000원 미만인 메뉴 조회
cursor.execute("SELECT * FROM menu WHERE price < 5000")
cheap_menu = cursor.fetchall()
print("4. 5000원 미만 메뉴:")
for item in cheap_menu:
    print(f"   {item[1]} - {item[2]}원")

# 5. 아메리카노 가격을 4200원으로 인상
cursor.execute("UPDATE menu SET price = 4200 WHERE name = '아메리카노'")
conn.commit()
cursor.execute("SELECT * FROM menu WHERE name = '아메리카노'")
updated_americano = cursor.fetchone()
print(f"5. 인상된 아메리카노: {updated_americano[1]} - {updated_americano[2]}원")

# 6. 가장 비싼 메뉴 삭제
cursor.execute("SELECT MAX(price) FROM menu")
max_price = cursor.fetchone()[0]
cursor.execute("DELETE FROM menu WHERE price = ?", (max_price,))
conn.commit()

cursor.execute("SELECT * FROM menu")
final_menu = cursor.fetchall()
print("6. 가장 비싼 메뉴 삭제 후:")
for item in final_menu:
    print(f"   {item[1]} - {item[2]}원")

conn.close()
print("\n모든 과제 완료!")
