import random
from question import questions

def quiz():
    score = 0
    random.shuffle(questions)
    for question in questions:
        correct = game(question)
        if correct:
            score +=1
        else:
            print(f'Wrong answer! the correct answer is ',question['answer'])
        print()
    print(f'The score is : {score} out of {len(questions)}')

def game(question_data):

    print(question_data['question'])

    for option in question_data['option']:
        print(option)
    answer = input("Enter the option? ").strip().upper()

    if answer in ['A','B','C','D']:
        if answer == question_data['answer']:
            return True
    else:
        print("Enter the correct options")


if __name__ == '__main__':
    quiz()