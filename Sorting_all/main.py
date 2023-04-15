from quick_sort import *

def sorting(lst = str):
    lst = lst.split(",")
    lst1, lst2 = [], []
    for i in lst:
       lst2.append(i) if len(i) > 1 else lst1.append(i)
    lst.clear()
    lst = quick_sort(lst1)
    lst.extend(quick_sort(lst2))     
    return str(lst)

if __name__ == "__main__":
    a = "safyur,ramz,otti,aziz,dila,1,3,4,5,6,a,6,7,89,g,k,sab"
    print(sorting(a))