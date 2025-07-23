# problem-18---> flat multidimention list --->
# [1, [2, 3], [4, [5, 6]]] → [1, 2, 3, 4, 5, 6]

numsList = [11,14,[1, [[2, 3], [4, [5, 6]],[9, 8]]]]

def flatMultiDimList(nsList):
    flat_list =[]
    for item in nsList:
        if isinstance(item,list):
            flat_list.extend(flatMultiDimList(item))
        else:
            flat_list.append(item)
    return flat_list
print(flatMultiDimList(numsList))