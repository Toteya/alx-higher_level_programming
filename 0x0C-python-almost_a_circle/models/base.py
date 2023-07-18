#!/usr/bin/python3
""" The base module
Contains Base class
"""
import json
import csv
import turtle
import random


class Base:
    """ Base class """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns the JSON string representation of the given
        list of dictionaries `list_dictionaries`
        """
        if list_dictionaries is None:
            return json.dumps([])
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """ Returns the list of the JSON string representation given
        """
        if json_string:
            return json.loads(json_string)
        return []

    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes a the list of Base objects `list_obj` to
        a file
        """
        filename = f"{cls.__name__}.json"
        if list_objs is None:
            list_dicts = []
        else:
            list_dicts = [obj.to_dictionary() for obj in list_objs]
        json_dicts = cls.to_json_string(list_dicts)
        with open(filename, mode="w", encoding="utf-8") as a_file:
            a_file.write(json_dicts)

    @classmethod
    def create(cls, **dictionary):
        """ Creates and returns an instance with all attributes
        already set
        """
        if cls.__name__ == 'Rectangle':
            obj = cls(1, 1)
        elif cls.__name__ == 'Square':
            obj = cls(1)
        obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        """ returns a list of instances from a file as determined by
        the file to load depends on the class e.g. Rectangle.json
        i.e. filename == <Class name>.json
        """
        filename = f"{cls.__name__}.json"
        dict_list = []
        obj_list = []
        try:
            with open(filename, mode="r", encoding="utf-8") as a_file:
                json_string = a_file.read()
                dict_list = cls.from_json_string(json_string)
                obj_list = [cls.create(**obj_dict) for obj_dict in dict_list]
        except FileNotFoundError:
            pass
        return obj_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Serializes and writes object instances into CSV format
        """
        filename = f"{cls.__name__}.csv"
        with open(filename, mode="w", encoding="utf-8", newline="") as a_file:
            if not list_objs:
                raise open.Break

            fields = list_objs[0].to_dictionary().keys()

            writer = csv.DictWriter(a_file, fieldnames=fields)
            writer.writeheader()
            for obj in list_objs:
                writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """ Reads and deserializes object instances from a CSV
        format file
        """
        filename = f"{cls.__name__}.csv"
        obj_list = []
        with open(filename, "r", encoding="utf-8") as a_file:
            csv_file = csv.DictReader(a_file)
            dict_list = [dict(obj_dict) for obj_dict in csv_file]

            for obj_dict in dict_list:
                for key, value in obj_dict.items():
                    obj_dict[key] = int(value)

            obj_list = [cls(**obj_dict) for obj_dict in dict_list]

        return obj_list

    @staticmethod
    def draw(list_rectangles, list_squares):
        """ Opens a window and draws all the Rectangles and Squares
        """
        # my turtle
        mt = turtle.Turtle()
        mt.pensize(2)
        mt.pencolor("red")
        mt.fillcolor("green")

        # set my screen
        tw = turtle.Screen()
        tw.setup(600, 600)
        tw.bgcolor("pink")
        # colormode allows me to set the color with (r,g,b)
        # this allows me to randomise the colors
        tw.colormode(255)

        # set turtle starting position
        mt.penup()
        mt.backward(tw.window_width() / 2 - 10)
        mt.right(90)
        mt.forward(tw.window_height() / 4 - 20)
        mt.left(90)

        list_shapes = [list_rectangles, list_squares]

        # get total width to allow correct sizing of drawings on the screen
        total_width = 0
        for shapes in list_shapes:
            if shapes is not None:
                for shape in shapes:
                    total_width += shape.width

        # ratio of screen to total_width allows to fit the shapes onto screen
        size_ratio = (tw.window_width() - 20) / (total_width)

        for shapes in list_shapes:
            if shapes is not None:
                for shape in shapes:
                    rgb = tuple(random.choice(range(255)) for _ in range(3))
                    mt.fillcolor(rgb)
                    mt.pendown()
                    mt.begin_fill()
                    for _ in range(2):
                        mt.forward(shape.width * size_ratio)
                        mt.left(90)
                        mt.forward(shape.height * size_ratio)
                        mt.left(90)

                    mt.end_fill()
                    mt.penup()
                    mt.forward(shape.width * size_ratio)
        turtle.done()
