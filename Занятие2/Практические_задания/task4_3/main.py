if __name__ == "__main__":
    rus_alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

    # for index, value in enumerate(rus_alphabet):  # TODO как за один раз получать пару индекс-значение?
    #     print(index, value)  # TODO как тогда должен выглядеть индекс?

    # for index, value in enumerate(rus_alphabet):  # TODO как за один раз получать пару индекс-значение?
    #     print(index + 1, value)

    for index, value in enumerate(rus_alphabet, start=100):  # TODO как за один раз получать пару индекс-значение?
        print(index, value)  # TODO как тогда должен выглядеть индекс?
