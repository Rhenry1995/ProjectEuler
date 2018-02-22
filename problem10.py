# Summaniation of primes
import time

def isPrime(n):
    if n == 2: return(True)
    if n % 2 == 0 or n<2: return(False)
    for i in range(3, int(n**0.5)+1,2):
        if n%i==0:
            return(False)
    return(True)


def main():
    Summaniation = 0
    for i in range(1,2000000):
        if isPrime(i): Summaniation += i
    return(Summaniation)

if __name__ == '__main__':
    t = time.time()
    ans = main()
    eclipsed = time.time() - t
    print("%d calcilated in %.8f seconds"%(ans, eclipsed))
