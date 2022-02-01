#number of boys and girls
boys_count = int(input('Enter number of boys: '))
girls_count = int(input('Enter number of girls: '))
boys_pref = []
girls_pref = []

print('Enter boys prefrences:')
for i in range(boys_count):
    pref_order = [int(x)-1 for x in input().split()]
    boys_pref.append(pref_order)

print('Enter girls prefrences:')
for i in range(girls_count):
    pref_order = [int(x)-1 for x in input().split()]
    girls_pref.append(pref_order)


def matching(boy_optimal):

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


    def show_result(is_boy_opt):
        if is_boy_opt:
            for i in range(proposees_count):
                print(f'Boy {relations[i][0]+1} <--> Girl {i+1}')
        else:
            for i in range(proposees_count):
                print(f'Girl {relations[i][0]+1} <--> Boy {i+1}')


    proposers = []
    proposees = []

    if boy_optimal:
        proposers_count = boys_count
        proposees_count = girls_count
    else:
        proposers_count = girls_count
        proposees_count = boys_count

    relations = [[] for _ in range(proposees_count)]

    for i in range(boys_count):
        preference_order = boys_pref[i]
        if boy_optimal:
            proposers.append(Proposer(i, preference_order))
        else:
            proposees.append(Proposee(i, preference_order))

    for i in range(girls_count):
        preference_order = girls_pref[i]
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
            show_result(boy_optimal)
            break
    
    return relations

# main
print("Boy-optimal is: ")
boy_opt = matching(1)

print("Girl-optimal is:")
girl_opt = matching(0)

# checking is unique or not
flag = 1
for i in range(len(boy_opt)):
    check = boy_opt[i][0]
    if  girl_opt[check][0] != i:
        flag = 0
        break

if flag:
    print("it is a unique stable matching. :))")
else:
    print("it is not a unique stable matching. :((")