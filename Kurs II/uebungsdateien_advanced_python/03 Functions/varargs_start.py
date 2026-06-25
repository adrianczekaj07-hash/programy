# Demonstrate the use of variable argument lists


# TODO: define a function that takes variable arguments
def addition(*args):
    result = 0
    for arg in args:
        result += arg
    return result



def main():
    # TODO: pass different arguments
    print(addition(13, 14, 17, 33, 35))

    # TODO: pass an existing list
    list1 = [13,14,17,33,35]
    print(addition(*list1))


if __name__ == "__main__":
    main()
