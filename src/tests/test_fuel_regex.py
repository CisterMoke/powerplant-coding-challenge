import pytest

import re
from src.utils.regex import fuel_pattern

def test_fuel_regex():
    keys = [
        'gas(euro/MWh)',
        'kerosine(euro/MWh)',
        'co2(euro/ton)',
        'wind(%)'
    ]
    splits = [
        ('gas', 'euro/MWh'),
        ('kerosine', 'euro/MWh'),
        ('co2', 'euro/ton'),
        ('wind', '%')
    ]

    for key, split in zip(keys, splits):
        match = re.match(fuel_pattern, key)
        assert match.groups() == split