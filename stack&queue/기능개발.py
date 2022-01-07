from collections import deque
import math

def solution(progresses, speeds):
    deqProgresses = deque(progresses)   # 시간 복잡도를 위해 deque로 선언
    deqSpeeds = deque(speeds)   # 시간 복잡도를 위해 deque로 선언
    answer = []
    while(len(deqProgresses)!=0):
        count=0
        upgrade=math.ceil((100-deqProgresses[0])/deqSpeeds[0])  # 맨 앞의 기능개발이 100이상이 되는데 걸리는 시간
        for i in range(len(deqProgresses)):
            deqProgresses[i]+=upgrade*deqSpeeds[i]
        while(True):
            if(deqProgresses[0]>=100):
                deqProgresses.popleft()
                deqSpeeds.popleft()    
                count+=1
                if(len(deqProgresses)==0):
                    answer.append(count)
                    break
            else:
                answer.append(count)
                break
    return answer
