#!/usr/bin/python3
"""Module with the base class"""
import json
import os
import csv
import turtle


class Base:
    """Class with methods"""
    __nb_objects = 0
    def __init__(self, id=None):
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
    
    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries == None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        filename = cls.__name__ + ".json"

        if list_objs == None:
            list_objs = []
        list_dict = [d.to_dictionary() for d in list_objs]
        json_string = cls.to_json_string(list_dict)
        with open(filename, "w", encoding="utf-8") as json_f:
            json_f.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        if json_string == None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + ".json"

        try:
            with open(filename, "r", encoding="utf-8") as json_f:
                json_string = json_f.read()
            list_dict = cls.from_json_string(json_string)
            return [cls.create(**d) for d in list_dict]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as f:
            if list_objs is None or list_objs == []:
                f.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as f:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(f, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        window = turtle.Screen()
        window.bgcolor("grey")

        drawer = turtle.Turtle()
        drawer.speed(0)

        for rect in list_rectangles:
            drawer.penup()
            drawer.goto(rect.x, rect.y)
            drawer.pendown()
            drawer.fillcolor("blue")
            drawer.begin_fill()
            for _ in range(2):
                drawer.forward(rect.width)
                drawer.left(90)
                drawer.forward(rect.height)
                drawer.left(90)
            drawer.end_fill()

        for square in list_squares:
            drawer.penup()
            drawer.goto(square.x, square.y)
            drawer.pendown()
            drawer.fillcolor("red")
            drawer.begin_fill()
            for _ in range(4):
                drawer.forward(square.size)
                drawer.left(90)
            drawer.end_fill()

        window.exitonclick()
