# Special Pythagorean triplet
import math
import time

def main():
    for i in range(1, 500):
        for j in range(1,500):
            pyth = math.sqrt(i**2 + j**2)
            if  pyth % 1 == 0 and pyth + i + j ==1000:
                return(pyth*i*j)


if __name__ == '__main__':
    t = time.time()
    ans = main()
    eclipsed = time.time() - t
    print("%d calcilated in %.8f seconds"%(ans, eclipsed))
