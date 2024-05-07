#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''pa6 functions for homework 6'''


# In[1]:


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

total_amount = 10
result = make_change(total_amount)
print("Distinct combinations of coins for", total_amount, "cents:", result)


# In[2]:


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

result = dict_filter(checker, example)
print(result)


# In[ ]:





# In[3]:


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

samplekv = KVTree("us", 4.6)
pa = KVTree("pa", 1.9)
samplekv.add_child(pa)
pa.add_child(KVTree("Pittsburgh", 0.3))
pa.add_child(KVTree("Philadelphia", 1.6))
il = KVTree("il", 2.7)
samplekv.add_child(il)
il.add_child(KVTree("Chicago", 2.7))

treemap(update_node, samplekv)

def print_tree(tree):
    print(f"Key: {tree.key}, Value: {tree.value}")
    for child in tree.children:
        print_tree(child)

print_tree(samplekv)


# In[ ]:





# In[4]:


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


tree1 = DTree(0, 66, DTree(None, None, None, None, "walk"),
              DTree(None, None, None, None, "stay home"), None)

tree2 = DTree(0, 66,
              DTree(2, 10,
                    DTree(None, None, None, None, "walk"),
                    DTree(None, None, None, None, "stay home"), None),
              DTree(None, None, None, None, "stay home"), None)

print("Minimum tuple size for tree1:", tree1.tuple_atleast())
print("Minimum tuple size for tree2:", tree2.tuple_atleast())

observations = (60, 50, 8)
print("Outcome for observations in tree2:", tree2.find_outcome(observations))

print("No repeats in tree1:", tree1.no_repeats())
print("No repeats in tree2:", tree2.no_repeats())


# In[ ]:




