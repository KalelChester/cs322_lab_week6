import pytest
from bank import Account

def test_initial_balance():
    # Test that the initial balance is set correctly
    account = Account("Testing_User", 0)
    assert account.get_balance() == 0, "Initial balance: $0.00"

def test_deposit():
    account = Account("Testing_User", 0)
    account.deposit(10)
    assert account.get_balance() == 10, "Balance after deposit: $10.00"

def test_withdraw():
    # Test that withdrawing a valid amount updates the balance correctly
    account = Account("Testing_User", 10)
    account.withdraw(5)
    assert account.get_balance() == 5, "Balance after withdrawal: $5.00"

def test_deposit_negative_amount():
    account = Account("Testing_User", 5)
    with pytest.raises(ValueError, match="Deposit amount must be positive"):
        account.deposit(-5)

def test_withdraw_more_than_balance():
    account = Account("Testing_User", 5)
    with pytest.raises(ValueError, match="Insufficient funds"):
        account.withdraw(10)

def test_withdraw_negative_amount():
    account = Account("Testing_User", 5)
    with pytest.raises(ValueError, match="Withdrawal amount must be positive"):
        account.withdraw(-10)