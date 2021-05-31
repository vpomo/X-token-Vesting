from brownie import Wei, reverts
import brownie
import time

def test_token_xtkn(BEP20TokenXTKN, accounts, interface):
    print('='*20 + ' running ... ' + '='*20)
    decimal = 1e8

    my_contract = BEP20TokenXTKN.deploy(accounts[0], {'from': accounts[0]})
    amount = 100*decimal

    print('balance XTKN of accounts[0]', my_contract.balanceOf(accounts[0])/decimal)
    my_contract.approve(my_contract, 1000000000000*amount, {'from': accounts[0]})

#    arrAddress = [accounts[2], accounts[3], accounts[4], accounts[5], accounts[6], accounts[2], accounts[3], accounts[4], accounts[5], accounts[6], accounts[2], accounts[3], accounts[4], accounts[5], accounts[6], accounts[2], accounts[3], accounts[4], accounts[5], accounts[6]]
#    arrAmount = [amount*10, amount*20, amount*30, amount*40, amount*50, amount*10, amount*20, amount*30, amount*40, amount*50, amount*10, amount*20, amount*30, amount*40, amount*50, amount*10, amount*20, amount*30, amount*40, amount*50]

    arrAddress = [accounts[2], accounts[3], accounts[4], accounts[5], accounts[6], accounts[2], accounts[3], accounts[4], accounts[5], accounts[6], accounts[2], accounts[3], accounts[4], accounts[5], accounts[6], accounts[2], accounts[3], accounts[4], accounts[5], accounts[6], accounts[2], accounts[3], accounts[4], accounts[5], accounts[6], accounts[2], accounts[3], accounts[4], accounts[5], accounts[6], accounts[2], accounts[3], accounts[4], accounts[5], accounts[6], accounts[2], accounts[3], accounts[4], accounts[5], accounts[6], accounts[2], accounts[3], accounts[4], accounts[5], accounts[6], accounts[2], accounts[3], accounts[4], accounts[5], accounts[6], accounts[2], accounts[3], accounts[4], accounts[5], accounts[6], accounts[2], accounts[3], accounts[4], accounts[5], accounts[6], accounts[2], accounts[3], accounts[4], accounts[5], accounts[6], accounts[2], accounts[3], accounts[4], accounts[5], accounts[6], accounts[2], accounts[3], accounts[4], accounts[5], accounts[6], accounts[2], accounts[3], accounts[4], accounts[5], accounts[6],accounts[2], accounts[3], accounts[4], accounts[5], accounts[6], accounts[2], accounts[3], accounts[4], accounts[5], accounts[6], accounts[2], accounts[3], accounts[4], accounts[5], accounts[6], accounts[2], accounts[3], accounts[4], accounts[5], accounts[6]]
    arrAmount = [amount*10, amount*20, amount*30, amount*40, amount*50, amount*10, amount*20, amount*30, amount*40, amount*50, amount*10, amount*20, amount*30, amount*40, amount*50, amount*10, amount*20, amount*30, amount*40, amount*50, amount*10, amount*20, amount*30, amount*40, amount*50, amount*10, amount*20, amount*30, amount*40, amount*50, amount*10, amount*20, amount*30, amount*40, amount*50, amount*10, amount*20, amount*30, amount*40, amount*50,amount*10, amount*20, amount*30, amount*40, amount*50, amount*10, amount*20, amount*30, amount*40, amount*50, amount*10, amount*20, amount*30, amount*40, amount*50, amount*10, amount*20, amount*30, amount*40, amount*50, amount*10, amount*20, amount*30, amount*40, amount*50, amount*10, amount*20, amount*30, amount*40, amount*50, amount*10, amount*20, amount*30, amount*40, amount*50, amount*10, amount*20, amount*30, amount*40, amount*50, amount*10, amount*20, amount*30, amount*40, amount*50, amount*10, amount*20, amount*30, amount*40, amount*50, amount*10, amount*20, amount*30, amount*40, amount*50, amount*10, amount*20, amount*30, amount*40, amount*50]

#    tx = my_contract.batchTransfer(arrAddress, arrAmount, {'from': accounts[0]})
#    print('tranza', tx.info())

    print('balance XTKN of accounts[2]', my_contract.balanceOf(accounts[2])/decimal)
    print('balance XTKN of accounts[3]', my_contract.balanceOf(accounts[3])/decimal)

    print('balance XTKN of accounts[0]', my_contract.balanceOf(accounts[0])/decimal)



