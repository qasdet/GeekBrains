import time  # use for test
import sys  # use for test


def my_set(*argv):
    """ return unique elemts of argv """
    answ = set()

    for elem in argv:
        if not elem in answ:
            answ.add(elem)
        else:
            answ.remove(elem)

    #return (x for x in argv if x in answ)  # best
    return [x for x in argv if x in answ]  # better
    # return [ x for x in argv if argv.count(x) == 1 ] # worst
    # return [ x for i, x in enumerate(argv) if not x in [*argv[:i], *argv[i+1:]] ] # bad


if __name__ == "__main__":

    src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
    result = [23, 1, 3, 10, 4, 11]

    t = time.perf_counter()
    r = my_set(*src)

    print("mem: ", sys.getsizeof(r))
    print("time: ", time.perf_counter() - t)

    print(r == result)
    print(r)