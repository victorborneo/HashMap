from HashMap import HashMap
import random
import time


def main():
    hmap = HashMap()
    default_hmap = {}

    for i in range(1_000_000):
        num = random.randint(1, 1_000_000)
        default_hmap[i] = num
        hmap.add(i, num)
    
    x = []
    start = time.perf_counter()
    for i in range(1_000_000):
        x.append(default_hmap.get(i))
    print(time.perf_counter() - start)

    y = []
    start = time.perf_counter()
    for i in range(1_000_000):
        y.append(hmap.get(i))
    print(time.perf_counter() - start)

    print(x==y)


if __name__ == "__main__":
    main()
