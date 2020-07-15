#!/usr/bin/env python3
import unittest
from fluent import fluent


class TestExample(unittest.TestCase):
    def test_dog_example(self):
        @fluent(arg="color", func_name="with_color")
        @fluent(arg="long_ears", func_name="with_long_ears", default_value=True)
        @fluent(arg="long_ears", func_name="with_short_ears", default_value=False)
        def new_dog(name: str, long_ears: bool, color: str) -> str:
            length = "long" if long_ears else "short"
            return f"I am a dog named {name} with {length} ears, and my fur is {color}"

        self.assertEqual(
            "I am a dog named Brian with long ears, and my fur is brown",
            new_dog("Brian").with_long_ears().with_color("brown"),
        )

    def test_person(self):
        @fluent(arg="age")
        def new_person(name: str, age: int) -> str:
            return f"my name is {name}, and i am {age} years old."

        self.assertEqual(
            "my name is Casper, and i am 1337 years old.",
            new_person("Casper").with_age(1337),
        )


if __name__ == "__main__":
    unittest.main()
