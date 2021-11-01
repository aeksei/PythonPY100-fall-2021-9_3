def pow_func(base, pow_=2):
    # base ** pow_ -> реализовать через цикл while
    res = 1
    k = 1
    while k <= pow_:  # 1 * a * a * a ... * a
        res *= base
        k += 1

    return res


if __name__ == "__main__":
    a = 5
    n = 3

    print(pow_func(a, n))
