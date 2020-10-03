import pytest
import random


words = ['skillfactory']
# r_words = random.choice(words)

@pytest.fixture()
def random_word():
    return random.choice(words)

# @pytest.fixture()
# def get_template(r_words):
#     template = list('_ ' * (len(r_words) - 1) + '_')
#     return template

