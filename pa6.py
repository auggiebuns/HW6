#!/usr/bin/env python3
'''pa6 functions for homework 6'''


def make_change(total):
    '''Find all distinct combinations of coins that add up to the total amount.'''
    denominations = [1, 5, 10, 25, 100]
    combinations = []

    def backtrack(curr_combination, remaining_total, start_index):
        if remaining_total == 0:
            combinations.append(curr_combination[:])
            return
        for i in range(start_index, len(denominations)):
            coin = denominations[i]
            if coin <= remaining_total:
                curr_combination.append(coin)
                backtrack(curr_combination, remaining_total - coin, i)
                curr_combination.pop()
    backtrack([], total, 0)
    return combinations

CHANGE = 10
RESULT = make_change(CHANGE)
print("Distinct combinations of coins for", CHANGE, "cents:", RESULT)


def dict_filter(func, dictionary):
    '''Filter a dictionary based on a given function.'''
    filtered_dict = {}
    for key, value in dictionary.items():
        if func(key, value):
            filtered_dict[key] = value
    return filtered_dict


def checker(name, abbrev):
    return abbrev[0] == "I" and name[1] == "l"

example = {"Illinois": "IL", "Pennsylvania": "PA", "Indiana": "IN"}

RESULT2 = dict_filter(checker, example)
print(RESULT2)


class KVTree:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.children = []

    def add_child(self, child):
        self.children.append(child)


def treemap(func, tree):
    '''Modify a tree according to the provided function.'''
    tree.key, tree.value = func(tree.key, tree.value)
    for child in tree.children:
        treemap(func, child)


def update_node(key, value):
    return key.upper(), value * 1000000


SAMPLEKV = KVTree("us", 4.6)
PENN = KVTree("pa", 1.9)
SAMPLEKV.add_child(pa)
PENN.add_child(KVTree("Pittsburgh", 0.3))
PENN.add_child(KVTree("Philadelphia", 1.6))
ILL = KVTree("il", 2.7)
samplekv.add_child(il)
ILL.add_child(KVTree("Chicago", 2.7))

treemap(update_node, SAMPLEKV)


def print_tree(tree):
    print(f"Key: {tree.key}, Value: {tree.value}")
    for child in tree.children:
        print_tree(child)

print_tree(SAMPLEKV)


class DTree:
    def __init__(self, variable, threshold, lessequal, greater, outcome):
        if (variable is not None and threshold is not None and 
            lessequal is not None and greater is not None and outcome is None) or \
           (variable is None and threshold is None and 
            lessequal is None and greater is None and outcome is not None):
            self.variable = variable
            self.threshold = threshold
            self.lessequal = lessequal
            self.greater = greater
            self.outcome = outcome
        else:
            raise ValueError("Invalid inputs")


    def tuple_atleast(self):
        '''Analyze the tree and determine the minimum size of tuples needed.'''
        if self.variable is not None:
            return max(self.variable + 1, self.lessequal.tuple_atleast(), self.greater.tuple_atleast())
        else:
            return 0


    def find_outcome(self, observations):
        '''Navigate through the tree to find the outcome based on the observations.'''
        if self.variable is None:
            return self.outcome
        elif observations[self.variable] <= self.threshold:
            return self.lessequal.find_outcome(observations)
        else:
            return self.greater.find_outcome(observations)


    def no_repeats(self):
        '''Analyze the tree and determine if there are no repeats.'''
        def helper(node, seen):
            if node.variable is None:
                return True
            elif node.variable in seen:
                return False
            else:
                seen.add(node.variable)
                return helper(node.lessequal, seen) and helper(node.greater, seen)
        return helper(self, set())


TREE1 = DTree(0, 66, DTree(None, None, None, None, "walk"),
              DTree(None, None, None, None, "stay home"), None)

TREE2 = DTree(0, 66,
              DTree(2, 10,
                    DTree(None, None, None, None, "walk"),
                    DTree(None, None, None, None, "stay home"), None),
              DTree(None, None, None, None, "stay home"), None)

print("Minimum tuple size for tree1:", TREE1.tuple_atleast())
print("Minimum tuple size for tree2:", TREE2.tuple_atleast())

OBSERVATIONS = (60, 50, 8)
print("Outcome for observations in tree2:", TREE2.find_outcome(OBSERVATIONS))

print("No repeats in tree1:", TREE1.no_repeats())
print("No repeats in tree2:", TREE2.no_repeats())
