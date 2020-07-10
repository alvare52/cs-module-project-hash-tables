records = [
    ("Tim", "Texas"),
    ("Adam", "Florida"),
    ("Austin", "Florida"),
    ("Kai", "South Carolina"),
    ('Jud', 'Phoebos'),
    ("Eric", "Utah"),
    ("Mandi", "Virginia"),
    ("Emma", "Florida"),
    ("Anna", "Texas"),
    ("Andrew", "Utah"),
    ("Leo", "New York"),
    ('James', "New York")
]

# given a list of records, build an index
# so we can quickly find everyone in a given state

# Iterate through the tuples in our list
# Build a dictionary as we go. Use states as key, and names and values

def build_index(records):
    index = {}
    # iterate through list
    # tuple destructuring
    for name, state in records:
        # for each pair, check if the state is in the dictionary
        if state in index:
            # if so, append the name to the list
            index[state].append(name)
        # if not, add the key and list (with name in it)
        else:
            #index.setdefault(state, [name])
            index[state] = []
            index[state].append(name)

    return index

idx = build_index(records)

print(idx["New York"])
print(idx["South Carolina"])