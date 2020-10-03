import random


WORDS = ['skillfactory', 'testing', 'blackbox', 'pytest', 'unittest', 'coverage']
RANDOM_WORD = random.choice(WORDS)
TEMPLATE = ''

def set_get_template(RANDOM_WORD):
    TEMPLATE = '_ ' * (len(RANDOM_WORD) - 1) + '_'
    print(TEMPLATE)
    TEMPLATE = list(TEMPLATE)
    return TEMPLATE

def update_template(TEMPLATE, RANDOM_WORD):


def game(words):
    # random_words = random.choice(words)
    template = '_ ' * (len(random_words) - 1) + '_'

    print(random_words)
    print(template)

    template = list(template)

    n_fail = 0
    n_success = 0
    while n_fail < 4 and n_success < len(random_words):
        litter = input('Укажите букву, которая есть в слове ')
        if litter in template:
            print('Эта буква уже угадана' )
            continue

        if litter in random_words:
            for i in range(len(random_words)):
                if random_words[i] == litter:
                    n_success += 1
                    template[i*2] = litter
            print(''.join(template))
        else:
            n_fail += 1
            print('Такой буквы нет в загаданном слове' )

    if  n_fail == 4:
        print('К сожалению, вы не отгадали слово.' )
        # return n_fail
    else :
        print('Поздравляю! Вы отгадали слово: ', random_words)

    return {'n_fail': n_fail, 'n_success': n_success, 'template' : template }

if __name__ == '__main__':
    words = ['skillfactory', 'testing', 'blackbox', 'pytest', 'unittest', 'coverage']
    random_words = random.choice(words)
    
    r = game(random_words)
    print(r)