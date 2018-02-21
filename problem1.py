import time


def main():
    sumOf = 0
    for i in range(1,1000):
        if i%3 == 0:
            sumOf = sumOf + i
        elif i%5 == 0:
            sumOf = sumOf + i

    return(sumOf)


if __name__ == '__main__':
    t = time.time()
    ans = main()
    eclipsed = time.time() - t
    print('%d was calculated in %.8f seconds' % (ans, eclipsed))
