import os
import azure.cognitiveservices.speech as speechsdk
import time
import transTo16khz
import movefiles

def recognize_from_file(filename):
    # This example requires environment variables named "SPEECH_KEY" and "SPEECH_REGION"
    speech_config = speechsdk.SpeechConfig(subscription=os.environ.get('SPEECH_KEY'), region=os.environ.get('SPEECH_REGION'))
    speech_config.speech_recognition_language="zh-TW"
    audio_config = speechsdk.audio.AudioConfig(filename=filename)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

    done = False
    def stop_cb(evt):
        speech_recognizer.stop_continuous_recognition()
        nonlocal done
        done = True

    # # 初始化一個列表
    results = []

    speech_recognizer.recognized.connect(lambda evt: results.append('辨識結果: {}'.format(evt.result.text).rstrip()))

    speech_recognizer.session_stopped.connect(stop_cb)
    speech_recognizer.canceled.connect(stop_cb)
    speech_recognizer.start_continuous_recognition()
    while not done:
        time.sleep(.5)   
    print(results)
    txtname = filename.split(".")[0]
    f = os.path.join("C:\\Users\\xin\\Desktop\\pydub\\Recognized_Text", f"{txtname}.txt")
    with open(f, "w") as file:
        for text in results:
            file.write(f"{text}\n")
        file.close

for file in os.listdir("./untrans"):
    if file.endswith(".wav"):
        transTo16khz.tran_to_16khz(file)

for filename in os.listdir("./"):
    if filename.endswith(".wav"):
        recognize_from_file(filename)

for file in os.listdir("./untrans"):
    if file.endswith(".wav"):
        movefiles.move_files_to_txts(file)



# recognize_from_file("2_161307.wav")