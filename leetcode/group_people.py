# Helper Fxn -----------------------------------------------
def create_and_add_in_group(new_g_size, unique_id):
    if new_g_size == 1:
        record.append([[unique_id], new_g_size, False])
    else:
        record.append([[unique_id], new_g_size, True])

def find_empty_group(size):

    for pos, rec in enumerate(record):
        if rec[1] == size and rec[2]:
            return pos
    return -1

def add_id_in_group(pos, unique_id):
    record[pos][0].append(unique_id)
    if len(record[pos][0]) == record[pos][1]:
        record[pos][2] = False
        
# main Fxn -----------------------------------------------

def groupThePeople(groupSizes: List[int]) -> List[List[int]]:

    global record
    record = []
    for i,v in enumerate(groupSizes):
        empty_group = find_empty_group(v) # Check if any group of given size in empty or not
        if empty_group != -1 :
             add_id_in_group(empty_group, i)
        else:
            create_and_add_in_group(v, i)
    out = [i[0] for i in record]
    return out

# Faster Soln -----------------------------------------------

def groupThePeople(groupSizes: List[int]) -> List[List[int]]:

    record = defaultdict(list)
    for i,v in enumerate(groupSizes):
        record[v].append(i)
    print(record)
    out = []
    for i in record.keys():
        count = 0
        temp = []
        for j in record[i]:
            if count != i:
                temp.append(j)
                count += 1
            else:
                out.append(temp)
                temp = [j]
                count = 1
        out.append(temp)
    return out
                  
