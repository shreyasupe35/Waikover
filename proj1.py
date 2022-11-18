print("happy deepavali in advanve")
print("welcome to your shopping list")
shopping_list=[]
list=[]
total=0
end_shopping_list=False

while(shopping_list!=True):
    print("1)view the cart 2) add item 3)delete item 4)calculate he total price ")
    print("your choice")
    choice=int(input())
    

    if choice==1:
        print("you have"+ str(len(list))+"list in your cart")
        print(list)
    elif choice==2:
        item_dict{'item':'price'}
        print("enter the item")
        item=str(input())
        
        shopping_list.append(item)
        print("enter the cost")
        cost=float(input())
        shopping_list.append(cost)
        list.append(shopping_list)
        shopping_list=[]
    elif choice==3:
        #end_shopping_list.pop()
        print("eneter the item to delete")
        item_to_delete=input()
        shopping_list.remove(item_to_delete)
    
    elif choice==4:
        print(" the total price of the shopping list")
        for i in range(len(list)):
            
            total+=list[i][1]
        print("the cost of the itm Rs=%.2f",total)    
    
    else:
        end_shopping_list=True

