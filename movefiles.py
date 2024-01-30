import shutil
import os

def move_files_to_txts(filename):
    shutil.move(f"./untrans/{filename}", f"./Recognized_Text/{filename}")

def delete_files(filename):
    os.remove(f"./{filename}")
