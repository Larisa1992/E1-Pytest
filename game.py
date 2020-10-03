import random

WORDS = ['skillfactory', 'testing', 'blackbox', 'pytest', 'unittest', 'coverage']
RANDOM_WORD = random.choice(WORDS)


def set_get_template(RANDOM_WORD):
    TEMPLATE = ['_' for i in range(len(RANDOM_WORD))]
    return TEMPLATE

TEMPLATE = set_get_template(RANDOM_WORD)

def exists_in_word(letter, word):
    return letter in word

def update_template(letter):
    for i in range(len(RANDOM_WORD)):
        if RANDOM_WORD[i] == letter:
            TEMPLATE[i] = letter
    return TEMPLATE

if __name__ == '__main__':

    n_fail = 0
    set_get_template(RANDOM_WORD) # формируем шаблон

    while (n_fail < 4) and ('_' in TEMPLATE):
        letter = input('Укажите букву, которая есть в слове ')
        print(f' TEMPLATE while = {TEMPLATE}')

        if exists_in_word(letter, RANDOM_WORD):
  
            if exists_in_word(letter, TEMPLATE):
                print(f'Буква {letter} угадана ранее')
                print(' '.join(TEMPLATE))
            else:
                update_template(letter)
                print(' '.join(TEMPLATE))
        else:
            n_fail += 1
            print('Такой буквы нет в загаданном слове')
            print(' '.join(TEMPLATE))
    if n_fail == 4:
        print('К сожалению, вы не отгадали слово.')
    else:
        print(f'Поздравляю! Вы отгадали слово: {RANDOM_WORD}')