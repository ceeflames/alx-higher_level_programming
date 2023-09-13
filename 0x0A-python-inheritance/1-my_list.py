#!/usr/bin/python3
""" Class that inherits from list """


class MyList(list):
    """ inherits from list """

    def print_sorted(self):
        """ prints in acending order """

        print(sorted(self))
