# -*- coding: utf-8 -*- Repaso interactivo de python
from contracts import contract

@contract(lower='>0',
          upper='>0', 
          returns='list(int)')
def lower_up(lower, upper):
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
        return(x)

@contract(args='!None',
          kwargs='!None', 
          returns='list(str)')
def all_the_args(*args, **kwargs):
    """ 2: Return an array. Use * to expand positional args and use **
    to expand keyword args

    >>> all_the_args(1, 2, a=3, b=4)
    (1, 2)
    {"a": 3, "b": 4}
    """
    print(args)
    return(str(kwargs).replace('\'', '"'))

@contract(tup='!None',
          returns='tuple(int, int)')
def may_20(*tup):
    """ 3: Definir una tupla con 10 números. Imprimir la
        cantidad de números superiores a 20.
    >>> may_20(10, 16, 22, 26, 27, 30)
    22, 26, 27, 30
    """
    lists = []
    for x in tup:
        lists.append(may_20_1(x))
    y = str(list(filter(None, lists)))
    return(y[1:-1])


def may_20_1(x):
    if x > 20:
        return x


@contract(list_of_words='!None',
          n='>0', 
          returns='list(str)')
def word_filter(list_of_words, n):
    """ 4: Filtra las palabras que contienen más de n caracteres
    >>> word_filter(['hello', 'bye', 'computer', 'software', 'python'],5)
    ['computer', 'software', 'python']
    """
    lista = []
    for item in list_of_words:
        prueba(item, n, lista)
    return(lista)


def prueba(x, n, lista):
    if len(x) > n:
            lista.append(x)


@contract(list='!None',
          returns='int')
def string_length(list):
    """ 5: imprime el largo de una cadena de caracteres
    >>> string_length("popularity")
    10
    """
    return(len(list))


@contract(x='!int,!float',
          returns='bool')
def is_vocal(x):
    """ 6: Determines if it is vocal
    >>> is_vocal('a')
    True
    >>> is_vocal('b')
    False
    """
    if x in ('a', 'e', 'i', 'o', 'u'):
        return(True)
    else:
        return(False)


@contract(year='int',
          returns='bool')
def is_leap_year(year):
    """ 7: Determines if a year is a leap year.
        >>> is_leap_year(2016)
        True
    """
    import calendar
    return(calendar.isleap(year))


@contract(word='!None',
          returns='int')
def has_uppercase(word):
    """ 8: Evaluate if a word has uppercase letters
    >>> has_uppercase('MayuSculA')
    3
    """
    return(sum(1 for c in word if c.isupper()))


@contract(cadena='str',
          returns='int')
def contar_vocales(cadena):
    """ 9: Return number of vocales in a word.
    >>> contar_vocales('murcielago')
    5
    """
    return(sum(1 for c in cadena if c in ('a', 'e', 'i', 'o', 'u')))


@contract(list='list[int]',
          returns='list[int]')
def square(list):
    """ 10: Calculate the square of the numbers in a list
    >>> l = [0, 1, 2, 3]
    >>> square(l)
    [0, 1, 4, 9]
    """
    return([i ** 2 for i in list])



@contract(n='int',
          returns='bool')
def is_prime(n):
    """ 11:  Return if n is prime.
    >>> is_prime(5)
    True
    >>> is_prime(6)
    False
    """
    if n > 1:
        loopprime(n)
    else:
        return(False)


def prime(n, i):
    if (n % i) == 0:
        print(False)
        return
    else:
        print(True)
        return


def loopprime(n):
    for i in range(2, n):
        prime(n, i)
        break


@contract(n='int',
          returns='int')
def factorial(n):
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


@contract(num='int',
          returns='str')
def to_roman(num):
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


@contract(word1='str',
          word2='str',
          returns='str')
def rima(word1, word2):
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


def rima3(word1, word2):
    if word1[len(word1)-2] == word2[len(word2)-2]:
        rima2(word1, word2)
    else:
        print('no rima')


def rima2(word1, word2):
    if word1[len(word1)-3] == word2[len(word2)-3]:
        print('rima')
    else:
        print('rima un poco.')


@contract(pesos='int, >0',
          interes='float, >0.0',
          anios='int,>0',
          returns='float')
def capital(pesos, interes, anios):
    """ 15: Pide una cantidad de pesos, una tasa de interés y un
        numero de años. Muestra en cuanto se habrá convertido el
    capital inicial transcurridos esos años si cada año se aplica
    la tasa de interés introducida.
    >>> capital(10000, 4.5, 20)
    24117.14
    """
    resultado = pesos * (1 + interes / 100) ** anios
    print(round(resultado, 2))
