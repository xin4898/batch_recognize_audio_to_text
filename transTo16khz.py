import os
import shutil

def tran_to_16khz(filename):
    audio_path = f"the audio_path to 16khz wav\\{filename}"
    target_path = f"path of batch_recognize_audio_to_text\\{filename}"
    cmd_str = f"ffmpeg -i {audio_path} -ac 1 -ar 16000 {target_path}"
    os.system(cmd_str)



