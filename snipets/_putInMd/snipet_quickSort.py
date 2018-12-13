
# quick sort

#%%


def quickSort(ls):
    """ returns the sorted list
    no random pivot here: we take the last element
    version presented [here](https://classroom.udacity.com/courses/ud513/lessons/7123524086/concepts/71181150370923) """

    if len(ls) <= 1:
        return ls
    else:
        ip = len(ls)-1
        i = 0
        
        while i < ip:
            if ls[i] > ls[ip]:
                # swap and move pivot
                tmp = ls[i]
                ls[i] = ls[ip-1]
                ls[ip-1] = ls[ip]
                ls[ip] = tmp
                ip -= 1
            else:
                # continue
                i += 1

        return quickSort(ls[:ip]) + [ls[ip]] + quickSort(ls[ip+1:])


ls = [8,37,5,8,93,2,63,64,87,44,5,7,26,4,76,83,5,8,56,7]
print(quickSort(ls))

