# -*- coding: utf-8 -*-
from . import helpers

class Sample():
    description = "RCE for version 12.4.0-12.8.1 - !!RUBY REVERSE SHELL IS VERY UNRELIABLE!! WIP"

    def __init__(self):
      self.true = True
      self.false = False
      self.int = 1
      self.string = "Hello"

    def print_vars(self):
      print("True:\t{}".format(self.true))
      print("False:\t{}".format(self.false))
      print("Int:\t{}".format(self.int))
      print("String:\t{}".format(self.string))
        