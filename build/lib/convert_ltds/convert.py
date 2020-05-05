"""Convertor , Version : 0.1.1"""


# To List
def to_list(data):
    if type(data) == list:  # List to List
        return data

    elif type(data) == tuple:  # Tuple to List
        return list(data)  # Converted to Tuple

    elif type(data) == dict:  # Dict to List
        dict_list = []  # List of dict

        for key, values in data.items():
            key = str(key) + ":"  # Adding " : " to know that it is key
            dict_list.append(key)
            dict_list.append(values)

        return dict_list  # List

    else:  # Error
        print("Provide List/Tuple/Dict/Set")


# To Tuple
def to_tuple(data):
    if type(data) == list:  # List to Tuple
        return tuple(data)

    elif type(data) == tuple:  # Tuple to Tuple
        return data

    elif type(data) == dict:  # Dict to Tuple
        dict_tuple = tuple(to_list(data))
        return dict_tuple

    else:  # Error
        print("Provide List/Tuple/Dict/Set")


# To Dictionary
def to_dict(data):
    if type(data) == list:  # List to Dict

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
            print("List cannot be Converted")  # Hey! Why didn't you follow ":" rule.
            # (Which was made by Me)

    elif type(data) == tuple:  # Tuple to Dict
        return to_dict(list(data))

    elif type(data) == dict:  # Dict to Dict
        return data

    else:  # Error
        print("Provide List/Tuple/Dict/Set")


if __name__ != '__main__':
    print("Hii from Benefit Zebra\nConvertor Version 0.1.1\n")
