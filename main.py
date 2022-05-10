#!/usr/bin/env python

import pandas as pd
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--infile', type=argparse.FileType('r', encoding='UTF-8'),
                    required=False)
args = parser.parse_args()
print("Entering main.py")


def divide_chunks(lst, number):
    for i in range(0, len(lst), number):
        yield lst[i:i + number]


df = pd.read_excel(args.infile.name, header=None, names=['szamok'])
n = 30
devi = list(divide_chunks(list(df.szamok), n))

new_df = pd.DataFrame(devi).transpose()

new_df.to_excel('test_end.xlsx')
