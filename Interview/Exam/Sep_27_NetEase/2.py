# fd >= 0 int
class fd:
    def __init__(self, n):
        self.max = n
        self.pair = {}  # fd:fn

    def open(self, file_name):
        # return a new fd point to file_name
        for i in range(self.max):
            if not i in self.pair.keys():
                self.pair.update({i: file_name})
                return i

    def dup(self, fd):
        # return a new fd point to the file old fd point to
        new_fd = self.open(self.query(fd))
        return new_fd

    def dup2(self, fd, new_fd):
        # let new fd point to the file fd point to
        self.pair.update({new_fd: self.pair[fd]})

    def close(self, fd):
        # let fd point to nothing
        self.pair.pop(fd)

    def query(self, fd):
        # return file_name fd point to
        return self.pair[fd]


def main():
    T = int(input())
    for _ in range(T):
        n = int(input())
        sol = fd(int(1e6))
        for i in range(n):
            line = input().split()
            func = line[0]

            if func == 'open':
                param = line[1]
                print(sol.open(param))
            elif func == 'dup':
                param = int(line[1])
                print(sol.dup(param))
            elif func == 'dup2':
                param = list(map(int, line[1:]))
                sol.dup2(param[0], param[1])
            elif func == 'close':
                param = int(line[1])
                sol.close(param)
            elif func == 'query':
                param = int(line[1])
                print(sol.query(param))


if __name__ == '__main__':
    main()
