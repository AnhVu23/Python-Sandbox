"""
Dictionary
* Question prompts playground
📚 Resources:
https://www.youtube.com/watch?v=rfscVS0vtbw&t=1s&ab_channel=freeCodeCamp.org
"""
from question import Question
question_prompts = ['What color are apple?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n',
                    'What color are bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n',
                    'What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n']

questions = [
    Question(question_prompts[0], 'a'),
    Question(question_prompts[1], 'c'),
    Question(question_prompts[2], 'b'),
]


# Define a run test function
def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.question)
        if answer != question.answer:
            print('Incorrect')
        else:
            score += 1
    print(f'You got {str(score)} correct')


run_test(questions)