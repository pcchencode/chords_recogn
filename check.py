import sys, os
import json


with open('/Users/user/Desktop/chords_recogn/CE200_sample/CE200_sample/14/ground_truth.txt', 'r') as f:
    chords = []
    for line in f:
        chords.append(line.split())
print(chords)
print(len(chords))


with open('/Users/user/Desktop/chords_recogn/CE200_sample/CE200_sample/14/feature.json', 'r') as f:
    d = f.read()
    js = json.loads(d)
print(len(js['poly_features'][0]))

# chords 跟 feature 長度不一樣...



dct = dict(js)
print(dct.keys()) # 印出所有特徵數,共12個

i = 0
for feat in dct.keys():
    print(f"the length of feature {feat} is {len(js[feat])}")
    i = i + len(js[feat])


# chroma 代表的是 12 個半音:C,C#,D..., B在每隔bin中的能量大小
print(js['chroma_stft'][0]) # 長度共10186~=整首歌長236.50175s / (hop_length512/sr22050)
print(len(js['chroma_stft'][0]))
#print(len(js['chroma_cqt'][0]))
