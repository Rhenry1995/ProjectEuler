#palandrome product
import time

def is_palandrome(numString):
    for k, char in enumerate(numString):
        if char != numString[-k-1]:
            return False
    return True

def main():
    palandrome= 0
    for i in range(1,999):
        for j in range(1,999):
            product = i * j
            numString = str(product)
            if is_palandrome(numString):
                if product > palandrome:
                    palandrome = product
    return(palandrome)


if __name__ == '__main__':
    t = time.time()
    ans = main()
    eclipsed = time.time() - t
    print('%d was calculated in %.8f seconds' % (ans, eclipsed))
