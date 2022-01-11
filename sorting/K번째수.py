def solution(array, commands):
    answer=[]
    for k in range(len(commands)):
        newArray=array[commands[k][0]-1:commands[k][1]]
        newArray.sort()
        answer.append(newArray[commands[k][2]-1])
    return answer
