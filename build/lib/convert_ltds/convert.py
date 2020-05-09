"""Convertor , Version : 0.1.5"""


def input_err():
    print("Provide List/Tuple/Dict/Set/Frozenset")
    exit(-1)


# To List
def to_list(data):
    # List/Tuple/Set/Frozenset to List
    if type(data) is list or type(data) is tuple or \
            type(data) is set or type(data) is frozenset:
        return list(data)

    # Dict to List
    elif type(data) is dict:
        dict_list = []  # List of dict

        for key, values in data.items():
            key = str(key) + ":"  # Adding " : " to know that it is key
            dict_list.append(key)
            dict_list.append(values)

        return dict_list  # List

    else:  # Error
        input_err()


# To Tuple
def to_tuple(data):
    # List/Tuple/Set/Frozenset to Tuple
    if type(data) is list or type(data) is tuple or \
            type(data) is set or type(data) is frozenset:
        return tuple(data)

    # Dict to Tuple
    elif type(data) is dict:
        return tuple(to_list(data))

    else:  # Error
        input_err()


# To Dictionary
def to_dict(data):
    if type(data) is list:  # List to Dict

        list_dict = {}
        first_word = data[0]
        key = ""
        value = ""

        if first_word[-1] == ":":
            for element in data:
                element = str(element)
                if element[-1] == ":":
                    key = str(element)
                    key = key[:-1]  # We need to remove ":"
                else:
                    value = element

                list_dict[key] = value

            return list_dict
        else:
            print("Data cannot be Converted")  # Hey! Why didn't you follow ":" rule.
            # (Which was made by Me)

    # Tuple to Dict
    elif type(data) is tuple:
        return to_dict(list(data))

    # Dict to Dict
    elif type(data) is dict:
        return data

    elif type(data) is set or type(data) is frozenset:
        print("Set/Frozenset cannot be converted to Dict.\n"
              "Due to Fact that set/frozenset elements get rearranged each time when program is run")
        exit(-1)

    else:  # Error
        print("Provide List/Tuple/Dict")
        exit(-1)


# To Set
def to_set(data):
    # List/Tuple/Set/Frozenset to Set
    if type(data) is list or type(data) is tuple or \
            type(data) is set or type(data) is frozenset:
        return set(data)

    # Dict to Set
    elif type(data) is dict:
        return set(to_list(data))

    else:  # Error
        input_err()


# To Frozenset
def to_frozenset(data):
    # List/Tuple/Set/Frozenset to Frozenet
    if type(data) is list or type(data) is tuple or \
            type(data) is set or type(data) is frozenset:
        return frozenset(data)

    # Dict to Frozenset
    elif type(data) is dict:
        return frozenset(to_list(data))

    else:  # Error
        input_err()


if __name__ != '__main__':
    print("Hii from Benefit Zebra\nConvertor Version 0.1.5\n"
          "Give me Suggestions on https://github.com/Benefit-Zebra/Convertor-LTDS\n")

# Tests
# list1 = ["abcd:", "$%^';", 4535, 4545.979]
# tuple1 = ("efgh:", "/*-+", 5656, 2343.432)
# set1 = {"ijkl:", "*&^%", 1234, 1234.56}
# dict1 = {"mnop": "!@$$", "asdf": 7890.01}
# frozenset1 = frozenset({"Asad:", 32432, "qwer", 2324.5})
# print()
