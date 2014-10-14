def had_a_farm():
    return 'Old MacDonald had a farm. E-I-E-I-O!'


def and_on_that_farm(animal):
    article = choose_article(animal)
    return 'And on that farm he had {0} {1}. E-I-E-I-O!'.format(article, animal)


def with_a(sound):
    article = choose_article(sound)
    with_a_ = 'With {0} {1}, {1} here, and {0} {1}, {1} there. '.format(article, sound)
    here_a_ = 'Here {0} {1}, there {0} {1}, everywhere {0} {1}, {1}.'.format(article, sound)
    return with_a_ + here_a_


def choose_article(sound):
    return 'an' if sound[0].lower() in 'aeiou' else 'a'


def print_verse(animal, sound):
    lines = [had_a_farm(), and_on_that_farm(animal), with_a(sound), had_a_farm()]
    return "\n".join(lines) + "\n"

animals = {'pig': 'oink',
           'cow': 'moo',
           'duck': 'quack',
           'sheep': 'baa',
           'alpaca':'humng',
           'dog': 'bark'}

for name in animals:
    print print_verse(name, animals[name])
