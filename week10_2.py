     
def insertion_sort(list):
    for i in range(1, len(list)):
        x = i-1
        pivot_element = list[i]
        
        while (list[x] > pivot_element) and (x >= 0):
            list[x+1] = list[x]
            x=x-1
        list[x+1] = pivot_element
    return

list = [1,0,1,0,1,0,0,1]
insertion_sort(list)
print(list)
        
                      
   
   

