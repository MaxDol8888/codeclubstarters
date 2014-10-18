import pytest
import hangman

hangman.secret = 'CIRCLEVILLE PUMPKIN SHOW'


def test_determines_if_letter_in_secret():
    assert hangman.check_letter('L')
    assert not hangman.check_letter('T')


def test_check_letter_disregards_case():
    assert hangman.check_letter('i')


def test_records_correct_guesses(setup):
    hangman.check_letter('A')
    hangman.check_letter('N')
    hangman.check_letter('E')
    hangman.check_letter('D')

    assert 'A' not in hangman.correct_letters
    assert 'N' in hangman.correct_letters
    assert 'E' in hangman.correct_letters
    assert 'D' not in hangman.correct_letters
    assert len(hangman.missed_letters) == 2


def test_records_misses(setup):
    hangman.check_letter('A')
    hangman.check_letter('N')
    hangman.check_letter('E')
    hangman.check_letter('D')

    assert 'A' in hangman.missed_letters
    assert 'N' not in hangman.missed_letters
    assert 'E' not in hangman.missed_letters
    assert 'D' in hangman.missed_letters
    assert len(hangman.missed_letters) == 2


def test_display_secret_with_no_guesses(setup):
    hangman.secret = 'PYTHON'

    assert '- - - - - -' == hangman.hide_word()


def test_display_secret_with_guesses(setup):
    hangman.secret = 'PYTHON'
    hangman.correct_letters = ['T', 'N']

    assert '- - T - - N' == hangman.hide_word()


def test_display_secret_phrase_with_spaces(setup):
    hangman.secret = 'FOR THE WIN'
    hangman.correct_letters = ['T', 'N']

    assert '- - -   T - -   - - N' == hangman.hide_word()


@pytest.fixture
def setup():
    hangman.correct_letters = []
    hangman.missed_letters = []
