class Question:
    def __init__(self, question_text, difficulty, correct_answer):
        self.question_text = question_text
        self.difficulty = difficulty
        self.correct_answer = correct_answer
        self.question_asked = False
        self.user_answer = None
        # self.points = self.calculate_points()

    def get_points(self):
        """
        Возвращает int, количество баллов.
        Баллы зависят от сложности: за 1 дается 10 баллов, за 5 дается 50 баллов.
        """
        if self.difficulty == 1:
            return 10
        elif self.difficulty == 2:
            return 20
        elif self.difficulty == 3:
            return 30
        elif self.difficulty == 4:
            return 40
        elif self.difficulty == 5:
            return 50
        else:
            return 0

    def is_correct(self):
        """Возвращает True, если ответ пользователя совпадает
        с верным ответом иначе False.
        """
        return self.user_answer == self.correct_answer

    def build_question(self):
        """Возвращает вопрос в понятном пользователю виде, например:
        Вопрос: What do people often call American flag?
        Сложность 4/5
        """
        return f"Вопрос: {self.question_text}\nСложность: {self.difficulty}/5"

    def build_positive_feedback(self):
        """Возвращает:
        Ответ верный, получено __ баллов
        """
        score = self.difficulty * 10
        return f"Ответ верный, получено {score} баллов."

    def build_negative_feedback(self):
        """Возвращает:
        Ответ неверный, верный ответ __
        """
        return f"Ответ неверный, верный ответ: {self.correct_answer}."


# Создание списка экземпляров класса Question
def create_question_objects(data):
    question_objects = []
    for item in data:
        question = Question(item['q'], item['d'], item['a'])
        question_objects.append(question)
    return question_objects


questions = create_question_objects(question_data)

