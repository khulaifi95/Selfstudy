
voted = {}


def check_voter(name):
    if voted.get(name):
        print("Kick him out!")
    else:
        voted[name] = True
        print("Let him vote!")


check_voter("tom")

check_voter("tom")
