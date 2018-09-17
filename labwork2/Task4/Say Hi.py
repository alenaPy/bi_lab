"""In this mission you should write a function that introduce a person with a given parameters in attributes.

Input: Two arguments. String and positive integer.

Output: String."""


def say_hi(name: str, age: int) -> str:
    """Define the function."""
    return "Hi. My name is {} and I'm {} years old".format(name, str(age))
