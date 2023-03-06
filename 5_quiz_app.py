class Question:
    def __init__(self, text, choices, answer):
        self.text = text
        self.choices = choices
        self.answer = answer

    def check_answer(self, answer):
        return self.answer == answer


class Quiz:
    def __init__(self, question):
        self.question = question
        self.score = 0
        self.questionIndex = 0

    def get_question(self):
        return self.question[self.questionIndex]

    def display_question(self):
        question = self.get_question()
        print(f'Question {self.questionIndex + 1}: {question.text}')

        for q in question.choices:
            print('-' + q)

        answer = input('Answer: ')
        self.guess(answer)
        self.load_question()

    def guess(self, answer):
        question = self.get_question()

        if question.check_answer(answer):
            self.score += 1
        self.questionIndex += 1

    def load_question(self):
        if len(self.question) == self.questionIndex:
            self.show_score()
        else:
            self.display_progress()
            self.display_question()

    def show_score(self):
        print('Score: ', self.score)

    def display_progress(self):
        totalQuestion = len(self.question)
        questionNumber = self.questionIndex + 1

        if questionNumber > totalQuestion:
            print('Quiz Over.')
        else:
            print(f'Question {questionNumber} of {totalQuestion}'.center(100, '*'))

# Here are some sample questions
q1 = Question('What is the capital of Italy?', ['Rome', 'Milan', 'Venice', 'Florence'], 'Rome')
q2 = Question('What is the name of the longest river in the world?', ['Mississippi', 'Parana', 'Nile', 'Amazon'], 'Nile')
q3 = Question('Which country is not in the Northern hemisphere?', ['Japan', 'Argentina', 'Mexico', 'Hungary'], 'Argentina')
questions = [q1, q2, q3]

quiz = Quiz(questions)

quiz.load_question()