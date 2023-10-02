import math
import constants


def main():
    # input
    TAU = constants.TAU
    r = float(input("Radius: "))
    # process
    circumfrence = TAU * r

    # output
    print("")
    print("circumfrence = {} cm".format(circumfrence))


if __name__ == "__main__":
    main()
