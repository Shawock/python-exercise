class MagicDemo:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __del__(self):
        print("gc happened.")
