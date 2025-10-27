def add(a, b):
    # BUG: off-by-one error fixed
    return a + b

if __name__ == "__main__":
    print(add(2, 3))  # Output now 5 ✅
