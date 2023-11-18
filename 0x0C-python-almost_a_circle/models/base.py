#!/usr/bin/python3
"""First class base"""


import json, csv


class Base:
    """ private class attribute """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            """ assign the public instance attr id with the argument value"""
            self.id = id
        else:
            """ increment __nb_object and assign the new value to id """
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON str representation of list_dictionaries"""
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON str representation of list_objs"""
        if list_objs is None:
            list_objs = []

        filename = cls.__name__ + ".json"

        with open(filename, mode="w") as file:
            obj_list = [obj.to_dictionary() for obj in list_objs]
            json_str = cls.to_json_string(obj_list)
            file.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string"""
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)

        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        filename = cls.__name__ + ".json"

        try:
            with open(filename, mode="r") as f:
                json_str = f.read()
                obj_dicts = cls.from_json_string(json_str)
                return [cls.create(**obj_dict) for obj_dict in obj_dicts]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        filename = cls.__name__ + ".csv"

        with open(filename, mode="w", encoding="utf-8") as f:
            if cls.__name__ == "Rectangle":
                fieldnames = ["id", "width", "height", "x", "y"]
            elif cls.__name__ == "Square":
                fieldnames = ["id", "size", "x", "y"]

            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()

            for obj in list_objs:
                writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """deserializes in CSV"""
        filename = cls.__name__ + ".csv"
        instance = []

        try:
            with open(filename, mode="r", encoding="utf-8") as f:
                content = f.read()
                content = cls.from_json_string(content)

                for contents in content:
                    instance.append(cls.create())

                return instance
        except FileNotFoundError:
            return []
