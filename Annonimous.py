import hashlib
from random import randrange, random
import random
def randprime(N=10**40):
    p = 1
    while not is_prime(p):
        p = randrange(N)
    return p
def is_prime(n, k=6):
    from random import randint
    if n < 2: return False
    for p in [2,3,5,7,11,13,17,19,23,29]:
        if n % p == 0: return n == p
    s, d = 0, n-1
    while d % 2 == 0:
        s, d = s+1, d//2
    for i in range(k):
        x = pow(randint(2, n-1), d, n)
        if x == 1 or x == n-1: continue
        for r in range(1, s):
            x = (x * x) % n
            if x == 1: return False
            if x == n-1: break
        else: return False
    return True

def hash_function(s_tr):
    return hashlib.sha256(s_tr.encode()).hexdigest()


def hex_2_int(s_tr):
    return int(s_tr, 16)


def xor_function(a, b):
    return a ^ b


D = []
P = []
R = []
r_bar = []
q = []
if __name__ == '__main__':
    numberOfItems = int(input("enter the number of items in the list : "))
    for i in range(numberOfItems):
        d = randprime(2 ** 20)
        D.append(d)
    print("This is the ID list that Clint sneds to Server", D)
    d = int(input("enter your ID :  "))
    for j in range(numberOfItems) :
        if D[j] == d :
            print("my ID : ",D[j])
            myID = D[j]
            positions = j
            break
    for k in range(numberOfItems):
        p = randrange(2**20)
        P.append(p)
    print("This is passward list for corresponding IDs",P)
    for rs in range(numberOfItems):
        word = str(randprime(2 ** 20))
        R.append(int(word))
    print("This is the random string ",R)
    for i in range(numberOfItems):
        temp = hash_function(str(P[i]))
        temp_2 = hex_2_int(temp)
        xor = xor_function(temp_2, R[i])
        q.append(xor)
        r_hash = hash_function(str(R[i]))
        r_bar.append(r_hash)
    b = int(input(" press 1 if you want to send the hashed r and b bar to the clint"))
    if b==1:
        print("Client id:", D[positions])
        print("Client Password", P[positions])
        print("this is the list of P that is send to the clint ", q)
        print("this is the list of r bar that is send to the clint ", r_bar)

        p_prime_bar = hash_function(str(P[positions]))
        int_p_prime_bar = hex_2_int(p_prime_bar)
        r_prime = xor_function(q[positions], int_p_prime_bar)
        r_prime_bar = hash_function(str(r_prime))

        print("This is the value of r bar ", r_bar[positions])
        print("This is the value of r prime ber", r_prime_bar)

        if r_bar[positions] == r_prime_bar:
            print("-------------------------------------------------------")
            print("The voter is ready to send r prime to the server")
            print("-------------------------------------------------------")

        else:
            print("-------------------------------------------------------")
            print("The clint is not ready to send the document to server ")
            print("-------------------------------------------------------")
    else :
        print(" Thank you ")
    print("the value of r prime ",r_prime)
    print("the value of R for the voter",R[positions])
    k = int (input("enter 1 if you want to send the document to q"))
    if k == 1 :
        if r_prime == R[positions]:
            print("-------------------------------------------------------")
            print("the voter is authenticated")
            print("-------------------------------------------------------")
        else:
            print("-------------------------------------------------------")
            print("the voter is not authenticated")
            print("-------------------------------------------------------")
    else :
        print("thank you ")

