# 1.
# class MyList:
#     def __init__(self, num_list) -> None:
#         self.num_list = num_list
    
#     def get_num_rep_count(self):
#         result = {}
#         for num in self.num_list:
#             if num in result:
#                 result[num] += 1
#             else:
#                 result[num] = 1
#         for k,v in result.items():
#             print(f'Число {k} встречается {v}')

#     def __str__(self) -> str:
#         return (f'Список: {self.num_list}')

# mylist = MyList([1,1,3,2,1,3,4])
# mylist.get_num_rep_count()
# print(mylist)

# 2. 
class Star:
    def __init__(self, text) -> None:
        self.text = text
    
    def replace_space_to_star(self):
        result = ''
        for t in (self.text.strip().split()):
            result += t
            result += '*'
        print(result[:-1])

star = Star('     Hello World!  ')
star.replace_space_to_star()