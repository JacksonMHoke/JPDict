import sys
import requests
import json

def search(term):
    url = f'https://jisho.org/api/v1/search/words?keyword={term}'
    r = requests.get(url)
    if (r.ok):
        return json.loads(r.text)
    else:
        return False

path="C:\\Users\\User\\Desktop\\word_frequency\\"
pathRead=path+'word_freq_report.txt'
pathWrite=path+'word_freq_report_with_definition.txt'

with open(pathRead,'r', encoding='utf8') as f:
    contents=f.read().split()
    words=contents[8:]
    words=words[::7]
    freqs=contents[7:]
    freqs=freqs[::7]
    word_freq=zip(freqs, words)
    with open(pathWrite, 'a+', encoding='utf8') as w:
        for (freq,word) in word_freq:
            if (int(freq)<=1):
                break

            data=search(word)
            if (not data):
                continue

            try:
                w.write(freq)
                w.write('\t')
                w.write(data['data'][0]['slug'])
                w.write('\t')
                w.write(data['data'][0]['japanese'][0]['reading'])
                w.write('\t')
                for defs in data['data'][0]['senses'][0]['english_definitions']:
                    w.write(defs)
                    w.write(', ')
                w.write('\n')
            except:
                print('An error occured, continuing')