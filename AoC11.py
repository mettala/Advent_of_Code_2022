class Monkey:
    def __init__(self, start_items, operator, term, test_divider, if_true, if_false):
        self.items = start_items
        self.operator = operator
        self.term = term
        self.test_divider = test_divider
        self.if_true = if_true
        self.if_false = if_false
        self.activity = 0
        self.item_max_value = 0

    def receive_item(self, item):
        return self.items.append(item)

    def get_term(self, item):
        if self.term == 'old':
            return item
        else:
            return self.term

    def run_test(self,value):
        if value % self.test_divider == 0:
            return True
        else:
            return False

    def throw_item(self,item,worried):
        term = self.get_term(item)
        if worried:
            divider = 1
        else:
            divider = 3

        self.items.remove(item)
        if item > self.item_max_value:
            item = item % self.item_max_value

        if self.operator == '+':
            value = (int(item) + int(term)) // divider
        else:
            value = (int(item) * int(term)) // divider

        self.activity = self.activity + 1

        if self.run_test(value):
            return self.if_true, value
        else:
            return self.if_false, value

def initialize_monkeys(input):
    for r in input:
        if r[0:6] == 'Monkey':
            _, value = r.split(' ')
            monkey = 'monkey_' + str(value[0])
        if r[2:10] == 'Starting':
            starting_items = list(map(int, re.findall('\d+', r)))
        if r[2:11] == 'Operation':
            operator = r.split(' ')[6]
            term = r.split(' ')[7]
        if r[2:6] == 'Test':
            test_divier = int(r.split(' ')[-1])
        if r[4:11] == 'If true':
            if_true = int(r.split(' ')[-1])
        if r[4:12] == 'If false':
            if_false = int(r.split(' ')[-1])
            monkeys[monkey] = Monkey(starting_items, operator, term, test_divier, if_true, if_false)
    return monkeys

def run_rounds(loops,monkeys,worried = False):

    for i in range(loops):
        for monkey in monkeys:
            while len(monkeys[monkey].items) > 0:
                target,item = monkeys[monkey].throw_item(monkeys[monkey].items[0], worried)
                monkeys['monkey_'+str(target)].receive_item(item)

        activity_list = []
        for monkey in monkeys:
            activity_list.append(monkeys[monkey].activity)

    activity_list = sorted(activity_list)
    print('Level of monkey business after',loops,'rounds:',activity_list[-1]*activity_list[-2])

import re
import numpy as np

input = open('.\\Desktop\\AoC\\AoC11\\input.txt','r').read().splitlines()
monkeys = dict()

monkeys = initialize_monkeys(input)

test_divider_list=[]
for monkey in monkeys:
    test_divider_list.append(monkeys[monkey].test_divider)
item_max_value = np.prod(sorted(test_divider_list))

for monkey in monkeys:
    monkeys[monkey].item_max_value = item_max_value

run_rounds(20,monkeys)

monkeys = initialize_monkeys(input)
for monkey in monkeys:
    monkeys[monkey].item_max_value = item_max_value

run_rounds(10_000,monkeys,worried=True)