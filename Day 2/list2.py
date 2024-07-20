my_list=list(map(int,input().split(",")))
print(f"1.append 2.pop 3.sort 4.len")
print("enter the choice")
choice=int(input())
if(choice==1):
    my_list.append(10)
    print(*my_list)
elif(choice==2):
    my_list.pop(2)
    print(*my_list)
elif(choice==3):
    my_list.sort(5)
    print(*my_list)
else:
    print((len(*my_list)))

