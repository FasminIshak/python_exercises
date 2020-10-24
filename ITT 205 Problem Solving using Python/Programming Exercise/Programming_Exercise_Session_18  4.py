def data(list1, list2):
     result = False
     for x in list1:
         for y in list2:
             if x == y:
                 result = True
                 return result
print(data([10,11,12,13,14], [15,16,17,18,19]))
print(data([1,2,3,7,5], [6,7,8,9]))