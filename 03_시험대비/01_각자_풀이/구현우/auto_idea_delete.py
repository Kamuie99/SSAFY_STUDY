# 자동으로 .idea 폴더 삭제 해주는 코드

import os
import subprocess

current_folder = os.getcwd()

for foldername, subfolders, filenames in os.walk(current_folder):
    if '.idea' in subfolders:
        idea_folder_path = os.path.join(foldername, '.idea')
        subprocess.run(['rm', '-rf', idea_folder_path])
        print(f'{idea_folder_path} 폴더가 삭제되었습니다.')