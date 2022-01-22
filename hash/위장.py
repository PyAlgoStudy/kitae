def solution(clothes):
    answer = 1
    clothesType=dict()
    for cloth in clothes:
        if(cloth[-1] in clothesType):
            clothesType[cloth[-1]]+=1
        else:
            clothesType[cloth[-1]]=1
    for type in clothesType:
        answer*=(clothesType[type]+1)
    return answer-1
