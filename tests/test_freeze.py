from brownie import Wei, reverts
import brownie
import time

def test_freeze(FreezeTokens, accounts, interface, usdt, usdt_whale, chain):
    print('='*20 + ' running ... ' + '='*20)
    decimal = 1e6
    FOUR_MONTHS = 60*60*24*120
    ONE_WEEK = 60*60*24*7

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
    seek = FOUR_MONTHS + ONE_WEEK + 100
    my_contract_freeze.setSeek(seek, {'from': accounts[0]})

    print('checkUnFreezeAmount', my_contract_freeze.checkUnFreezeAmount()/decimal)

    seek = FOUR_MONTHS + ONE_WEEK*50 + 100
    my_contract_freeze.setSeek(seek, {'from': accounts[0]})
    print('checkUnFreezeAmount', my_contract_freeze.checkUnFreezeAmount()/decimal)

    seek = FOUR_MONTHS + ONE_WEEK*60 + 100
    my_contract_freeze.setSeek(seek, {'from': accounts[0]})
    print('checkUnFreezeAmount', my_contract_freeze.checkUnFreezeAmount()/decimal)

    seek = FOUR_MONTHS + ONE_WEEK*2 + 100
    my_contract_freeze.setSeek(seek, {'from': accounts[0]})
    print('checkUnFreezeAmount', my_contract_freeze.checkUnFreezeAmount()/decimal)

    my_contract_freeze.unFreeze(my_contract_freeze.checkUnFreezeAmount(), {'from': accounts[0]})
    print('checkUnFreezeAmount', my_contract_freeze.checkUnFreezeAmount()/decimal)

    print('balance USDT of my_contract_freeze', usdt.balanceOf(my_contract_freeze)/decimal)
    print('balance USDT of accounts[0]', usdt.balanceOf(accounts[0])/decimal)

    seek = FOUR_MONTHS + ONE_WEEK*3 + 100
    my_contract_freeze.setSeek(seek, {'from': accounts[0]})
    print('checkUnFreezeAmount', my_contract_freeze.checkUnFreezeAmount()/decimal)

    seek = FOUR_MONTHS + ONE_WEEK*49 + 100
    my_contract_freeze.setSeek(seek, {'from': accounts[0]})
    val = my_contract_freeze.checkUnFreezeAmount()
    print('checkUnFreezeAmount', my_contract_freeze.checkUnFreezeAmount()/decimal)
    my_contract_freeze.unFreeze(val, {'from': accounts[0]})
    print('checkUnFreezeAmount', my_contract_freeze.checkUnFreezeAmount()/decimal)
    print('balance USDT of my_contract_freeze', usdt.balanceOf(my_contract_freeze)/decimal)

    seek = FOUR_MONTHS + ONE_WEEK*50 + 100
    my_contract_freeze.setSeek(seek, {'from': accounts[0]})
    print('checkUnFreezeAmount', my_contract_freeze.checkUnFreezeAmount()/decimal)


