# class Counter:
#     def __init__(self, max_number):
#         self.i = 0
#         self.max_number = max_number
#     def __iter__(self):
#         self.i = 0
#         return self
#
#     def __next__(self):
#         self.i += 1
#         if self.i > self.max_number:
#             raise StopIteration
#         return self.i
# count = Counter(5)
# for elem in count:
#     print(elem)
# spysok = [666,333,444]
# i = iter(spysok)
#
# for j in i:
#     print(j)
# for j in i:
#     print(j)
def raise_to_the_degrees(number, max_degree):
    i=0
    for _ in range(max_degree):
        yield number**i
        i+=1
res = raise_to_the_degrees(2, 10)
print(res)
for _ in res:
    print(_)