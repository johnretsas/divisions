from platform import release
from traceback import print_list


def get_results(division, n):
    # Your code here
    resultString = ''
    division.sort(key=accessPoints, reverse=True)
    promote = division[0:n]
    relegate = division[-n:]

    for pr in promote:
        for re in relegate:
            if (pr['name'] == re['name']):
                return "Team " + pr['name'] + "is in both the promote and the relegate categories"

    resultString += "Promote:\n"
    
    for pr in promote:
        resultString += pr['name'] + "\n"
    
    resultString += "\n"

    resultString += "Relegate:\n"

    for re in relegate:
        resultString += re['name'] + "\n"

    return resultString

def accessPoints(d):
    return d['points']


given_division = [
    {
        "name": "Rockets",
        "points": 64,
    },
    {
        "name": "Cardinals",
        "points": 77,
    },
    {
        "name": "Bruisers",
        "points": 51,
    },
    {
        "name": "Renegades",
        "points": 37,
    },
    {
        "name": "Porpoises",
        "points": 52,
    },
]

print(get_results(given_division, 2))