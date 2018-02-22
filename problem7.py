# 10001 first
import time

def isPrime(n):
    if n == 2: return(True)
    if n % 2 == 0 or n<2: return(False)
    for i in range(3, int(n**0.5)+1,2):
        if n%i==0:
            return(False)
    return(True)


def main():
    n = 0
    i = 0
    while i<10001:
        n +=1
        if isPrime(n):
            i += 1

    return n

if __name__ == '__main__':
    t = time.time()
    ans = main()
    eclipsed = time.time() - t
    print("%s calcilated in %.8f seconds"%(ans, eclipsed))
