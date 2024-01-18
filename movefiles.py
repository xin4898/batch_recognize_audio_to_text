import shutil
import os

def move_files_to_txts(filename):
    shutil.move(f"./untrans/{filename}", f"./Recognized_Text/{filename}")

# for file in os.listdir("./untrans"):
#     if file.endswith(".wav"):
#         move_files_to_txts(file)