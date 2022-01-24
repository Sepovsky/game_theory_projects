# number of boys and girls
boys_num = int(input('Enter number of boys: '))
girls_num = int(input('Enter number of girls: '))

# lists for saving their prefre
girls = []
boys = []
relation = [[] for x in range(girls_num)]


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

    def compare_girls(self): #we should use another array for girls-opt
        tmp = -1
        for i in self.order:
            if i in relation[self.x]:
                tmp = i
                break
        
        for i in relation[self.x]:
            if i != tmp:
                boys[i].reject()

            relation[self.x].remove(i)
        
        relation[self.x].append(tmp)
    
    def choose_girl(self):
        return self.order[0]
    
    def reject(self):
        tmp = self.order.pop(0)
        self.state = 0
    
    def request(self):
        self.state = 1
        relation[self.choose_girl()].append(self.x)


class Girl:

    def __init__(self, x, boys_order) -> None:
        self.x = x
        self.order = sort_boys(boys_order)
        self.state = 0 # in relation or not
    
    def compare_boys(self):
        tmp = -1
        for i in self.order:
            if i in relation[self.x]:
                tmp = i
                break
        
        for i in relation[self.x]:
            if i != tmp:
                boys[i].reject()

            relation[self.x].remove(i)
        
        relation[self.x].append(tmp)

    
    def choose_boy(self):
        return self.order[0]
    
    def reject(self):
        self.order.pop(0)


def stable_conditon():
    for i in range(girls_num):
        if len(relation[i]) > 1:
            return i
    
    return -1


def show_result():
    for i in range(girls_num):
        print(f'boy {relation[i]} --> girl {i}')



############ main
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


for ctr in range((boys_num * girls_num) + 1):
    for i in boys:
        if i.state == 0:
            i.request()
    
    famouse_girl = stable_conditon()
    # print("f_g", famouse_girl)
    if(famouse_girl != -1):
        # print('im here')
        # for k in range(girls_num):
            # print(f'{relation[k]}-{k}')
        girls[famouse_girl].compare_boys()
    
    else:
        print(ctr)
        show_result()
        break