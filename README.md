# 부산대학교 수강신청 매크로  

## 실행원리
#### 1. 수강신청 로그인 페이지 진입
#### 2. 스레드 4개 생성
각각 UTC+9 기준 07시 59분 58초, 59초, 59.5초, 8시 정각에 로그인 시도
#### 3. 로그인 되는 순서대로 수강신청 진행
담아둔 희망과목을 이용하여 수강신청  

## 준비사항
#### 1. 희망과목 담기
경쟁률이 높은 순서대로 신청해두는게 좋다.
#### 2. [Chrome 브라우저](https://www.google.com/intl/ko_kr/chrome/) 설치
이미 설치되어 있다면 생략한다.
#### 3. [Chrome Driver](https://chromedriver.chromium.org/downloads) 다운로드 
자신의 Chrome과 "동일한 버전"을 다운받고 "프로젝트 경로"에 넣는다.  
<br>
Chrome 버전 확인하는 법
   1. 컴퓨터에서 Chrome을 엽니다.
   2. 오른쪽 상단에서 더보기 ⋮ 클릭, 설정을 클릭합니다.
   3. 왼쪽 목록 하단의 Chrome 정보를 클릭하여 버전을 확인합니다.
#### 4. Selenium 라이브러리 설치
```
pip install selenium
```  

## 주의
1. 로그인 타이밍이 부정확하여 제대로 작동하지 않을 수 있습니다.
2. 해당 프로그램은 학습용으로 개발하였으며 실제로 사용하지 않습니다.
3. 해당 프로그램을 사용하여 발생하는 모든 책임은 사용자에게 있습니다.
4. 자유롭게 수정 및 배포가 가능합니다(MIT License).