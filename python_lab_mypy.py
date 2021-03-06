# -*- coding: utf-8 -*- Repaso interactivo de python
from typing import Iterable
from typing import Any
from typing import List
from typing import Dict
from typing import Tuple
from typing import Union

def lower_up(lower: int, upper: int) -> None:
    """ 1: Returns a list of numbers from the lower number to the upper number:
    >>> lower_up(5,15)
    5
    6
    7
    8
    9
    10
    11
    12
    13
    14
    15
        """
    for x in range(lower, upper+1):
        print(x)


def all_the_args(*args: str, **kwargs: bool) -> None:
    """ 2: Return an array. Use * to expand positional args and use **
    to expand keyword args

    >>> all_the_args(1, 2, a=3, b=4)
    (1, 2)
    {"a": 3, "b": 4}
    """
    print(args)
    print(str(kwargs).replace('\'', '"'))


def may_20(*tup: Tuple[int]) -> None:
    """ 3: Definir una tupla con 10 números. Imprimir la
        cantidad de números superiores a 20.
    >>> may_20(10, 16, 22, 26, 27, 30)
    22, 26, 27, 30
    """
    lists: List[int] = []
    for x in tup:
        result: int = may_20_1(x)
        lists.append(result)
    y = str(list(filter(None, lists)))
    print(y[1:-1])


def may_20_1(x: Tuple[int]) -> int:
    if x[0] > 20:
        return x[0]
    return x[0]


def word_filter(list_of_words: List[str], n: int) -> None:
    """ 4: Filtra las palabras que contienen más de n caracteres
    >>> word_filter(['hello', 'bye', 'computer', 'software', 'python'],5)
    ['computer', 'software', 'python']
    """
    lista: List[str] = []
    for item in list_of_words:
        prueba(item, n, lista)
    print(lista)


def prueba(x: str, n: int, lista: List[str]) -> None:
    if len(x) > n:
            lista.append(x)


def string_length(list: str) -> None:
    """ 5: imprime el largo de una cadena de caracteres
    >>> string_length("popularity")
    10
    """
    print(len(list))


def is_vocal(x: str) -> None:
    """ 6: Determines if it is vocal
    >>> is_vocal('a')
    True
    >>> is_vocal('b')
    False
    """
    if x in ('a', 'e', 'i', 'o', 'u'):
        print(True)
    else:
        print(False)


def is_leap_year(year: int) -> None:
    """ 7: Determines if a year is a leap year.
        >>> is_leap_year(2016)
        True
    """
    import calendar
    print(calendar.isleap(year))


def has_uppercase(word: str) -> None:
    """ 8: Evaluate if a word has uppercase letters
    >>> has_uppercase('MayuSculA')
    3
    """
    result: Union[str, int] = sum(1 for c in word if c.isupper())
    print(result)


def contar_vocales(cadena: str) -> None:
    """ 9: Return number of vocales in a word.
    >>> contar_vocales('murcielago')
    5
    """
    result: Union[str, int] = sum(1 for c in cadena if c in ('a', 'e', 'i', 'o', 'u'))
    print(result)


def square(list: List[int]) -> None:
    """ 10: Calculate the square of the numbers in a list
    >>> l = [0, 1, 2, 3]
    >>> square(l)
    [0, 1, 4, 9]
    """
    result: List[int] = [i ** 2 for i in list]
    print(result)


def is_prime(n: int) -> None:
    """ 11:  Return if n is prime.
    >>> is_prime(5)
    True
    >>> is_prime(6)
    False
    """
    if n > 1:
        loopprime(n)
    else:
        print(False)


def prime(n: int, i: int)-> None:
    if (n % i) == 0:
        print(False)
        return
    else:
        print(True)
        return


def loopprime(n: int) -> None:
    for i in range(2, n):
        prime(n, i)
        break


def factorial(n: int) -> int:
    """ 12: Return the factorial of n, an exact integer >= 0.
    If the result is small enough to fit in an int, return an int.
    Else return a long.
    >>> [factorial(n) for n in range(6)]
    [1, 1, 2, 6, 24, 120]
    >>> [factorial(long(n)) for n in range(6)]
    [1, 1L, 2L, 6L, 24L, 120L]
    >>> factorial(30)
    265252859812191058636308480000000L
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


def to_roman(num: int) -> List[str]:
    """ 13: Convert number integer to Roman numeral
        >>> to_roman(598)
        ['DXCVIII']
    """
    val = (1000, 900,  500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
    syb = ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX',
           'V', 'IV', 'I')
    roman_num = ""
    list = []
    for i in range(len(val)):
        count = int(num / val[i])
        roman_num += syb[i] * count
        num -= val[i] * count
    list.append(roman_num)
    return list


def rima(word1: str, word2: str) -> None:
    """ 14: Indica si dos palabrar riman. Si coinciden
        las 3 ultimas letras rima,
        si ncoinciden solo 2 rima un poco, si coincide solo 1 no rima.
    >>> rima('flor', 'coliflor')
    rima
    >>> rima('amar', 'plantar')
    rima un poco.
    >>> rima('azucar', 'barrer')
    no rima
    """
    if word1[len(word1)-1] == word2[len(word2)-1]:
        rima3(word1, word2)
    else:
        print('no rima')


def rima3(word1: str, word2: str) -> None:
    if word1[len(word1)-2] == word2[len(word2)-2]:
        rima2(word1, word2)
    else:
        print('no rima')


def rima2(word1: str, word2: str) -> None:
    if word1[len(word1)-3] == word2[len(word2)-3]:
        print('rima')
    else:
        print('rima un poco.')


def capital(pesos: int, interes: int, anios: int) -> None:
    """ 15: Pide una cantidad de pesos, una tasa de interés y un
        numero de años. Muestra en cuanto se habrá convertido el
    capital inicial transcurridos esos años si cada año se aplica
    la tasa de interés introducida.
    >>> capital(10000, 4.5, 20)
    24117.14
    """
    resultado = pesos * (1 + interes / 100) ** anios
    print(round(resultado, 2))
