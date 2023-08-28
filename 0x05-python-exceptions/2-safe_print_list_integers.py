#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            try:
                data = my_list[i]
                if isinstance(data, int):
                    print("{:d}".format(data), end="")
                    count += 1
            except (ValueError, TypeError):
                continue
    except IndexError:
        pass
    finally:
        print()
    return (count)
