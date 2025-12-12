import random


expected_dice_roll = 3.5


def dice_roll(k=6):
    result = random.randint(1, k)
    print("result:", result)
    return result
