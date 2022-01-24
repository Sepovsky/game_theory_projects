# number of boys and girls
girls_num = 0
boys_num = 0

# lists for saving their prefre
girls = []
boys = []
relation = []


# show index of boys in order ascending
def sort_boys(boys_arr):
    return sorted(range(boys_num), key=boys_arr.__getitem__)


# show index of girls in order ascending
def sort_girls(girls_arr):
    return sorted(range(girls_num), key=girls_arr.__getitem__)


class Boy:

    def __init__(self, x, girls_order) -> None:
        self.x = x
        self.order = sort_girls(girls_order)
        self.state = 0

    def compare_boys(self, g1, g2):

        for i in range(self.order):
            if i == g1:
                return 0
            elif i == g2:
                return 1
            else:
                return -1
    
    def choose_girl(self):
        return self.order[0]
    
    def reject(self):
        self.order.pop(0)


class Girl:

    def __init__(self, x, boys_order) -> None:
        self.x = x
        self.order = sort_boys(boys_order)
        self.state = 0 # in relation or not
    
    def compare_boys(self, b1, b2):

        for i in range(self.order):
            if i == b1:
                return 0
            elif i == b2:
                return 1
            else:
                return -1
    
    def choose_boy(self):
        return self.order[0]
    
    def reject(self):
        self.order.pop(0)


def choose_boy(b1, b2, g):

    if(girls[g].compare_boys(b1, b2)):
        boys[b1].reject()
        boys[b1].state = 0
        relation[g].append(b2)
        return 1
    
    else:
        return 0


def request(b):
    relation[b.choose_girl()].append(b)


def stable_conditon():
    for i in relation:
        if len(i) > 1:
            return 0
    
    return 1


############ main

boys_num = int(input('Enter number of boys: '))
girls_num = int(input('Enter number of girls: '))

print('Enter boys prefrences')

for i in range(boys_num):
    list_g = [int(x) for x in input().split()]
    boy = Boy(i, list_g)
    boys.append(boy)

print('Enter girls prefrences')

for i in range(girls_num):
    list_b = [int(x) for x in input().split()]
    girl = Girl(i, list_b)
    girls.append(girl)


while(stable_conditon() != 0):

    for i in range(boys_num):
        request(i)