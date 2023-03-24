from app.classes import Question, Quiz


categories = {'Arts & Literature': 'arts_and_literature', 'Film & TV': 'film_and_tv',
              'Food & Drink': 'food_and_drink', 'General Knowledge': 'general_knowledge',
              'Geography': 'geography', 'History': 'history', 'Music': 'music', 'Science': 'science',
              'Society & Culture': 'society_and_culture', 'Sport & Literature': 'sport_and_leisure'}

difficulties = ['Easy', 'Medium', 'Hard']

def print_options() -> list[int]:
    base = ''
    cat_option_nums = []
    for i, cat in enumerate(categories.keys()):
        base += f'({i+1}): {cat} '
        base += '\n' if i % 2 != 0 else '| '
        cat_option_nums.append(i+1)
    print(base)
    return cat_option_nums

def print_difficulties():
    print(' | '.join([f'{i+1}) {diff}' for i, diff in enumerate(difficulties)]))

def main():
    print('###################################################\n'
          '#             Weclome to PyQuiz!                  #\n'
          '###################################################\n')
    
    user = ''

    while user == '':
        user = input('What is your name?: ')

    print(f'\nHello, {user}!')
    print('What kind of quiz would you like to take today?\n')
    cat_options = print_options()
    cat_choice = 0
    
    while cat_choice not in cat_options:
        try: 
            cat_choice = int(input('\nPlease enter the number of the category you\'d like to play: '))
        except TypeError:
            print(f'Please enter a number between {cat_options[0]} and {cat_options[-1]}')
            diff = 0
             
    cat = list(categories.keys())[cat_choice-1]
    print(f'\n\nYou have chosen: {cat}.\n\n')

    print_difficulties()
    diff = 0

    while diff < 1 or diff >  3:
        try:
            diff = int(input('Please choose a difficulty: '))
        except TypeError:
            print('Please enter a number between 1 and 3.')
            diff = 0
    quiz = Quiz(player=user, category=categories[cat], difficulty=difficulties[diff-1])

    print('\nLets Begin!')

    quiz.run_quiz()


if __name__ == '__main__':
    main()
