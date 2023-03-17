import random
import requests


class Question:
    def __init__(self, question_text: str, answers: list[str], correct_answer: str):
        self._answers = answers
        self._correct_answer = correct_answer
        self._text = question_text

    def get_answers(self):
        return self._answers

    def get_question(self):
        return self._text

    def check_answer(self, guess):
        return True if guess == self._correct_answer else False


class Quiz:
    def __init__(self, category: str = None, difficulty: str = None, num_qs: int = 10):
        self.difficulty = difficulty
        self.category = category
        self.number_of_questions = num_qs
        self._questions = self._populate_questions()
        self._correct_answers = 0

    def _populate_questions(self) -> list[Question] | bool:
        api_url = f'https://the-trivia-api.com/api/questions'

        params = {'region': 'GB'}

        if self.category is not None:
            params['categories'] = self.category

        if self.difficulty is not None:
            params['difficulty'] = self.difficulty

        params['limit'] = self.number_of_questions

        try:
            res = requests.get(api_url, params=params, headers={'Content-Type': 'application/json'})
            if res.ok:
                qs = res.json()
                prepare_qs = []
                for q in qs:
                    correct_answer = q['correctAnswer']
                    all_answers = q['incorrectAnswers']
                    all_answers.append(correct_answer)
                    prepare_qs.append(
                        Question(question_text=q['question'], answers=all_answers, correct_answer=correct_answer))
                return prepare_qs
            else:
                return False
        except Exception as e:
            print(f'encountered an error: {e}')
            return False

    def run_quiz(self):
        print('##################################'
              '#         Let\'s Begin!          #'
              '##################################')

        random.shuffle(self._questions)

        for i, q in enumerate(self._questions):
            answers = q.get_answers()
            random.shuffle(answers)
            print(f'+----------------------------------------------------------+\n'
                  f'| QUESTION 1: {q.get_question()}                           |\n'
                  f'+----------------------------------------------------------|\n')

            for j, a in enumerate(answers):
                print(f'| {j})    {a}                                                 |')

            print(f'+----------------------------------------------------------+\n')





