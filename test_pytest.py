import pytest
import game

LET = 's'
LET_FAIL = 'd'
TEMP = ['_','_','_','_','_','_','_','_','_','_', '_','_']

def setup_module(game):
    game.TEMPLATE = []

# тест формирования шаблона
def test_template(random_word):
    game.RANDOM_WORD = random_word
    tmp = game.set_get_template(random_word)
    assert TEMP == tmp

def test_exists_in_word(random_word):
    bb = game.exists_in_word(LET, random_word)
    assert bb == True

def test_update_template(random_word):
    game.RANDOM_WORD = random_word
    game.TEMPLATE = TEMP
    res_template = game.update_template(LET)
    assert res_template == ['s','_','_','_','_','_','_','_','_','_', '_','_']

@pytest.mark.xfail()
def test_fail_update_template(random_word):
    game.RANDOM_WORD = random_word
    game.TEMPLATE = TEMP
    res_template = game.update_template(LET)
    assert res_template == TEMP

@pytest.mark.xfail()
def test_fail_exists_in_word(random_word):
    bb = game.exists_in_word(LET_FAIL, random_word)
    assert bb == True

