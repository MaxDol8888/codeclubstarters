import macdonald


def test_had_a_farm():
    assert 'Old MacDonald had a farm. E-I-E-I-O!' == macdonald.had_a_farm()


def test_and_on_that_farm():
    assert 'And on that farm he had a pig. E-I-E-I-O!' == macdonald.and_on_that_farm('pig')


def test_with_a():
    assert 'With a quack, quack here, and a quack, quack there. Here a quack, there a quack, everywhere a quack, quack.' == macdonald.with_a('quack')


def test_choose_article():
    assert 'a' == macdonald.choose_article('quack')
    assert 'an' == macdonald.choose_article('oink')


def test_with_an():
    assert 'With an oink, oink here, and an oink, oink there. Here an oink, there an oink, everywhere an oink, oink.' == macdonald.with_a('oink')


def test_had_an():
    assert 'And on that farm he had an alpaca. E-I-E-I-O!' == macdonald.and_on_that_farm('alpaca')


def test_verse():
    print macdonald.print_verse("fish","blub")
    assert """Old MacDonald had a farm. E-I-E-I-O!
And on that farm he had a fish. E-I-E-I-O!
With a blub, blub here, and a blub, blub there. Here a blub, there a blub, everywhere a blub, blub.
Old MacDonald had a farm. E-I-E-I-O!
""" == macdonald.print_verse("fish","blub")