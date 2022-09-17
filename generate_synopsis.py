import re
import os
import openai
from time import time,sleep
from random import seed,choice
from uuid import uuid4


def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()


def save_file(filepath, content):
    with open(filepath, 'w', encoding='utf-8') as outfile:
        outfile.write(content)


openai.api_key = open_file('openaiapikey.txt')


def gpt3_completion(prompt, engine='text-davinci-002', temp=1.1, top_p=1.0, tokens=1000, freq_pen=0.0, pres_pen=0.0, stop=['asdfasdf', 'asdasdf']):
    max_retry = 5
    retry = 0
    prompt = prompt.encode(encoding='ASCII',errors='ignore').decode()  # force it to fix any unicode errors
    while True:
        try:
            response = openai.Completion.create(
                engine=engine,
                prompt=prompt,
                temperature=temp,
                max_tokens=tokens,
                top_p=top_p,
                frequency_penalty=freq_pen,
                presence_penalty=pres_pen,
                stop=stop)
            text = response['choices'][0]['text'].strip()
            #text = re.sub('\s+', ' ', text)
            filename = '%s_gpt3.txt' % time()
            save_file('gpt3_logs/%s' % filename, prompt + '\n\n==========\n\n' + text)
            return text
        except Exception as oops:
            retry += 1
            if retry >= max_retry:
                return "GPT3 error: %s" % oops
            print('Error communicating with OpenAI:', oops)
            sleep(1)


def pick_random(filename):
    seed()
    lines = open_file(filename).splitlines()
    return choice(lines)


if __name__ == '__main__':
    # pick random variables
    genre = pick_random('genres.txt')
    tone = pick_random('tones.txt')
    character = pick_random('characters.txt')
    pace = pick_random('paces.txt')
    storyline = pick_random('storylines.txt')
    style = pick_random('styles.txt')
    setting = pick_random('settings.txt')
    timeperiod = pick_random('times.txt')
    # instantiate prompt
    prompt = open_file('prompt_synopsis.txt')
    prompt = prompt.replace('<<GENRE>>', genre)
    prompt = prompt.replace('<<TONE>>', tone)
    prompt = prompt.replace('<<CHARACTER>>', character)
    prompt = prompt.replace('<<PACE>>', pace)
    prompt = prompt.replace('<<STORYLINE>>', storyline)
    prompt = prompt.replace('<<STYLE>>', style)
    prompt = prompt.replace('<<SETTING>>', setting)
    prompt = prompt.replace('<<TIME>>', timeperiod)
    prompt = prompt.replace('<<UUID>>', str(uuid4()))
    print('\n\nPROMPT:', prompt)
    # generate and save synopsis
    synopsis = 'APPEAL TERMS: %s, %s, %s, %s, %s, %s, %s, %s\n\nBEGINNING: ' % (genre, setting, timeperiod, character, pace, style, tone, storyline)
    synopsis = synopsis + gpt3_completion(prompt).replace('SYNOPSIS:','').replace('  ', ' ')
    filename = 'synopses/%s.txt' % str(uuid4())
    save_file(filename, synopsis)
    print('\n\nSYNOPSIS:', synopsis)