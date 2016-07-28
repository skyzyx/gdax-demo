# Simple BTC calculation demo

Leverages the [Coinbase Global Digital Asset Exchange (GDAX)](https://www.gdax.com) digital currency exchange.

## Requirements

* Python 2.7+, 3.5+
* Pip
* VirtualEnv is recommended, but not required

## Installation

```bash
# If you have VirtualEnv installed...
virtualenv .vendor
source .vendor/bin/activate

# Everybody
pip install -r requirements.txt
```

## Usage

```
./gdax.py -h

./gdax.py 1.0
```

## Parameters

* GDAX data is sorted by ascending price per BTC.
* You can purchase a partial offering from a seller.
* You want to purchase BTC at the lowest possible price, USD.
* Input: BTC quantity
* Output: USD cost

## Logic

Since the data is pre-sorted, we can skip the sorting step.

We want to take the amount of BTC desired as the upper limit. We start at the beginning, loop over the data in sequence, and collect as much BTC as we can (calculating the price along the way) until we add the _penultimate_ value.

For the final value (i.e., value remaining), we only want to take a portion of the next value. We can subtract the remaining desired from what is available, calculate that cost, and add these values to the data we've already collected.

It's simple arithmetic. :+1:

## Known Issues

* Cost calculation does not currently do any rounding or "to fixed" for currency calculations.
* Does not handle API timeouts or 500s gracefully.

## Future Improvements

* Allow USD cost as an input (e.g., $100), and the amount of BTC as an output (e.g., 0.15224176 BTC @ $656.85/BTC).
