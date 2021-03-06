from functools import wraps


def type_logger(level=0):

    def logger(func):

        @wraps(func)
        def decor(*argv, **kwargs):

            all_args = list(argv) + list(kwargs.values())
            norm_res = func(all_args[0])

            if level == 1:
                print(", ".join([f"{x}:{type(x)}" for x in all_args]))
            elif level == 2:
                print(f"{func.__name__}:{type(func)}")
                print(f"{func.__name__}({all_args[0]}):{type(norm_res)}")

            return norm_res

        return decor

    return logger


@type_logger(2)
def calc_cube(x):
    """ cube of args """
    return x ** 3


if __name__ == "__main__":
    a = calc_cube(5, 6, 7, 8, 9, 1, 2, 3, val1=4, val2=5)
    print(a)