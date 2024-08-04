import random
from question import questions

def quiz():
    score = 0
    random.shuffle(questions['question'])
    for question in questions['question']:
        correct = play_again(question)
        if correct:
            score +=1
        else:
            print(f'Wrong answer! the correct answer is ',question['answer'])
        print()
    print(f'The score is : {score} out of {len(questions)}')

def play_again(question_data):

    print()


if __name__ == '__main__':
    quiz()