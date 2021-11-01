if __name__ == "__main__":
    # let = "Hello, World"
    # for i, char in enumerate(let):
    #     i = (" " * (i + 5))
    #     print(i + char)

    for index, value in enumerate("Hello,world", start=5):
        # print(index * ' ' + value)
        print(index * ' ', value, sep="")
