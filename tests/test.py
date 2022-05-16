#!/usr/bin/env python3
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from unittest.mock import patch
import unittest

from utils import main
from utils import config



@patch(
    "utils.config.config",
    {
        "arbitrum_web3_provider": os.environ.get("ARBITRUM_ENDPOINT"),
        "avalanche_web3_provider": os.environ.get("AVALANCHE_ENDPOINT"),
        "binance_web3_provider": os.environ.get("BINANCE_ENDPOINT"),
        "fantom_web3_provider": os.environ.get("FANTOM_ENDPOINT"),
        "optimism_web3_provider": os.environ.get("OPTIMISM_ENDPOINT"),
        "polygon_web3_provider": os.environ.get("POLYGON_ENDPOINT"),
        "web3_provider": os.environ.get("WEB3_PROVIDER"),
        "ipfs_gateway": os.environ.get("IPFS_GATEWAY"),
        "opensea_api_key":os.environ.get("opensea_api_key"),
        "moralis_api_key":os.environ.get("moralis_api_key")
    },
)
class TestUtils(unittest.TestCase):
    def test_utils(self):
        self.assertIsInstance(main.hello(), str)
        self.assertEqual(main.hello(), "GM World!")

    def test_config(self):
        print(config.config)



if __name__ == "__main__":  # pragma: no cover
    unittest.main()
