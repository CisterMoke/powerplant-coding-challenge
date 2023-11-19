import os
import os.path as pth

from src.data_models.api import Payload
from src.data_models.fuel import FuelSupply


def test_payload_parsing():
    examples = pth.join(pth.dirname(__file__), '..', '..', 'example_payloads')
    for root, _, files in os.walk(examples):
        for filename in files:
            if not filename.startswith('payload'):
                continue
            with open(pth.join(root, filename), 'rb') as f:
                parsed = Payload.model_validate_json(f.read())
                assert isinstance(parsed, Payload)
                for f in parsed.get_fuels():
                    assert isinstance(f, FuelSupply)