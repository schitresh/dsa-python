class MergeSort:
    def __init__(self, array):
        self.array = array

    def perform(self):
        self.array.sort()
        return self.array
