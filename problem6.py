# Sum square difference
import time

def main(n):
    sumOfSquare = 0
    squareOfSum =0
    for i in range (1,n):
        squareOfSum += i
        sumOfSquare += (i**2)
    squareOfSum = squareOfSum ** 2
    return(squareOfSum - sumOfSquare)

if __name__ == '__main__':
    t = time.time()
    ans = main(100)
    eclipsed = time.time() - t
    print("%s calcilated in %.8f seconds"%(ans, eclipsed))
