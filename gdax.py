#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import argparse
import json
import requests
from pprint import pprint

# Reading from the file system
# with open('gdax.json') as data_file:
#     data = json.loads(data_file.read())

# Reading from the API
r = requests.get('https://api.gdax.com/products/BTC-USD/book?level=3')
data = r.json()

parser = argparse.ArgumentParser(description='Calculate BTC stuff.')
parser.add_argument('btc', type=float, help='Amount of BTC to purchase.')
args = parser.parse_args()

amount_of_btc = 0
cost_of_btc = 0

for (i, ask) in enumerate(data['asks']):
    [cost, available, uuid] = ask

    cost = float(cost)
    available = float(available)

    while (amount_of_btc < args.btc):
        if (amount_of_btc + available <= args.btc):
            amount_of_btc += available
            cost_of_btc += (cost * available)
        else:
            remaining = args.btc - amount_of_btc
            next_cost = float(data['asks'][i][0])
            next_available = float(data['asks'][i][1])

            amount_of_btc += remaining
            cost_of_btc += (next_cost * remaining)
            break

print ('BTC requested: {}'.format(args.btc))
print ('BTC purchased: {}'.format(amount_of_btc))
print ('BTC cost:      {}'.format(cost_of_btc))
