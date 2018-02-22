# Largest prime factor
import time

def main(n):
    for i in range(2,100000):
        while n % i == 0:
            n //= i
            if n == 1 or n == i:
                return i

if __name__ == '__main__':
    t = time.time()
    ans = main(600851475143)
    eclipsed = time.time() - t
    print('%d was calculated in %.8f seconds' % (ans, eclipsed))
