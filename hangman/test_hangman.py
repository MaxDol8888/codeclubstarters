# Our next game is "hangman". You know how it works, a player tries to guess
# letters in the secret word or phrase. The player wins if all letters are
# guessed, the player loses if it misses seven times.
import pytest
import hangman


# Create a file called hangman.py, with the first lines:
#
# secret = ''
# correct_letters = []
# missed_letters = []
#
# The following function sets and resets these values for the sake of these tests
@pytest.fixture
def setup():
    hangman.secret = 'CIRCLEVILLE PUMPKIN SHOW'
    hangman.correct_letters = []
    hangman.missed_letters = []


# First, we need a `check_letter` function that determines if a guess is in
# our secret phrase.
def test_determines_if_letter_in_secret(setup):
    assert hangman.check_letter('L')
    assert not hangman.check_letter('T')


def test_check_letter_disregards_case(setup):
    assert hangman.check_letter('i')


# We will need to keep record of which letters have been correctly guessed.
# There are many ways to do this, we will simply append letters to
# the correct_letters list as letters are checked.
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


# We will also need to keep track of letters missed, so we can display misses.
def test_records_misses(setup):
    hangman.check_letter('N')
    hangman.check_letter('E')
    hangman.check_letter('A')
    hangman.check_letter('D')

    assert 'A' in hangman.missed_letters
    assert 'N' not in hangman.missed_letters
    assert 'E' not in hangman.missed_letters
    assert 'D' in hangman.missed_letters
    assert len(hangman.missed_letters) == 2


# We will need a function that I have called hide_word to partially display
# words, indicating number of letters and spaces as the next three tests
# indicate.
#
# Note that the value of the secret is changed for these tests.
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


# It will also be convenient to have a function that can tell us whether
# the hangman puzzle has been solved.
def test_checks_for_all_correct():
    hangman.secret = 'CODE'

    hangman.check_letter('A')
    hangman.check_letter('B')
    hangman.check_letter('C')
    hangman.check_letter('D')
    hangman.check_letter('E')

    assert not hangman.solved()

    hangman.check_letter('O')
    assert hangman.solved()

# At this point you have many useful pieces, but there is significant work to do.
# You still need to code the following:
#
# First: Selecting a word or phrase randomly from a list.
# Then have a while loop, in which:
#
#     - Computer displays the current word (in hidden form)
#     - Computer also displays the list of missed guesses
#     - Player guesses letter
#     - Computer responds with message indicating either missed or correct
#
# This continues until one of two things happen:
#     - The puzzle is solved
#     - Seven misses are recorded
#
# Once this works, you should add the following:
#     - A main loop, so that the game can be repeated
#     - Some nice ascii art indicating the players danger:
#
#     +----+
#     |    |
#    \O/   |
#     |    |
#     |    |
#   _/ \_  |
#          |
#    ------+--
#     |     |
#
# This is what I came up with in a few minutes, surely you can do better.
#
# You will need to keep a list of strings for each of the hangman stages, and
# choose one to dispaly after each turn.