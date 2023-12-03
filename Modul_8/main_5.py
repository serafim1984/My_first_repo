import random


def get_random_winners(quantity, participants):

    if quantity > len(participants):

        return []
    
    list_keys = list(participants.keys())

    random.shuffle(list_keys)

    winners_keys = random.sample(list_keys, k = quantity)

    return winners_keys