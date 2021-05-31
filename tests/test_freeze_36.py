from brownie import Wei, reverts
import brownie
import time

def test_freeze(FreezeTokens, accounts, interface, usdt, usdt_whale, chain):
    print('='*20 + ' running ... ' + '='*20)
    decimal = 1e6
    MONTHS = 60*60*24*30*36

    amount = 1000*decimal

    my_contract_freeze = FreezeTokens.deploy(accounts[0], usdt, {'from': accounts[0]})
    print('FreezeTokens address', my_contract_freeze)

    usdt.transfer(accounts[0], 100*amount, {'from': usdt_whale})

    print('token for my_contract_freeze', my_contract_freeze.token())

    print('balance USDT of accounts[0]', usdt.balanceOf(accounts[0])/decimal)

    usdt.approve(my_contract_freeze, 10000000*amount, {'from': accounts[0]})
    print('allowance USDT of accounts[0]', usdt.allowance(accounts[0], my_contract_freeze)/decimal)

    my_contract_freeze.freeze(amount, {'from': accounts[0]})
    print('balance USDT of my_contract_freeze', usdt.balanceOf(my_contract_freeze)/decimal)

    print('balanceFreezeTokens', my_contract_freeze.balanceFreezeTokens()/decimal)
    print('isProcessedFreeze', my_contract_freeze.isProcessedFreeze())

    print('getCurrentDate', my_contract_freeze.getCurrentDate())
    seek = MONTHS - 60*60*24
    my_contract_freeze.setSeek(seek, {'from': accounts[0]})

    print('checkUnFreezeAmount', my_contract_freeze.checkUnFreezeAmount()/decimal)

    seek = MONTHS*50 + 100
    my_contract_freeze.setSeek(seek, {'from': accounts[0]})
    print('checkUnFreezeAmount', my_contract_freeze.checkUnFreezeAmount()/decimal)

