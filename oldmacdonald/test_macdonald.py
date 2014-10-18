# For this assignment, you will write a program to print the words
# to "Old MacDonald had a farm"
#
# The main idea is to use functions to build the repetitive parts of the verses,
# allowing the new animal names and sounds to be inserted easily.
#
# To begin, create a folder with a macdonald.py file, and a test_macdonald.py file
# Copy this file to your test_macdonald.py file, and build the other file to pass the tests.
import macdonald


# Make a simple function that returns a string.
def test_had_a_farm():
    assert 'Old MacDonald had a farm. E-I-E-I-O!' == macdonald.had_a_farm()


# Make a function that takes an animal name as an argument,
# and uses that name in the string returned.
def test_and_on_that_farm():
    assert 'And on that farm he had a pig. E-I-E-I-O!' == macdonald.and_on_that_farm('pig')


# Similarly, make a function for the animal noise.
def test_with_a():
    assert 'With a quack, quack here, and a quack, quack there. Here a quack, there a quack, everywhere a quack, quack.' == macdonald.with_a('quack')


# Make a function that returns 'a' or 'an' appropriately
def test_choose_article():
    assert 'a' == macdonald.choose_article('quack')
    assert 'an' == macdonald.choose_article('oink')


# Make use of the choose_article function so that the grammer works with 'oink'
def test_with_an():
    assert 'With an oink, oink here, and an oink, oink there. Here an oink, there an oink, everywhere an oink, oink.' == macdonald.with_a('oink')


# Make use of the choose_article function again, so that animals beginning with vowels work.
def test_had_an():
    assert 'And on that farm he had an alpaca. E-I-E-I-O!' == macdonald.and_on_that_farm('alpaca')


# Put these verses together to build an entire verse
def test_verse():
    print macdonald.build_verse("fish","blub")
    assert """Old MacDonald had a farm. E-I-E-I-O!
And on that farm he had a fish. E-I-E-I-O!
With a blub, blub here, and a blub, blub there. Here a blub, there a blub, everywhere a blub, blub.
Old MacDonald had a farm. E-I-E-I-O!
""" == macdonald.build_verse("fish","blub")

# Now that you can build a verse, use a loop to print at least four verses
