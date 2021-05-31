import pytest
from brownie import config

@pytest.fixture
def usdt(interface):
    yield interface.USDT('0xdAC17F958D2ee523a2206206994597C13D831ec7')


@pytest.fixture
def usdt_whale(accounts):
    # binance8
    yield accounts.at('0x47ac0fb4f2d84898e4d9e7b4dab3c24507a6d503', force=True)

@pytest.fixture
def vpomo(accounts):
    yield accounts.at('0x5a8C89E24417ee83F1b5B07a1608F7C0eF12E6E2', force=True)

@pytest.fixture
def vpomo_two(accounts):
    yield accounts.at('0x661a3b8a02E70e3b4E0623C3673e78F0C6A202DD', force=True)

@pytest.fixture
def vpomo_three(accounts):
    yield accounts.at('0xC6209690b79DDB25d12EE7eD659B705eB6607879', force=True)

@pytest.fixture
def weth_whale(accounts):
    yield accounts.at('0x2f0b23f53734252bda2277357e97e1517d6b042a', force=True)
