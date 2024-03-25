# 1.
class MyList:
    def __init__(self, num_list) -> None:
        self.num_list = num_list
    
    def get_num_rep_count(self):
        result = {}
        for num in self.num_list:
            if num in result:
                result[num] += 1
            else:
                result[num] = 1
        for k,v in result.items():
            print(f'Число {k} встречается {v}')

    def __str__(self) -> str:
        return (f'Список: {self.num_list}')

mylist = MyList([1,1,3,2,1,3,4])
mylist.get_num_rep_count()
print(mylist)