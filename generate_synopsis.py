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
            text = re.sub('\s+', ' ', text)
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
    lines = open_file(filename).splitlines()
    return choice(lines)


def pick_variables():
    # pick random variables
    genre = pick_random('genres.txt')
    tone = pick_random('tones.txt')
    character = pick_random('characters.txt')
    pace = pick_random('paces.txt')
    storyline = pick_random('storylines.txt')
    style = pick_random('styles.txt')
    setting = pick_random('settings.txt')
    timeperiod = pick_random('times.txt')
    return genre, tone, character, pace, storyline, style, setting, timeperiod
    
    

def generate_synopsis(genre, tone, character, pace, storyline, style, setting, timeperiod):
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
    # generate and save synopsis
    synopsis = gpt3_completion(prompt).replace(':','').replace('SYNOPSIS','').replace('BEGINNING', '').replace('MIDDLE','').replace('ENDING','').replace('END','').replace('  ', ' ')
    return synopsis


def generate_many(number):
    for i in list(range(0,number)):
        genre, tone, character, pace, storyline, style, setting, timeperiod = pick_variables()
        synopsis = generate_synopsis(genre, tone, character, pace, storyline, style, setting, timeperiod)
        print('\n\nSYNOPSIS:', synopsis)
        unique_id = str(uuid4())
        #save_file('current_id.txt', unique_id)
        filename = 'synopses/%s.txt' % unique_id
        save_file(filename, synopsis)


def grade_synopsis(synopsis):
    prompt = open_file('prompt_grade.txt').replace('<<STORY>>', synopsis)
    grade = gpt3_completion(prompt, temp=0.0)
    return grade  # should be a string like '1' or '3' or whatever


def synopsis_gan():
    genre, tone, character, pace, storyline, style, setting, timeperiod = pick_variables()
    print('\n\nTERMS:', genre, setting, timeperiod, tone, character, pace, storyline, style)
    while True:
        synopsis = generate_synopsis(genre, tone, character, pace, storyline, style, setting, timeperiod)
        print('\n\nSYNOPSIS:', synopsis)
        grade = grade_synopsis(synopsis)
        print('\n\nGRADE:', grade)
        if grade == '5':
            unique_id = str(uuid4())
            filename = 'synopses/%s.txt' % unique_id
            save_file(filename, synopsis)
            exit(0)

if __name__ == '__main__':
    seed()
    synopsis_gan()