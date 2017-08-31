#[1,[2,3],[4,[5,[6,7]]]] on reverse should give
#[[[[7,6],5],4],[3,2],1]
#WORKING
def deep_rev(p):
    if isinstance(p,list):
        result=[]
        for i in range(len(p)-1 , -1 , -1):
            result.append(deep_rev(p[i]))
        return result
    else:
        return p

print(deep_rev([1,[2,3],[4,[5,[6,7]]]]))


