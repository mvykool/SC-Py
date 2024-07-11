class Emitter:
    def __init__(self, fullpath):
        self.fullPath = fullpath
        self.header = ""
        self.code = ""

    def emit(self, code):
        self.code += code
