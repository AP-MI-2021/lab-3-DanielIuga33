def toateElementelePalindroame(l):
    '''
    determina daca toate nr. dintr-o lista sunt palindroame
    :param l: lista de nr. intregi
    :return: True, daca toate nr. din l sunt palindroame sau False, in caz contrar
    '''
    for x in l:
        cx=x
        inv = 0
        while cx!=0:
            inv = inv * 10 + cx %10
            cx = cx// 10
        if inv != x:
            return False
    return True

def testToateElementelePalindroame():
    assert toateElementelePalindroame([1, 2, 3]) is True
    assert toateElementelePalindroame([13, 11, 10]) is False
    assert toateElementelePalindroame([33, 11, 21, 55, 12]) is False
    assert toateElementelePalindroame([]) is True

def SubsecventaMaxElementePalindroame(l):
    '''
    determina cea mai lunga subsecventa de nr. palindroame
    :param l: lista de nr. intregi
    :return: cea mai lunga subsecventa de nr. palindroame din l
    '''
    SubsecventaMax = []
    for i in range(len(l)):
        for j in range(i, len(l)):
            if toateElementelePalindroame(l[i:j+1]) and len(l[i:j+1]) > len(SubsecventaMax):
                SubsecventaMax = l[i:j+1]
    return SubsecventaMax

def testSubsecventaMaxElementePalindroame():
    assert SubsecventaMaxElementePalindroame([11,12,13,15]) == [11]
    assert SubsecventaMaxElementePalindroame([11,33,22,12,13]) == [11,33,22]
    assert SubsecventaMaxElementePalindroame([11,12,33,22,45]) == [33,22]
    assert SubsecventaMaxElementePalindroame([]) == []

def printMenu():
    print("1. Citire lista")
    print("2. Afisare cea mai lunga subsecventa de palindroame")
    print("3. Afisare cea mai lunga subsecventa de numere cu cifre prime")
    print("4. Toate numerele sunt divizibile cu k (citit).")
    print("x. Iesire")

def citireLista():
    l = []
    givenString = input("Dati lista, cu elementele separate prin virgula: ")
    numberAssString=givenString.split(",")
    for x in numberAssString:
        l.append(int(x))
    return l

def isPrime(x):
    if x<2:
        return False
    for i in range(2,x//2 +1):
        if x%i==0:
            return False
    return True
def numereCuCifrePrimeDinLista(l):
    for n in l:
        while n!=0:
            cif=n%10
            n = n // 10
            if isPrime(cif) == False:
                return False
    return True

def testNumereCuCIfrePrimeDinLista():
    assert numereCuCifrePrimeDinLista([2,3,11]) is False
    assert numereCuCifrePrimeDinLista([1,11,13]) is False
    assert numereCuCifrePrimeDinLista([121,33,74]) is False
    assert numereCuCifrePrimeDinLista([3,5,7,]) is True
def SubsecventaMaxElementeCifrePrime(l):
    '''
    determina cea mai lunga subsecventa de nr. cu cifre prime
    :param l: lista de nr. intregi
    :return: cea mai lunga subsecventa de nr. cu cifre prime din l
    '''
    SubsecventaMax = []
    for i in range(len(l)):
        for j in range(i, len(l)):
            if numereCuCifrePrimeDinLista(l[i:j + 1]) and len(l[i:j + 1]) > len(SubsecventaMax):
                SubsecventaMax = l[i:j + 1]
    return SubsecventaMax
def testSubsecventaMaxElementeCifrePrime():
    assert SubsecventaMaxElementeCifrePrime([33,35,75]) == [33,35,75]
    assert SubsecventaMaxElementeCifrePrime([10,12,8]) == []
    assert SubsecventaMaxElementeCifrePrime([]) == []
    assert SubsecventaMaxElementeCifrePrime([10,11,55,35]) == [55,35]
    assert SubsecventaMaxElementeCifrePrime([10,55,35,10]) == [55,35,]
def toateElementeleNumereDivizibileCuK(l,k):
    '''
    Verifica daca toate elem. din lista sunt divizibile cu un nr. k citi de la tastatura
    :param k: numarul citit de la tastatura
    :param l: lista de numere intregi
    :return: True daca toata elem din lista sunt div. cu k sau False daca nu
    '''
    for x in l:
        if x % k != 0:
            return False
    return True
def test_toateElementeleNumereDivizibileCuK():
    assert toateElementeleNumereDivizibileCuK([12,14,16],2) is True
    assert toateElementeleNumereDivizibileCuK([10,11,13],3) is False
    assert toateElementeleNumereDivizibileCuK([13,10,12],2) is False
    assert toateElementeleNumereDivizibileCuK([12,16,64],4) is True
    assert toateElementeleNumereDivizibileCuK([],100) is True
def SubsecventatoateElementeleNumereDivizibileCuK(l, k):
    SubsecventaMax = []
    for i in range(len(l)):
        for j in range(i, len(l)):
            if toateElementeleNumereDivizibileCuK(l[i:j + 1], k) and len(l[i:j + 1]) > len(SubsecventaMax):
                SubsecventaMax = l[i:j + 1]
    return SubsecventaMax
def test_SubsecventatoateElementeleNumereDivizibileCuK():
    assert SubsecventatoateElementeleNumereDivizibileCuK([10,12],2) == [10,12]
    assert SubsecventatoateElementeleNumereDivizibileCuK([9,11],2) == []
    assert SubsecventatoateElementeleNumereDivizibileCuK([9,8,12,15],3) == [12,15]
def main():
    testToateElementelePalindroame()
    testSubsecventaMaxElementePalindroame()
    testNumereCuCIfrePrimeDinLista()
    testSubsecventaMaxElementeCifrePrime()
    test_toateElementeleNumereDivizibileCuK()
    test_SubsecventatoateElementeleNumereDivizibileCuK()
    l = []
    while True:
        printMenu()
        optiune = input("Da-ti optiunea: ")
        if optiune == "1":
            l=citireLista()
        elif optiune == "2":
            print(SubsecventaMaxElementePalindroame(l))
        elif optiune == "3":
            print(SubsecventaMaxElementeCifrePrime(l))
        elif optiune == "4":
            k = int(input("Divizor= "))
            print(SubsecventatoateElementeleNumereDivizibileCuK(l, k))
        elif optiune == "x":
            break
        else:
            print("Optiune gresita, reincearca")
main()