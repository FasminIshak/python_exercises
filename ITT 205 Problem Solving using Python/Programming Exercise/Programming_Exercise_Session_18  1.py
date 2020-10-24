def search(list,n): 
  
    for i in range(len(list)): 
        if list[i] == n: 
            return True
    return False

list = [11, 32, 'sum', 4,'equal', 6] 
n = input("Enter the string/number :")
if search(list, n): 
    print("Found") 
else: 
    print("Not Found") 