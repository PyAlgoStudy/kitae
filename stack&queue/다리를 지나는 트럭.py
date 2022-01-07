from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge=deque([0]*bridge_length)
    index=0
    sumBridge=0
    while(True):
        out=bridge.pop()
        sumBridge-=out
        if(truck_weights[index]+sumBridge<=weight):
            bridge.appendleft(truck_weights[index])
            sumBridge+=truck_weights[index]
            index+=1
        else:
            bridge.appendleft(0)
        answer+=1
        if(index==len(truck_weights)):
            answer+=(len(bridge))
            break
    return answer
