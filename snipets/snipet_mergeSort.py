
# merge sort

#%%

def mergeSort(ls):
    """ returns a new list sorted """
    
    def merge(ls1, ls2):
        """ returns the merge of two *sorted* lists """
        i1, i2 = 0, 0
        n1, n2 = len(ls1), len(ls2)
        ls = []
    
        while i1 < n1 and i2 < n2: # maybe better to use .pop() ...
            a1, a2 = ls1[i1], ls2[i2]
            if a1 <= a2:
                ls.append(a1)
                i1 += 1
            else:
                ls.append(a2)
                i2 += 1
        if i1 == n1:
            ls += ls2[i2:] # ... pecifically to avoid using [i2:] ...
        if i2 == n2:
            ls += ls1[i1:]
    
        return ls

    n = len(ls)
    if n <= 1:
        return ls
    else:
        m = int(n/2)
        lsL = ls[:m]
        lsR = ls[m:]
        
        lsL_sorted = mergeSort(lsL)
        lsR_sorted = mergeSort(lsR)

        ls_merged = merge(lsL_sorted, lsR_sorted)

        return ls_merged



ls = [10, 38, 28, 34, 59, 84, 46, 17, 4, 8, 47, 10]
print(mergeSort(ls))
ls = 'dfhhtupoutntbhc3806tgnqwexfd5cuv93ygyh'
print(mergeSort(ls))
ls = []
print(mergeSort(ls))