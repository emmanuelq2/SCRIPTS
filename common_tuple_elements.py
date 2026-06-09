

def common_tuple_elements_traversing(sourceArray, searchArray):
    
    result = []
    for n_source, l_source in sourceArray:
        for n_search, l_search in searchArray:
            if n_source <= n_search and l_source in l_search:
                result.append((n_source, l_source))
                break
    return result