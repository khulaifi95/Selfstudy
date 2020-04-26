
from collections import deque


graph = {}

graph['you'] = ['alice', 'bob', 'claire']
graph['bob'] = ['anuj', 'peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['thom', 'jonny']
graph['anuj'] = []
graph['peggy'] = []
graph['thom'] = []
graph['jonny'] = []


def person_is_seller(name):
    return name[-1] == 'm'


def search(name):
    queue = deque()
    queue += graph[name]
    searched = []

    while queue:
        person = queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print(person + " is a mango seller!")
                return True
            else:
                queue += graph[person]
                searched.append(person)

    return False

search('you')