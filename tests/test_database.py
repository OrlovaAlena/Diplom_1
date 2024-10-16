from typing import List

from src.database import Database


class TestDataBase:

    def test_get_available_buns(self):
        db = Database()
        buns = db.available_buns()

        assert db.buns == buns
        assert len(buns) == 3
        assert db.buns[0] in buns

    def test_get_available_ingredients(self):
        db = Database()
        ingredients = db.available_ingredients()

        assert db.ingredients == ingredients
        assert len(ingredients) == 6
        assert db.ingredients[0] in ingredients
