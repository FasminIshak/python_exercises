def Sequential_Search(list, n):
    for i in range(len(list)): 
        if list[i] == n: 
            return True
    return False
    
list = [1, 3, 'sum', 5,'equal', 7] 
n = input("Enter the string/number :")
if Sequential_Search(list, n): 
    print("Found") 
else: 
    print("Not Found") 