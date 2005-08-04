import sys

from read import read


def main(argv):
    print(read(argv[1]))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
# channel list argument
# output directory
