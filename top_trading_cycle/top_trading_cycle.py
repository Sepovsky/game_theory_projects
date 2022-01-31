from collections import defaultdict
from random import randint, choice


class Graph:
    def __init__(self, vertices_count):
        self.edges = defaultdict(list)
        self.vertices_count = vertices_count

    def addEdge(self, from_node, to_node):
        self.edges[from_node].append(to_node)

    def findVertexInCycle(self):
        visited = set()
        v = choice(list(self.edges.keys()))
        while v not in visited:
            visited.add(v)
            v = choice(self.edges[v])
        return v

    def findCycle(self):
        vertex = self.findVertexInCycle()
        cycle = set()
        currentVertex = choice(self.edges[vertex])
        while currentVertex not in cycle:
            cycle.add(currentVertex)
            for _ in range(11):
                currentVertex = choice(self.edges[currentVertex])
        return cycle


class User:
    def __init__(self, index, preference_order):
        self.index = index
        self.order = preference_order

    def choose_proposee(self):
        return self.order[0]

    def reject(self):
        self.order.pop(0)


def sort_preferences(preference_order):
    return sorted(range(len(preference_order)), key=preference_order.__getitem__)


users_count = int(input('Enter number of users: '))
users = []
print('Enter user prefrences: ')
for i in range(users_count):
    preference_order = [int(x)-1 for x in input().split()]
    users.append(User(i, preference_order))

while users:
    graph = Graph(len(users))
    for user in users:
        graph.addEdge(user.index, user.choose_proposee())
    cycle = graph.findCycle()
    for vertex in cycle:
        print(f'User {vertex+1} <--> House {graph.edges[vertex][0]+1}')
    users_temp = []
    for user in users:
        if user.index not in cycle:
            if user.choose_proposee() in cycle:
                user.reject()
            users_temp.append(user)
            user_order = []
            for proposee in user.order:
                if proposee not in cycle:
                    user_order.append(proposee)
            user.order = user_order
    users = users_temp
