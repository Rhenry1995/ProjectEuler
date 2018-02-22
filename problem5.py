#smallest multiple
import time

arr = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

def main():
    for i in range(2520, 999999999999, 2520):
        if all(i%n ==0 for n in arr):
            return i


if __name__ == '__main__':
    t = time.time()
    ans = main()
    eclipsed = time.time() - t
    print('%d was calculated in %.8f seconds' % (ans, eclipsed))
