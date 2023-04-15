from random import randint

def quick_sort(items = []):

    if len(items) < 2:
        return items
    
    low, mid, high = [], [], []
    middle = items[len(items)//2]

    for i in items:
        if i < middle:
            low.append(i)
        elif i > middle:
            high.append(i)
        else:
            mid.append(i)
    return quick_sort(low)+ mid + quick_sort(high)

if __name__ == "__main__":
    # lst = [randint(1,50) for i in range(20)]
    lst = ["safyur", "aziz", "abi", "safb"]
    print(lst)
    a = quick_sort(lst)
    print(a)