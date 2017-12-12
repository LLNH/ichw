from urllib.request import urlopen
def exchange(currency_from, currency_to, amount_from):
    """Returns: amount of currency received in the given exchange.

    In this exchange, the user is changing amount_from money in 
    currency currency_from to the currency currency_to. The value 
    returned represents the amount in currency currency_to.

    The value returned has type float.

    Parameter currency_from: the currency on hand
    Precondition: currency_from is a string for a valid currency code

    Parameter currency_to: the currency to convert to
    Precondition: currency_to is a string for a valid currency code

    Parameter amount_from: amount of currency to convert
    Precondition: amount_from is a float"""
    trans={'ab':'currency_from','bc':'currency_to','cd':'amount_to'}
    doc = urlopen('http://cs1110.cs.cornell.edu/2016fa/a1server.php?from={ab}&to={bc}&amt={cd}'.format(**trans))
    docstr = doc.read()
    doc.close()
    jstr = docstr.decode('ascii')
    jstr = jstr[0:-34]+"}"
    dic=eval(jstr)
    ed=dic['"to"']
    a=ed.split(' ')
    c=float(a[0])
    return c

    


'''The module below is '''
def testA():
    assert(0.60410644907845 == exchange(NZD,EUR,1.0))

def testB():
    assert(0.1732197588011 == exchange(NOK,OMR,3.5))

def testC():
    assert(1.7447354516872 == exchange(BWP,PGK,5.5))

def testD():
    assert(0.16436791777583 == exchange(CLP,PHP,2.0))

def testE():
    assert(0.0028791281617024 == exchange(MMK,AZN,2.3))


def test_all():
    testA()
    testB()
    testC()
    testD()
    testE()
    print('All tests passed!')
    


    
