SUFFIXES = {1000: ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'],
            1024: ['KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']}

# Instead of the word `function`, in Python, you use `def`
def approximate_size(size, a_kilobyte_is_1024_bytes=True):

    '''Convert a file size to human-readable form.

    Keyword arguments:
    size -- file size in bytes
    a_kilobyte_is_1024_bytes -- if True (default), use multiples of 1024
                                if False, use multiples of 1000

    Returns: string

    '''
    if size < 0:
        raise ValueError('number must be non-negative')

    multiple = 1024 if a_kilobyte_is_1024_bytes else 1000
    for suffix in SUFFIXES[multiple]:
        size /= multiple
        if size < multiple:
            return '{0:.1f} {1}'.format(size, suffix)
            # or return f'{size:.1f} {suffix}'

    raise ValueError('number too large')

# if __name__ == '__main__':
#     print(approximate_size(16384, False))
#     print(approximate_size(size=16384, a_kilobyte_is_1024_bytes=True))
#     print(approximate_size(-16384))



# name = "Fred"
# def say_name():
#     global name
#     name = "Bubba"
    # print("internal, name")

# say_name()
# print("external", name)


# if/else
name = "Joe"
if name == "Steve":
    print("I feel great")
elif name == "Joe":
    print("You got the better instructor")
else:
    print("I have a cold")

# string concatenation
print(f"My name is {name}")

#Storing in Collections
#List

junk = ["Fred", True, [1,2,3], 234]
print(junk)

#add to the list
junk.append("uh-oh")
print(junk)

#for more than one addition only 2
junk.insert(3, "oh, I get it")
print(junk)

junk.extend(["Mary", "Joesph", "Bob"])
print(junk)

#take list and put as a string
print(", ".join(name))

#dictionaries
my_pairs = {
    123: "number",
    "name": "Bromhilda"

}

print(my_pairs["name"])

#add a key/value
my_pairs["last"] = "Jones"
print(my_pairs)
my_pairs["address"] = {"number": 123,
"street": "Seasame St"}
print(my_pairs)
#get address from mypairs/access nested values
street_name = my_pairs["address"]["street"]
print(street_name)

#to access all the keys or values of my_pairs
print(my_pairs.items())
print(my_pairs.values())
print(my_pairs.items())

street_name = my_pairs["address"]
["street"]

# Sets - is to make sure everything is unique can't index with set as line 108.
my_set = {"Fred", True, 123, "Jones"}
print(my_set)
print(junk[3])

my_stuff = ["Fred", True, 123, "Jones", "Fred"]
print(my_stuff)
print(list(set(my_stuff)))

#add to my set
my_set = {1,2,3}
my_set.add("Feed me")
print(my_set)


#tuple it is unchangable/unmutable but you can reassign value
my_tup = (1,2,3,3, "hello")
print(my_tup)
my_tup = ("WTF", "I'm hungry")
print(my_tup)
my_little_tup = ("hello")
print(my_little_tup)
print(isinstance(my_little_tup, tuple)

#loopss
# my_tup = (1,2,3,3, "hello")
# my_set = {1,2,3}
# junk = ["Fred", True, [1,2,3], 234]
# my_dict = {
#     123: "number",
#     "name": "Broomhilda"
# }

for foo in my_dict:
    print(f"Why do I still have {foo} in this drawer?")

for foo in my_pairs.values():
    print(f"Why do I still have {foo} in this drawer?")

for foo in my_dict.keys():
    print(f"Why do I still have {foo} in this drawer?")


my_list = [1,2,4, "hello", "monkey"]
my_subset = my_list[0:3]
my_subset = my_list[:3]
my_subset = my_list[2:]
my_subset = my_list[2:34]
my_subset = my_list[2:-1]


print(my_subset)


