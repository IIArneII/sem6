class sum(int):
    def __call__(self, a=0):
        return self + sum(a)


print(sum(10)(11))
