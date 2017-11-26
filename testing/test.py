from hypothesis import given, example
from hypothesis.strategies import text

@given(text())
@example(5,10)
def test_lowerup(lower,upper):
    assert lower_up_while(lower,upper) == lower_up_while(lower, upper)


@given(text())
@example(['computer', 'software', 'python'],5)
def test_word_filter(lower,upper):
    assert word_filter(lower,upper) == word_filter_2(lower, upper)


@given(text())
@example('hola')
def test_word_filter(l):
    assert string_length(l) == string_length(l)



@given(text())
@example('murcielago')
def test_is_vocal(l):
    assert is_vocal2(l) == is_vocal(l)


@given(text())
@example('2016')
def test_is_leapyear(l):
    assert is_leap_year2(l) == is_leap_year(l)


@given(text())
@example('Mario')
def test_is_hasuppercase(l):
    assert is_all_uppercase(l) == has_uppercase(l)


@given(text())
@example('Mario')
def test_is_manyvowels(l):
    assert contar_vocales(l) == countvowels(l)


@given(text())
@example([3,2,1])
def test_is_square(l):
    assert squareit(l) == square(l)


@given(text())
@example(20)
def test_is_leapyear(l):
    assert isprime(l) == is_prime(l)



@given(text())
@example(20)
def test_is_factorial(l):
    assert factorialmath(l) == factorial(l)


@given(text())
@example(650)
def test_is_roman(l):
    assert write_roman(l) == to_roman(l)














