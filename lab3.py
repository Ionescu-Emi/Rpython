# 1
def setops(a,b):
    return [set(a).intersection(set(b)),set(a).union(set(b)),set(a)-set(b),set(b)-set(a)]
#print(setops([1,2,3],[1,2,5]))
#2 
def occChar(str):
    occs={}
    for i in str:
        if (i not in occs):
            occs[i]=1
        else: occs[i]+=1
    return occs
#print(occChar("Ana has apples"))
#5
def validate_dict(rules, dictionary):
    for key, sir in dictionary.items():
        has_rule=False
        for key_r,prefix,middle,suffix in rules:
            
            if(key==key_r):
                if ((len(prefix)!=0) and not sir.startswith(prefix)) or (len(suffix)!=0 and (not sir.endswith(suffix))) or len(middle)!=0 and middle not in sir[len(prefix):len(sir)-len(suffix)]:
                    return False
                has_rule=True
        if not has_rule:
            return False
    
    return True

rules = {("key1", "", "inside", ""), ("key2", "start", "middle", "winter")}
dictionary = {"key1": "come inside, it's too cold out","key3":"this is not valid"}

result = validate_dict(rules, dictionary)
print(result)
#6
def uniqDupl(l):
    occs={}
    for i in l:
        if(i not in occs):
            occs[i]=1
        else:
            occs[i]+=1
    uniq=0
    for i in l:
        if(occs[i]==1):
            uniq+=1
    return uniq,len(l)-uniq 


#print(uniqDupl([1,2,3,2,2,3,3,3]))
#7
def set_operations(*sets):

    
    result = {}
    
    for i in range(len(sets)):
        for j in range(i + 1, len(sets)):
            set1 = sets[i]
            set2 = sets[j]
            
            key = f"{set1} | {set2}"
            result[key] = set1 | set2
            
            key = f"{set1} & {set2}"
            result[key] = set1 & set2
            
            key = f"{set1} - {set2}"
            result[key] = set1 - set2
            
            key = f"{set2} - {set1}"
            result[key] = set2 - set1
    
    return result
#print(set_operations(set([1,2,3]),set([2,3,4])))
#10 
def loop(mapping):
    visited=set()
    rlist=[]
    key=mapping['start']
    rlist+=[key]
    visited.add('start')
    while(True):
        if(key not in mapping):
            break
        key=mapping[key]
        if(key in visited):
            break
        rlist+=[key]
        visited.add(key)
    return rlist


#11
def count_matching_arguments(*args, **kwargs):
    count = 0
    
    for arg in args:
        if arg in kwargs.values():
            count += 1
    
    return count
result = count_matching_arguments(1, 2, 3, 4, x=1, y=2, z=3, w=5)
#print(result)  # Output: 3