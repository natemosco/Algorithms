#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    limiting_area = 10000000000000
    for key in recipe:
        if ingredients.get(key) is None:
            limiting_area = 0
            return limiting_area
        elif ingredients[key] // recipe[key] < limiting_area:
            limiting_area = ingredients[key] // recipe[key]
    return limiting_area


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
