import pytest
from evercraft.character import Character

class TestCharacter:
    def test_create(self):
        test_character = Character(None)
        assert test_character

    def test_name(self):
        # in this way the order of the parameters doesn't matters
        test_character = Character(in_name = "John")
        assert test_character.name == "John"
        test_character.name = "Walter"
        assert test_character.name == "Walter"

    def test_alignment(self):
        test_character = Character(None)
        assert test_character.alignment.lower() in ["good", "evil", "neutral"]

    def test_aligment_negative(self):
        '''negative test for the character object'''

        test_character = Character(None)
        with pytest.raises(ValueError):
            test_character.alignment = "whatever"
