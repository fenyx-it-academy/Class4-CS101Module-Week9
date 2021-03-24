import heapq
class Heap:
    
    def __init__(self,list=None) -> None:
        self.list=list       
        
    def min_item(self):
        if self.list is None:
            "list is empty"
        heapq.heapify(self.list) #converts list into a stack
        return heapq.heappop(self.list) #returns the smallest data from the list
        
    def ropes_lenght(self): 
        x=[]
        self.y=[]
        while len(self.list)>0:
            x.append(self.min_item()) #minimum item of the list add new list
            if len(x)==2:
                a=[sum(x)]               
                x=a                  # assigned the sum of the items 
                self.y.append(sum(x))       #the sum of the items add new list         
        return self.y
    
    def all_ropes(self):
       return sum(self.y)      #returns the sum of the items in new list
   
    def __str__(self) -> str:
        count=0
        total_list=[]
        for i in self.ropes_lenght():
            count+=1
            a=f"{count}.Rope Length: {i} "
            total_list.append(a)
        return  f'Lengths of Ropes:\n\n{"".join(total_list)}\n\nThe total cost for all ropes:{self.all_ropes()} € \n'      
                
        
   
rope=Heap([5,4,2,8])

print(rope.__str__())


    