# List = [] ordered and changeable, duplicates are OK
# set = {} unordered and immutable, but ADD/REMOVe OK, No dupplicates
# tuple = () ordered and ucnhangebale, Duplicates OK, faster
# print(help(list))
# print(dir(list))

#dictionaries
# a collection of {key:value} pairs, ordered and changeable. No duplicates
dictionary = {"key1":"value1", "key2":"value2", "key3":"value3"}

print(dictionary.keys())
print(dictionary.values())
print(dictionary.items())

for key, value in dictionary.items():
    print(f"{key}: {value}")