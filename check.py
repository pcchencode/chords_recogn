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
print(len(js['chroma_stft']))

# chords 跟 feature 長度不一樣...
