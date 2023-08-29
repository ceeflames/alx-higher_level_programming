#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    if my_list_1 is None or my_list_2 is None:
        return (None)
    new_list = []
    for value in range(list_length):
        try:
            new-list.append(my_list_1[value] / my_list_2[value])
        except (IndexError):
            print("out of range")
            new_list.append(0)
        except (ZeroDivisionError):
            print("division by 0")
            new_list.append(0)
        except (TypeError):
            print("wrong typoe")
            new_list.append(0)
        finally:
            pass
    return (new_list)