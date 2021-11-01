




if __name__ == "__main__":
    # i = None
    # if i % 2 == 0:
    #     i = i ** 2
    # else:
    #     i = -i
    #
    # i = i ** 2 if i % 2 == 0 else -i
    list_ = [
        i ** 2 if i % 2 == 0 else -i
        for i in range(10)
    ]
    print(list_)



