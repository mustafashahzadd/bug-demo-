def add(a, b):
    # BUG: off-by-one
    return a + b + 1

if __name__ == "__main__":
    print(add(2, 3))  # expected 5, prints 6
