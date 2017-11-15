# -*- coding: utf-8 -*-
""" Repaso interactivo de python
"""


def lower_up(lower, upper):
    for x in range(lower, upper+1):
        print(x)
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


def all_the_args(*args, **kwargs):
    print(args)
    print(str(kwargs).replace('\'', '"'))
    """ 2: Return an array. Use * to expand positional args and use **
    to expand keyword args

    >>> all_the_args(1, 2, a=3, b=4)
        (1, 2)
        {"a": 3, "b": 4}
    """


def may_20(tup):
    y=""
    for x in tup:
        if x >20:
            if y =="":
                y=str(x)
            else:
                y=y + ', ' + str(x)
    print(y)
    """ 3: Definir una tupla con 10 números. Imprimir la cantidad de números superiores a 20.
    >>> may_20(10, 16, 22, 26, 27, 30)
        22, 26, 27, 30
    """


def word_filter(list_of_words, n):
    for item in list_of_words:
        if len(item) > n:
            print item
    """ 4: Filtra las palabras que contienen más de n caracteres
    >>> word_filter([hello, bye, computer, software, python], 5)
	    [computer, software, python]
    """


def string_length(list):
    print len(item)
    """ 5: imprime el largo de una cadena de caracteres
    >>> string_length("popularity")
        10
    """


def is_vocal(x):
    if first in ('a', 'e', 'i', 'o', 'u'):
       print(True)
    else :
       print(False)

    """ 6: Determines if it is vocal
    >>> is_vocal(a)
        True
    >>> is_vocal(b)
        False
	"""


def is_leap_year(year):
    import calendar
    print calendar.isleap(year)
    """ 7: Determines if a year is a leap year.
	>>> is_leap_year(2016)
	    True
	"""

def has_uppercase(word):
    print(sum(1 for c in word if c.isupper()))
    """ 8: Evaluate if a word has uppercase letters
    >>> has_uppercase(MayuSculA)
        3
    """


def contar_vocales(cadena):
    print(sum(1 for c in cadena if c in ('a', 'e', 'i', 'o', 'u')))
    """ 9: Return number of vocales in a word.
    >>> contar_vocales(murcielago)
        5
    """


def square(list):
     print ([i ** 2 for i in list])
     """ 10: Calculate the square of the numbers in a list
	 >>> l = [0, 1, 2, 3]
     >>> square(l)
         [0, 1, 4, 9]
	"""


def is_prime(n):
    if n > 1:
         for i in range(2,n):
            if (n % i) == 0:
	           print(False)
	           break
	        else:
	           print(True)
    else:
	   print(False)
    """ 11:  Return if n is prime.
    >>> is_prime(5)
        True
    >>> is_prime(6)
        False
    """


def factorial(n):
    if n == 0:
       return 1
    else:
       return n * factorial(n-1)
    """ 12: Return the factorial of n, an exact integer >= 0.
    If the result is small enough to fit in an int, return an int.
    Else return a long.
    >>> [factorial(n) for n in range(6)]
        [1, 1, 2, 6, 24, 120]
    >>> [factorial(long(n)) for n in range(6)]
        [1, 1, 2, 6, 24, 120]
    >>> factorial(30)
        265252859812191058636308480000000L
    """


def to_roman(n):
    num_map = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
           (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
    roman = ''
    while n > 0:
        for i, r in num_map:
            while n >= i:
                roman += r
                n -= i
    print(roman)
    """ 13: Convert number integer to Roman numeral
	>>> to_roman(598)
        [DXCVIII]
    """


def rima(word1, word2):
    if word1[len(word1)-1]  == word2[len(word2)-1]:
        if word1[len(word1)-2]  == word2[len(word2)-2]:
            if word1[len(word1)-3]  == word2[len(word2)-3]:
                print("rima")
            else:
                print("rima un poco.")
        else:
            print("no rima")
   else:
        print("no rima")
	""" 14: Indica si dos palabrar riman. Si coinciden
	las 3 ultimas letras rima,
    si ncoinciden solo 2 rima un poco, si coincide solo 1 no rima.
    >>> rima(flor, coliflor)
        rima
    >>> rima(amar, plantar)
        rima un poco.
	>>> rima(azucar, barrer)
        no rima
    """


def capital(pesos, interes, anios):
    resultado=pesos*(1+interes/100)**anios
    print(round(resultado,2))
    """ 15: Pide una cantidad de pesos, una tasa de interés y un
	numero de años. Muestra en cuanto se habrá convertido el
    capital inicial transcurridos esos años si cada año se aplica
	la tasa de interés introducida.
    >>> capital(10000, 4.5, 20)
        24117.14
    """
