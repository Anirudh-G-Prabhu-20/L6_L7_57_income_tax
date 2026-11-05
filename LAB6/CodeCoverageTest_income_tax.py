
import pytest
from income_tax import taxable_income, tax_due, refund_status


# Taxable income tests

def test_new_regime():
    assert taxable_income(1000000, "new", 0) == 925000


def test_old_regime():
    assert taxable_income(1000000, "old", 100000) == 850000


def test_old_regime_investment_cap():
    assert taxable_income(1000000, "old", 200000) == 800000


def test_negative_gross_income():
    with pytest.raises(ValueError, match="invalid income"):
        taxable_income(-1000, "new", 0)


def test_unknown_regime():
    with pytest.raises(ValueError, match="unknown regime"):
        taxable_income(100000, "invalid", 0)


def test_taxable_income_below_zero():
    assert taxable_income(10000, "new", 0) == 0


def test_taxable_income_positive():
    assert taxable_income(200000, "new", 0) == 125000


# Tax calculation tests

def test_negative_taxable_amount():
    with pytest.raises(ValueError, match="invalid amount"):
        tax_due(-100, 30)


def test_age_below_60_exemption():
    assert tax_due(200000, 30) == 0


def test_age_60_exemption():
    assert tax_due(300000, 65) == 0


def test_age_80_exemption():
    assert tax_due(500000, 85) == 0


def test_first_tax_slab():
    assert tax_due(400000, 30) == 7500


def test_higher_tax_slab():
    assert tax_due(600000, 30) == 32500


# Refund and payment status tests

def test_refund_on_time():
    assert refund_status(50000, 40000, True) == "refund"


def test_refund_late():
    assert refund_status(50000, 40000, False) == "refund delayed"


def test_balance_on_time():
    assert refund_status(30000, 40000, True) == "pay balance"


def test_balance_late():
    assert refund_status(30000, 40000, False) == "pay balance with penalty"


def test_settled():
    assert refund_status(40000, 40000, True) == "settled"
