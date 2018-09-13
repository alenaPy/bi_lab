"""
Description of script.

It shows list element with iteration number.
"""

friends = ['john', 'pat', 'gary', 'michael', 45, 45.5, True, None]
for i, name in enumerate(friends):
    print("iteration {iteration} is {name}".format(iteration=i, name=name))
