import numpy

class UrlMatrix:
    def __init__(self, urlarray):
        self.matrix = numpy.matrix(urlarray, bool)

