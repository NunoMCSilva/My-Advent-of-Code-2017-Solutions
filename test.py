#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import solutions


def main():
    parser = argparse.ArgumentParser(description='Run solution.')
    parser.add_argument('day', metavar='N', type=int, choices=range(1, 25+1))

    args = parser.parse_args()
    solutions.test(args.day)


if __name__ == '__main__':
    main()
