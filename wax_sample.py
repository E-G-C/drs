from dictwax import *
import json

from dictwax.waxes import DictBodyShop

source = {
        "a":      1,
        "b":      2,
        "c":      [
                {
                        "d0": 5,
                        "d1": 10,
                        "d2": 15
                        },
                {
                        "d4": 4,
                        "d5": 20,
                        "d6": 50
                        }
                ],
        "nested": {
                "e": 5,
                "f": "6",
                "g": {"k": 100, "l": 200, "m": 300}
                },
        "j":      [1, 2, 3, 4, 5, 6, 7, 8, 9]
        }

waxed_dict = {
        'a': WaxOn(1, RepWax({1: 2})),
        'b': WaxOn(2, RemWax([2])),
        'c': WaxOn(3, RepWax({3: 'Replaced'}))
        }

print('-' * 50)
print('Original'.center(50))
print('-' * 50)
#
print(json.dumps(source, indent=4))

print('-' * 50)
print('WipeOff Class'.center(50))
print('-' * 50)

DictBodyShop(source).wipe([100])
print(json.dumps(source, indent=4))

print('-' * 50)
print('Replacement'.center(50))
print('-' * 50)

DictBodyShop(source).replace({4: 40, 3: 30, 8: 80, 9: 90})
print(json.dumps(source, indent=4))

print('-' * 50)
print('Wax Off'.center(50))
print('-' * 50)
#


DictBodyShop(waxed_dict).wax_off()
print(json.dumps(waxed_dict, indent=4))

