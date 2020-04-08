"""nums = [5,6,8,3]

#for i in nums:
#    print(i)

it = iter(nums)
print(it.__next__())
print(it.__next__())
print(next(it))"""
class Iterator:

    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= 10:
            val = self.num
            self.num += 1
            return val
        else:
            raise StopIteration

values = Iterator()
for i in values:
    print(i)