import os
import shutil

def tran_to_16khz(filename):
    audio_path = f"C:\\Users\\xin\\Desktop\\pydub\\untrans\\{filename}"
    target_path = f"C:\\Users\\xin\\Desktop\\pydub\\{filename}"
    cmd_str = f"ffmpeg -i {audio_path} -ac 1 -ar 16000 {target_path}"
    os.system(cmd_str)

# for file in os.listdir("./untrans"):
#     if file.endswith(".wav"):
#         tran_to_16khz(file)


