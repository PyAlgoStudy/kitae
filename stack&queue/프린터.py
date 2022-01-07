from collections import deque

def solution(priorities, location):
    answer = 0
    priorities=deque(priorities)
    while(True):
        print=priorities.popleft()
        if(len(priorities)==0):
            answer+=1
            break
        else:
            if(print>=max(priorities)):
                if(location==0):
                    answer+=1
                    break
                else:
                    answer+=1
                    location-=1
            else:
                if(location!=0):
                    location-=1
                    priorities.append(print)
                else:
                    location=len(priorities)
                    priorities.append(print)
    return answer
