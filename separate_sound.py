import librosa
from pydub import AudioSegment
from pydub.silence import split_on_silence
 
# 音声ファイルを読み込む
file_path = '分割したいファイルのパス'
audio, sr = librosa.load(file_path, sr=None)
 
# 音声ファイルの長さを取得
duration = librosa.get_duration(y=audio, sr=sr)
 
# pydub用にAudioSegmentオブジェクトに変換
audio_segment = AudioSegment.from_wav(file_path)
 
# 音声ファイルを発話単位に分割
chunks = split_on_silence(
    audio_segment,
    min_silence_len=250,  # 無音の最小長さ（ミリ秒）
    silence_thresh=-20    # 無音と判断する音量閾値（dBFS）
)
 
# 分割した発話を個別のファイルに保存
for i, chunk in enumerate(chunks):
    # 分割したファイルのパスとindexの指定、又formatの指定 ex: C:\sepalate_sound\sepalated_sound_{i}.wav とwavなど
    chunk.export(f"分割したファイルのパスとindexの指定", format="formatの指定")
    

print('finished')
