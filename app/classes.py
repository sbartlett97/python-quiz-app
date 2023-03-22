import datetime
import random
import time
import requests


class Question:
    """A Question class that holds the relevant question information 
    in a single class with getters and setters

    Args:
        question_text (str): The question itself
        answers (list[str]): A list of all the possible answers
        correct_answer (str): The correct asnwer to the question
    """
    def __init__(self, question_text: str, answers: list[str], correct_answer: str):
        self._answers = answers
        self._correct_answer = correct_answer
        self._text = question_text

    def get_answers(self) -> list[str]:
        """Returns the possible answers to a question

        Returns:
            str: The question answers
        """
        return self._answers

    def get_question(self) -> str:
        """Returns the question being asked

        Returns:
            str: The question text
        """
        return self._text

    def check_answer(self, guess: int):
        """Checks if the guessed answer is correct

        Args:
            guess (int): The array index of the guess

        Returns:
            bool: Guess is correct
        """
        return True if guess == self._correct_answer else False

    def get_correct_answer(self) -> str:
        """Returns the corect answer for the question

        Returns:
            str: The correct answer 
        """
        return self._correct_answer


class Quiz:
    def __init__(self, player: str, category: str = None, difficulty: str = None, num_qs: int = 10):
        self._player = player
        self.difficulty = difficulty
        self.category = category
        self._number_of_questions = num_qs
        self._questions = self._populate_questions()
        self._results = []
        self._correct_answers = 0

    def _populate_questions(self) -> list[Question] | bool:
        api_url = 'https://the-trivia-api.com/api/questions'

        params = {'region': 'GB'}

        if self.category is not None:
            params['categories'] = self.category

        if self.difficulty is not None:
            params['difficulty'] = self.difficulty

        params['limit'] = self._number_of_questions

        try:
            res = requests.get(api_url, params=params, headers={'Content-Type': 'application/json'}, timeout=60)
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
           
            return False
        except Exception as err:
            print(f'encountered an error: {err}')
            return False
        
    def print_question(self, q_num: int, q: Question):
        """Prints a Quiz Question and multiple choice answers to the terminal

        Args:
            q_num (int): The question Number
            q (Question): The Question Object
        """

        print(f'+----------------------------------------------------------+\n'
                f'| QUESTION {q_num}: {q.get_question()}                           |\n'
                f'+----------------------------------------------------------|\n')

        for j, a in enumerate(random.shuffle(q.get_answers())):
            print(f'| ({j+1})    {a}                                                 |')

        print('+----------------------------------------------------------+\n')


    def get_guess(self) -> int:
        while True:
            try:
                guess = int(input('What is your answer? (1-4): '))
                if 0 < guess < 5:
                    break
            except TypeError:
                print('\nYour guess must be a number between 1 and 4!\n')
        
        return int(guess)

    def run_quiz(self):
        print('##################################\n'
              '#         Let\'s Begin!          #\n'
              '##################################\n')

        for i, q in enumerate(self._questions):
            self.print_question(i, q)
            
            
            g = self.get_guess()
                

            correct = q.check_answer(g)
            
            if correct:
                self._correct_answers += 1
                self._results.append(f'Question ({i}) {q.get_question()}: Correct! Answer was: {q.get_correct_answer}')
            else:
                self._results.append(f'Question ({i}) {q.get_question()}: incorrect. Answer was: {q.get_correct_answer}')
            time.sleep(0.5)

        # Questions finished
        print('###############################################################\n'
              '#        Thanks for playing, Let\'s see how you did!          #\n'
              '###############################################################\n')
        print('+---------------------------------------------------------------------+\n')
        for r in self._results:
            print(f'|   {r}')
        print('+---------------------------------------------------------------------+\n')

        print(f'That means you got {self._correct_answers}/{self._number_of_questions} correct!')
        while True:
            save = input('Would you like to save your results? (Y/N): ')
            if save in ['y', 'Y']:
                with open(f'{self._player}_{datetime.datetime.now()}_results.txt', 'w') as results_file:
                    results_file.writelines(self._results)
            break


class QuizApp:
    def __init__(self):
        self.user = ''
        self._categories = {'Arts & Literature': 'arts_and_literature', 'Film & TV': 'film_and_tv',
                            'Food & Drink': 'food_and_drink', 'General Knowledge': 'general_knowledge',
                            'Geography': 'geography', 'History': 'history', 'Music': 'music', 'Science': 'science',
                            'Society & Culture': 'society_and_culture', 'Sport & Literature': 'sport_and_leisure'}
        self._difficulties = ['Easy', 'Medium', 'Hard']


    def start(self):
        pass

    def header(self):
        pass

    def categories(self):
        pass

    def difficulty(self):
        pass

