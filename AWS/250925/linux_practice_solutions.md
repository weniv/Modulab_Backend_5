# 리눅스 명령어 실습 해설집

## 📚 문제별 상세 해설

---

## 문제 1 해설: 기본 명령어 익히기

**명령어:**
```bash
pwd
cd ~
pwd
```

**해설:**
- `pwd`: 현재 작업 디렉토리의 전체 경로를 출력합니다.
- `cd ~`: 홈 디렉토리로 이동합니다. (`cd`만 입력해도 같은 효과)
- 두 번의 `pwd` 결과를 비교해보면 디렉토리가 변경된 것을 확인할 수 있습니다.

---

## 문제 2 해설: 디렉토리 만들기

**명령어:**
```bash
mkdir practice
```

**해설:**
- `mkdir`: 새로운 디렉토리를 생성하는 명령어입니다.
- `practice`라는 이름의 디렉토리가 현재 위치에 생성됩니다.
- `ls`로 생성된 디렉토리를 확인할 수 있습니다.

---

## 문제 3 해설: 파일 생성과 이동

**명령어:**
```bash
touch practice/hello.txt
cd practice
ls
```

**해설:**
- `touch practice/hello.txt`: `practice` 디렉토리 안에 빈 파일 `hello.txt`를 생성합니다.
- `cd practice`: `practice` 디렉토리로 이동합니다.
- `ls`: 현재 디렉토리의 파일과 디렉토리 목록을 출력합니다.

---

## 문제 4 해설: 파일 내용 추가

**명령어:**
```bash
echo "안녕하세요" > hello.txt
cat hello.txt
```

**해설:**
- `echo "안녕하세요" > hello.txt`: "안녕하세요"를 `hello.txt` 파일에 저장합니다.
- `>`: 리다이렉트 기호로, 명령어의 출력을 파일로 보냅니다.
- `cat hello.txt`: 파일의 내용을 화면에 출력합니다.

---

## 문제 5 해설: 파일 복사

**명령어:**
```bash
cp hello.txt greeting.txt
ls
```

**해설:**
- `cp hello.txt greeting.txt`: `hello.txt` 파일을 `greeting.txt`라는 이름으로 복사합니다.
- `cp` 명령어의 형식: `cp 원본파일 복사본파일`
- `ls`로 두 파일이 모두 있는지 확인합니다.

---

## 문제 6 해설: 와일드카드 사용

**명령어:**
```bash
touch test1.txt test2.txt data.log
ls *.txt
ls test*
```

**해설:**
- `touch test1.txt test2.txt data.log`: 한 번에 여러 파일을 생성합니다.
- `ls *.txt`: `*`는 임의의 문자열을 의미하므로 `.txt`로 끝나는 모든 파일을 보여줍니다.
- `ls test*`: `test`로 시작하는 모든 파일을 보여줍니다.
- `*` 와일드카드는 0개 이상의 임의의 문자와 매칭됩니다.

---

## 문제 7 해설: 파이프와 정렬

**명령어:**
```bash
echo -e "3\n1\n4\n2" > numbers.txt
cat numbers.txt | sort
```

**해설:**
- `echo -e "3\n1\n4\n2" > numbers.txt`: 숫자들을 각 줄에 하나씩 파일에 저장합니다.
- `cat numbers.txt | sort`: 파일 내용을 읽어서 정렬합니다.
- `|` (파이프): 앞 명령어의 출력을 뒤 명령어의 입력으로 전달합니다.
- `sort`: 입력받은 텍스트를 알파벳/숫자 순으로 정렬합니다.

---

## 문제 8 해설: 검색 명령어

**명령어:**
```bash
find . -name "*test*"
grep "안녕" greeting.txt
```

**해설:**
- `find . -name "*test*"`: 현재 디렉토리(`.`)에서 이름에 "test"가 포함된 파일을 찾습니다.
- `grep "안녕" greeting.txt`: `greeting.txt` 파일에서 "안녕"이라는 문자열이 포함된 줄을 찾습니다.
- `find`: 파일과 디렉토리를 검색하는 명령어
- `grep`: 텍스트에서 특정 패턴을 검색하는 명령어

---

## 문제 9 해설: 파일 이름 변경

**명령어:**
```bash
mv greeting.txt welcome.txt
```

**해설:**
- `mv greeting.txt welcome.txt`: `greeting.txt` 파일의 이름을 `welcome.txt`로 변경합니다.
- `mv` 명령어는 파일을 이동시키거나 이름을 변경할 때 사용합니다.
- 같은 디렉토리 내에서 사용하면 이름 변경, 다른 디렉토리로 사용하면 이동의 효과가 있습니다.

---

## 문제 10 해설: 정리하기

**명령어:**
```bash
rm *
cd ~
rmdir practice
```

또는

```bash
rm *.txt *.log
cd ~  
rmdir practice
```

**해설:**
- `rm *`: 현재 디렉토리의 모든 파일을 삭제합니다. (디렉토리는 삭제하지 않음)
- `cd ~`: 홈 디렉토리로 이동합니다.
- `rmdir practice`: 빈 디렉토리 `practice`를 삭제합니다.
- **주의**: `rm *`는 모든 파일을 삭제하므로 신중하게 사용해야 합니다.

---

## 💡 추가 학습 포인트

### 자주 사용하는 명령어 조합
- `ls | grep 문자열`: 파일 목록에서 특정 문자열 검색
- `cat 파일명 | sort`: 파일 내용 정렬하여 출력
- `find . -name "패턴"`: 현재 위치에서 파일 검색

### 안전한 파일 삭제
- 파일 삭제 전 `ls`로 항상 확인하기
- `rm` 사용시 삭제할 파일명을 정확히 입력하기
- 와일드카드 사용시 특히 주의하기

### 효율적인 작업 습관
- 명령어 입력 후 결과 확인하기
- `pwd`로 현재 위치 수시로 확인하기
- 실수했을 때 당황하지 말고 차근차근 해결하기
