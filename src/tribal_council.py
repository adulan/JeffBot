import random
from src.utils import get_idols

class TribalCounil:

    
    def __init__(self, tribe):
        self.tribe = tribe
        self.members = tribe.members
        self.time_to_vote = False
        self.votes = []

    def sort_votes(votes):
        """Return a list which gives a more 'dramatic' vote order"""
        # Grab a tally of the votes
        tally = {}
        for item in votes:
            if item in tally:
                tally[item] += 1
            else:
                tally[item] = 1
        # Check if a player is using an idol and handle accordingly
        has_idol = []
        idols = get_idols()
        for player in tally:
            if player in idols:
                has_idol.append(player)
        check = {}
        for item in votes:
            if item not in has_idol:
                if item in check:
                    check[item] += 1
                else:
                    check[item] = 1
        # Get who had the most votes
        highest = max(check.values())
        most = [a for a, b in check.items() if b == highest]
        # If more than one person has the most votes, shuffle the vote order
        # and return
        if len(most) != 1:
            random.shuffle(votes)
            return votes, None
        most = most[0]
        majority = len(votes) // 2
        if tally[most] > majority:
            # If a player has more than majority, get how many more they have
            extra = tally[most] - majority
            tally[most] -= extra
        else:
            tally[most] -= 1
        new = []
        # Add the rest to new
        for item in tally:
            for n in range(tally[item]):
                new.append(item)
        # Shuffle
        random.shuffle(new)
        # Add the final vote back to the end of new
        new.append(most)
        return new, most