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
    
    # for key in hmap.keys():
    #     print(key)

    # for val in hmap.values():
    #     print(val)

    # for k, v in hmap.items():
    #     print(k, v)

    hmap.remove(10)
    print(hmap.get(10))
    hmap.remove(10)


if __name__ == "__main__":
    main()
