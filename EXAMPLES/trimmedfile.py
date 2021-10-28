class TrimmedFile:
    def __init__(self, file_name):  # <1>
        self._file_in = open(file_name)

    def __iter__(self):  # <2>
        return self  # __iter__() must return obj that implements __next__

    def __next__(self):  # <3>  # make this obj an iterator
        line = self._file_in.readline()
        if line == '':
            raise StopIteration  # <4>
        else:
            return line.rstrip('\n\r')  # <5>

if __name__ == '__main__':
    trimmed = TrimmedFile('../DATA/mary.txt')  # <6>
    for line in trimmed:
        print(line)
