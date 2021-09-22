import os
import re
from bs4 import BeautifulSoup
from selenium import webdriver

os.system("clear")

print("\n\n* * * ♡◟(●•ᴗ•●)◞♡ 포뇨 E T L 다운로더 ♡◟(●•ᴗ•●)◞♡ * * *\n\n")
print("- - - - - - - - - W E L C O M E - - - - - - - - -\n\n")

print("[ 로그인 시 안내 사항 ]\n")
print("[0] 로그인 도중 키보드나 마우스를 조작하지 마세요.")
print("[1] 언니 말 안들으면 작동이 멈춥니다.")
print("[2] 이 경우, 프로그램을 껐다가 다시 켜주세요.")
print("[3] 로그인에 성공하면 이 창으로 다시 돌아와주세요!\n")
print("* 로그인하려면 ENTER 키를 눌러주세요\n")

while True:
    press = input()
    if press == "":
        break

print("♡ (*☌ᴗ☌)｡*ﾟ 로그인 중... ♡\n")

try:
    driver = webdriver.Chrome("driver/chromedriver")
    driver.get("https://etl.snu.ac.kr/login.php")

    elem_login = driver.find_element_by_id("input-username")
    # elem_login.clear()
    elem_login.send_keys("valikys")

    elem_login = driver.find_element_by_id("input-password")
    # elem_login.clear()
    elem_login.send_keys("sk199802200*")

    xpath = (
        """//*[@id="region-main"]/div/div/div/div[1]/div[1]/div[1]/form/div[2]/input"""
    )
    driver.find_element_by_xpath(xpath).click()
except Exception:
    driver.close
    press = input("<<< 로그인 실패!! 다시 시도해주세요...(Ｔ▽Ｔ) >>>")

print("♡ 로그인 성공!!! ٩(•̤̀ᵕ•̤́๑)૭✧ ♡\n\n")

driver.get(input("동영상 주소를 알려주세요: "))

try:
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    target = soup.find_all("script", {"type": "text/javascript"})[2]
    target = target.prettify()
    target_list = target.split("\n")
    find_string = "m3u8"
    m3u8 = ""
    for line in target_list:
        if find_string in line:
            m3u8 += line
    m3u8 = m3u8.split("'")[3]
    driver.close()
except Exception:
    print("<<< 파싱 중 오류 발생!! 처음부터 다시 시도해주세요...(Ｔ▽Ｔ) >>>")
    driver.close()

save_name = input("\n어떤 이름으로 저장할까요? (영어로/확장자제외): ")

print("\n\n- - - - - - L O A D I N G ... 무소식이 희소식 - - - - - -\n")

ffmpeg = "./ffmpeg"

try:
    os.system(
        f"{ffmpeg} -hide_banner -loglevel error -i {m3u8} -bsf:a aac_adtstoasc -c copy {save_name}.mp4"
    )
except Exception:
    print("<<< 변환 중 오류 발생!! 처음부터 다시 시도해주세요...(Ｔ▽Ｔ) >>>")

os.system("say 포뇨야포뇨야")
print("\n♡◟(●•ᴗ•●)◞♡ 다운로드 성공! ♡◟(●•ᴗ•●)◞♡\n\n")

print("[0] 폴더 열기\t [1] 바로 재생\n")

while True:
    press = input("번호를 입력해주세요: ")
    if press == "0":
        os.system("open .")
    elif press == "1":
        os.system(f"open {save_name}.mp4")
