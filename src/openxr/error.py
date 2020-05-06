# This is free and unencumbered software released into the public domain.

class Error(Exception):
    def __init__(self, result):
        self.result = result
