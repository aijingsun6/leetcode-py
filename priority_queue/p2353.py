## https://leetcode.cn/problems/design-a-food-rating-system/description/?envType=daily-question&envId=2025-02-28
from multiprocessing.spawn import old_main_modules
from typing import List
import heapq


class FoodRatings:
    food_map: dict[str, tuple[str,int]]  # food -> cuisine
    cuisine_map: dict[str, tuple[int,str]]

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_map = dict()
        self.cuisine_map = dict()
        for i in range(len(foods)):
            food = foods[i]
            cuisine = cuisines[i]
            rate = ratings[i]
            self.food_map[food] = (cuisine,rate)
            if cuisine in self.cuisine_map:
                self.cuisine_map[cuisine].append((-rate, food))
            else:
                self.cuisine_map[cuisine] = [(-rate, food)]
        for cuisine, values in self.cuisine_map.items():
            heapq.heapify(values)
            self.cuisine_map[cuisine] = values

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine,old_rate = self.food_map[food]
        values = self.cuisine_map[cuisine]
        values.remove((-old_rate, food))
        heapq.heappush(values, (-newRating, food))
        self.food_map[food] = (cuisine,newRating)

    def highestRated(self, cuisine: str) -> str:
        values = self.cuisine_map[cuisine]
        r = heapq.nsmallest(1, values)
        return r[0][1]

import unittest
class TestFoodRatings(unittest.TestCase):
    def test(self):
        foods = ["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"]
        cuisines = ["korean", "japanese", "japanese", "greek", "japanese", "korean"]
        ratings = [9, 12, 8, 15, 14, 7]
        foodRatings = FoodRatings(foods,cuisines, ratings)
        r = foodRatings.highestRated("korean")
        self.assertEqual("kimchi",r)
        r = foodRatings.highestRated("japanese")
        self.assertEqual("ramen", r)

        foodRatings.changeRating("sushi", 16)
        r = foodRatings.highestRated("japanese")
        self.assertEqual("sushi", r)
        foodRatings.changeRating("ramen", 16)
        r = foodRatings.highestRated("japanese")
        self.assertEqual("ramen", r)

if __name__ == '__main__':
    unittest.main()