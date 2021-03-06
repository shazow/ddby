import unittest

from ddby import Money, Currency, get_currency

class TestMoney(unittest.TestCase):

    def test_creating_money_with_currency_code_finds_currency(self):
        m = Money(500, 'USD')

        assert isinstance(m.currency, Currency)

    def test_creating_money_with_currency_object_uses_currency(self):
        currency = get_currency('USD')
        m = Money(500, currency)

        assert m.currency == currency

    def test_passing_float_stores_as_int(self):
        initial = 25.0
        expected = 2500

        m = Money(initial, 'USD')
        assert m.amount == expected

    def test_passing_int_uses_exact(self):
        initial = 2500
        expected = 2500

        m = Money(initial, 'USD')
        assert m.amount == expected

    def test_using_currency_without_precision_int(self):
        amount = 2500
        expected = 2500

        # Yen has no fractional amounts
        m = Money(amount, 'JPY')

        assert m.amount == expected

    def test_using_currency_without_precision_float(self):
        amount = 2500.0
        expected = 2500
        m = Money(amount, 'JPY')

        assert m.amount == expected

    def test_presence_of_value_equates_to_true(self):
        m = Money(100, 'USD')
        assert m

    def test_absence_of_value_equates_to_false(self):
        m = Money(0, 'USD')
        assert not m

    def test_adding_two_currencies_returns_total_amount(self):
        m1 = Money(100, 'USD')
        m2 = Money(200, 'USD')
        expected = Money(300, 'USD')

        actual = m1 + m2
        assert actual == expected

    def test_subtracting_two_currencies_returns_total_amount(self):
        m1 = Money(100, 'USD')
        m2 = Money(300, 'USD')
        expected = Money(200, 'USD')

        actual = m2 - m1
        assert actual == expected

if __name__ == '__main__':
    unittest.main()
