import random
from utils import Question, create_question_objects, questions

question_data = [
  {
    "q": "How many days do we have in a week?",
    "d": "1",
    "a": "7"
  },
  {
    "q": "How many letters are there in the English alphabet?",
    "d": "3",
    "a": "26"
  },
  {
    "q": "How many sides are there in a triangle?",
    "d": "2",
    "a": "3"
  },
  {
    "q": "How many years are there in one Millennium?",
    "d": "2",
    "a": "1000"
  },
  {
    "q": "How many sides does hexagon have?",
    "d": "4",
    "a": "6"
  }
]


def ask_questions_and_get_answers(questions):
    random.shuffle(questions)
    total_questions = len(questions)
    answered_questions = 0
    total_points = 0

    for question in questions:
        print()
        print(question.build_question())
        question.user_answer = input("Ваш ответ: ")

        if question.is_correct():
            print(question.build_positive_feedback())
            points = question.difficulty * 10
            total_points += points
        else:
            print(question.build_negative_feedback())

        answered_questions += 1

    return answered_questions, total_points, total_questions


def print_statistics(answered_questions, total_points, total_questions):
    print('\nВот и всё!')
    print(f'Отвечено {answered_questions} вопроса из {total_questions}')
    print(f'Набрано баллов: {total_points}')


def main():
    answered_questions, total_points, total_questions = ask_questions_and_get_answers(questions)
    print_statistics(answered_questions, total_points, total_questions)


if __name__ == "__main__":
    main()


