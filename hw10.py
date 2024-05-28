import os
import pickle

filename = 'score.bin'

def input_scores():
    scores = []
    print('[점수 입력]')
    i = 1
    while True:
        score = int(input(f'#{i}? '))
        if score < 0:
            break
        scores.append(score)
        i += 1
    return scores

def show_scores(scores):
    print('\n[점수 출력]')
    print('개인점수: ', end='')
    for score in scores:
        print(score, end=' ')
    print()

def get_average(scores):
    total = sum(scores)
    return total / len(scores)

def save_data(scores, filepath):
    with open(filepath, 'wb') as file:
        pickle.dump(scores, file)

def load_data(filepath):
    with open(filepath, 'rb') as file:
        return pickle.load(file)

if os.path.exists(filename):
    print('[파일 읽기]')
    scores = load_data(filename)
    show_scores(scores)
    print(f'평균: {get_average(scores):.1f}')
else:
    scores = input_scores()
    show_scores(scores)
    save_data(scores, filename)    
    print(f'평균: {get_average(scores):.1f}')
