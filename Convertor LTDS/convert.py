"""Convertor , Version : 0.0.1"""


# To Lists
def tuple_to_list(tup=()):  # Converts Tuple to List
    tuple_list = list(tup)

    return tuple_list  # List


def dictionary_to_list(dictionary={}):  # Converts Dictionary To List
    dict_list = []

    for key, values in dictionary.items():
        key = key + ":"  # Adding " : " to know that it is key
        dict_list.append(key)
        dict_list.append(values)

    return dict_list  # List


# To Tuple
def list_to_tuple(lis=[]):  # Converts Dictionary to List
    list_tuple = tuple(lis)

    return list_tuple


def dictionary_to_tuple(dictionary={}):  # Converts Dictionary To Tuple
    dict_list = []

    for key, values in dictionary.items():
        key = key + ":"  # Adding " : " to know that it is key
        dict_list.append(key)
        dict_list.append(values)

    return tuple(dict_list)


# To Dictionary
def list_to_dictionary(lis=[]):  # Converts List to Dictionary
    list_dict = {}
    first_word = lis[0]
    key = ""
    value = ""

    if first_word[-1] == ":":
        for element in lis:
            if element[-1] == ":":
                key = str(element)
                key = key[:-1]  # We need to remove ":"
            else:
                value = element

            list_dict[key] = value

        return list_dict
    else:
        print("List cannot be Converted")  # Hey! Why didn't you follow ":" rule.
                                           # (Which was made by Me)


def tuple_to_dictionary(tup=()):  # Converts List to Dictionary
    tuple_dict = {}
    first_word = tup[0]
    key = ""
    value = ""

    if first_word[-1] == ":":
        for element in tup:
            if element[-1] == ":":
                key = str(element)
                key = key[:-1]  # We need to remove ":"
            else:
                value = element

            tuple_dict[key] = value

        return tuple_dict
    else:
        print("Tuple cannot be Converted")  # Hey! Why didn't you follow ":" rule.
                                           # (Which was made by Me)


if __name__ != '__main__':
    print("Hii from Benefit Zebra\nConvertor Version 0.0.1\n")
