

def suma(args):
    """

    :param args:
    :return: sum of args
    """

    return sum(args)


def mean(args):
    N = len(args)
    m = sum(args) / N
    return m


def min_max(args):
    mini = min(args)
    maxi = max(args)
    return mini, maxi
