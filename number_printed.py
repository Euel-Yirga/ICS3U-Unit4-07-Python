#!/usr/bin/env python3

# Created by: Euel Yirga
# Created on: October 2019
# prints 5 integers per line
# from 1000 to 2000


def main():
    counter = 0

    for numbers in range(1000, 2001):
        counter += 1
        print(numbers, end = (" " if counter < 5 else "\n"))

        if counter == 5:
            counter = 0


if __name__ == "__main__":
    main()
