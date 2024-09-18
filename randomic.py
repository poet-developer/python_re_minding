# puthon3 ./randomic.py 실행 명령어

import os
import random

# 현재 작업 디렉토리를 가져옵니다.
a = os.getcwd()

# 현재 작업 디렉토리를 출력합니다.
print(f"현재 작업 디렉토리: {a}")

# 작업 디렉토리 내 파일 및 폴더 목록을 가져옵니다.
b = os.listdir(a)

# 디렉토리 목록을 출력합니다.
print(f"{a} 디렉토리 내 파일 및 폴더 목록: {b}")

# 1부터 10까지의 랜덤 정수를 생성하여 파일 이름으로 사용
random_num = random.randint(1, 10)
file_name = f"{random_num}.txt"

# 파일을 쓰기 모드로 열어 파일을 생성합니다.
with open(file_name, "w") as file:
    # 파일에 내용을 작성합니다.
    file.write(f"이 파일은 랜덤 정수 {random_num}로 생성되었습니다.")

print(f"파일 '{file_name}'이(가) 생성되었습니다.")
