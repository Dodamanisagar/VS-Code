# Creating sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# 1. add() - Adds an element to the set
set1.add(6)
print("After add:", set1)

# 2. remove() - Removes an element from the set
set1.remove(6)
print("After remove:", set1)

# 3. discard() - Removes an element from the set if it is a member. If not, do nothing.
set1.discard(5)
print("After discard:", set1)

# 4. pop() - Removes and returns an arbitrary set element. Raises KeyError if the set is empty.
popped_element = set1.pop()
print("Popped element:", popped_element)
print("After pop:", set1)

# 5. clear() - Removes all elements from the set
set1.clear()
print("After clear:", set1)

# 6. union() - Returns a new set with elements from both sets
union_set = set1.union(set2)
print("Union:", union_set)

# 7. intersection() - Returns a new set with elements common to both sets
intersection_set = set1.intersection(set2)
print("Intersection:", intersection_set)

# 8. difference() - Returns a new set with elements in the set that are not in the other set
difference_set = set2.difference(set1)
print("Difference:", difference_set)

# 9. symmetric_difference() - Returns a new set with elements in either the set or the other set but not in both
symmetric_difference_set = set1.symmetric_difference(set2)
print("Symmetric Difference:", symmetric_difference_set)

# 10. issubset() - Returns True if all elements of the set are in the other set
is_subset = set1.issubset(set2)
print("Is subset:", is_subset)

# 11. issuperset() - Returns True if all elements of the other set are in the set
is_superset = set2.issuperset(set1)
print("Is superset:", is_superset)

# 12. isdisjoint() - Returns True if two sets have a null intersection
is_disjoint = set1.isdisjoint(set2)
print("Is disjoint:", is_disjoint)