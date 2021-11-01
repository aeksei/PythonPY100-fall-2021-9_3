


if __name__ == "__main__":
    cart = {
        "apple": 80,
        "orange": 65,
        "banana": 40,
    }

    sum_ = 0
    for fruit in cart:
        print(cart[fruit])  # получаем значение по ключу
        sum_ += cart[fruit]
    print(sum_)

    print(sum(cart.values()))

    numbers = {i: i ** 2 for i in range(10)}
    cart["new_key"] = "new_value"
