class Proposer:
    def __init__(self, index, preference_order):
        self.index = index
        self.order = sort_preferences(preference_order)
        self.married = False

    def choose_proposee(self):
        return self.order[0]

    def reject(self):
        self.order.pop(0)
        self.married = False

    def propose(self):
        self.married = True
        relations[self.choose_proposee()].append(self.index)


class Proposee:
    def __init__(self, index, preference_order):
        self.index = index
        self.order = sort_preferences(preference_order)

    def compare_proposers(self):
        relations[self.index].sort(key=self.order.index)
        for proposer in relations[self.index][1:]:
            proposers[proposer].reject()
        relations[self.index] = [relations[self.index][0]]


def sort_preferences(preference_order):
    return sorted(range(len(preference_order)), key=preference_order.__getitem__)


def get_wanted_proposees():
    wanted_proposees = []
    for i in range(proposees_count):
        if len(relations[i]) > 1:
            wanted_proposees.append(i)
    return wanted_proposees


def show_result():
    for i in range(proposees_count):
        print(f'Boy {relations[i][0]+1} <--> Girl {i+1}')


boys_count = int(input('Enter number of boys: '))
girls_count = int(input('Enter number of girls: '))
boy_optimal = bool(input('0. Girl Optimal 1.Boy Optimal: '))
proposers = []
proposees = []
if boy_optimal:
    proposers_count = boys_count
    proposees_count = girls_count
else:
    proposers_count = girls_count
    proposees_count = boys_count
relations = [[] for _ in range(proposees_count)]

print('Enter boys prefrences:')
for i in range(boys_count):
    preference_order = [int(x)-1 for x in input().split()]
    if boy_optimal:
        proposers.append(Proposer(i, preference_order))
    else:
        proposees.append(Proposee(i, preference_order))

print('Enter girls prefrences:')
for i in range(girls_count):
    preference_order = [int(x)-1 for x in input().split()]
    if boy_optimal:
        proposees.append(Proposee(i, preference_order))
    else:
        proposers.append(Proposer(i, preference_order))


for _ in range((proposers_count * proposees_count) + 1):
    for proposer in proposers:
        if not proposer.married:
            proposer.propose()
    wanted_proposees = get_wanted_proposees()
    for proposee in wanted_proposees:
        proposees[proposee].compare_proposers()
    if not wanted_proposees:
        show_result()
        break
