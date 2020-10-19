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

for feat in dct.keys():
	print(f"the length of feature {feat} is {len(js[feat])}")
    
