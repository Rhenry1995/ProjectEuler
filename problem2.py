# Even Fibonacci numbers
import time

def main():
    f = [1, 2]
    fn = 0
    sum = 2

    while fn <= 4000000:
        fn = f[-1] + f[- 2]
        fnList = [fn]
        f.extend(fnList)

        if fn%2 == 0 and fn < 4000000:
            sum += fn
    return(sum)


if __name__ == '__main__':
    t = time.time()
    ans = main()
    eclipsed = time.time() - t
    print('%d was calculated in %.8f seconds' % (ans, eclipsed))
