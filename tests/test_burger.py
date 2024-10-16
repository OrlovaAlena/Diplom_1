from unittest.mock import Mock

from praktikum_app.data import Data
from praktikum_app.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from src.bun import Bun
from src.burger import Burger
from src.ingredient import Ingredient


class TestBurger:
    def test_set_buns(self):
        burger = Burger()
        bun = Bun(Data.BUN_NAME, Data.BUN_PRICE)
        burger.set_buns(bun)

        assert burger.bun == bun

    def test_add_ingredient_to_the_list(self):
        burger = Burger()
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'Ананас', 66)
        burger.add_ingredient(ingredient)

        assert burger.ingredients[0] == ingredient

    def test_remove_ingredient_from_the_list(self):
        burger = Burger()
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, Data.SAUCE_NAME, Data.SAUCE_PRICE)
        burger.add_ingredient(ingredient)
        burger.remove_ingredient(0)

        assert burger.ingredients == []

    def test_move_ingredient_in_the_list(self):
        burger = Burger()
        first_ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, Data.SAUCE_NAME, Data.SAUCE_PRICE)
        second_ingredient = Ingredient(INGREDIENT_TYPE_FILLING, Data.FILLING_NAME, Data.FILLING_PRICE)
        burger.add_ingredient(first_ingredient)
        burger.add_ingredient(second_ingredient)
        burger.move_ingredient(0, 1)

        assert burger.ingredients[0] == second_ingredient

    def test_get_burger_price(self):
        burger = Burger()

        mock_bun = Mock()
        mock_bun.get_price.return_value = 50
        burger.set_buns(mock_bun)

        mock_first_ingredient = Mock()
        mock_first_ingredient.get_price.return_value = 60
        mock_second_ingredient = Mock()
        mock_second_ingredient.get_price.return_value = 40
        burger.add_ingredient(mock_first_ingredient)
        burger.add_ingredient(mock_second_ingredient)

        assert burger.get_price() == 200

    def test_get_burger_receipt(self):
        burger = Burger()

        mock_bun = Mock()
        mock_bun.get_price.return_value = Data.BUN_PRICE
        mock_bun.get_name.return_value = Data.BUN_NAME
        burger.set_buns(mock_bun)

        mock_sauce = Mock()
        mock_sauce.get_price.return_value = Data.SAUCE_PRICE
        mock_sauce.get_type.return_value = INGREDIENT_TYPE_SAUCE
        mock_sauce.get_name.return_value = Data.SAUCE_NAME
        burger.add_ingredient(mock_sauce)

        price = int(burger.get_receipt()[-3]+burger.get_receipt()[-2]+burger.get_receipt()[-1])

        assert INGREDIENT_TYPE_SAUCE.lower() in burger.get_receipt()
        assert Data.SAUCE_NAME in burger.get_receipt()
        assert Data.BUN_NAME in burger.get_receipt()

        assert price == Data.BUN_PRICE*2 + Data.SAUCE_PRICE
