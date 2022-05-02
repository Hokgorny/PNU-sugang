# 부산대학교 수강신청 툴
# 1. 수강신청 로그인 페이지 진입
# 2. 스레드 4개 생성, 각각 UTC 기준 07시 59분 58초, 59초, 59.5초, 59.75초에 로그인 시도
# 3. 로그인 되는 순서대로 수강신청 진행

import time, datetime, threading
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# 0. 기본 설정(학번 비밀번호 입력)
lst_time = [2, 1, 0.5, 0]

print("로그인 정보 입력... 정확히 입력해 주세요.")
id = input("학번 입력 : ")
pw = input("비밀번호 입력 : ")
print("입력 완료! 잠시후 로그인을 시도합니다.\n")

def get_driver():
    driver = getattr(threadLocal, "driver", None)
    if driver is None:
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        options.add_argument("headless")
        driver = webdriver.Chrome(".//chromedriver.exe", options=options)
    return driver

def sugang(ob_time):
    curr_status = False

    # 1. 수강신청 로그인 페이지 진입
    driver = get_driver()
    driver.get("https://sugang.pusan.ac.kr/sugang/Login.aspx")

    # 2. 정해진 시간에 로그인 엘리먼트 클릭
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='txtid']")))
    driver.find_element(By.XPATH, value="//*[@id='txtid']").send_keys(id)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='txtpassword']")))
    driver.find_element(By.XPATH, value="//*[@id='txtpassword']").send_keys(pw)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='btnlogin']")))

    curr_time = (datetime.datetime.utcnow() + datetime.timedelta(hours=9)).time()
    while float(curr_time.strftime("%H%M%S")) <= float(datetime.time(8, 59, 59, 999999).strftime("%H%M%S.%f")) - ob_time:
        curr_time = (datetime.datetime.utcnow() + datetime.timedelta(hours=9)).time()
    driver.find_element(By.XPATH, value="//*[@id='btnlogin']").click()
    print(f"Thread {threading.get_native_id()} : {curr_time} 로그인 성공")

    # 3. 수강신청 페이지 진입 후, 희망과목 수강신청 엘리먼트 클릭
    while curr_status == False:
        try:
            WebDriverWait(driver, 0.01).until(EC.presence_of_all_elements_located((By.XPATH, "//*[contains(@id,'_bt신청')]")))
        except TimeoutException:
            pass
        else:
            curr_status = True
        
    subjects = driver.find_elements(by=By.XPATH, value="//*[contains(@id,'_bt신청')]")
    for i in range (0, len(subjects)):
        subjects[i].click()
        WebDriverWait(driver, 90).until(EC.presence_of_all_elements_located((By.XPATH, "//*[contains(@id,'_bt신청')]")))
        subjects = driver.find_elements(by=By.XPATH, value="//*[contains(@id,'_bt신청')]")
        try: # 수강신청 당일 결과창이 늦게 뜨는 경우 대비 예외처리
            res = driver.find_element(by=By.XPATH, value="//*[@id='lbError']")
            print(f"{i+1}번째 과목 : {res.text}\n")
        except:
            print(f"{i+1}번째 과목 : 신청 성공!(서버렉으로 인해 자세한 정보가 표기되지 않음)\n")
    print("수강신청 완료! 프로그램을 닫아도 좋습니다.")

def time_display():
    curr_time = (datetime.datetime.utcnow() + datetime.timedelta(hours=9)).time()
    while float(curr_time.strftime("%H%M%S")) <= float(datetime.time(8, 59, 59, 999999).strftime("%H%M%S.%f")) - lst_time[1] - 0.5:
        curr_time = (datetime.datetime.utcnow() + datetime.timedelta(hours=9)).time()
        print(f"현재시간(UTC) : {curr_time}", end="\r")
        time.sleep(0.02)
    print("")

def main():
    threads = []
    for tm in lst_time:
        t = threading.Thread(target=sugang, args=(tm, ))
        threads.append(t)
        t.start()
    t_time = threading.Thread(target=time_display)
    t_time.start()

if __name__ == "__main__":
    threadLocal = threading.local()
    main()