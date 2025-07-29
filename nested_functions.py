def count():
    count = 5

    def increment():
        nonlocal count
        count = count + 1
        print(count)

    increment()

count()