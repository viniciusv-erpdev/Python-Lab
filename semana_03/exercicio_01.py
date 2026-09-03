# Teste 1 — normal
votes = {"Ana": 1,"Carlos": 2}

candidates = [
    "Jose",
    "Jose",
    "Jose",
    "Ana",
    "Carlos",
    "Ana",
    "Maria",
    "Carlos",
    "Ana",
    "Sergio"
]

def count_votes_candidates(votes, candidates):

    for candidate in candidates:
        if candidate not in votes:
            votes[candidate] = 1
        else:
            votes[candidate] += 1

    return votes

print(count_votes_candidates(votes, candidates))