def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    for k in range(len(completion)):
        if(completion[k]!=participant[k]):
            answer=participant[k]
            break
    if(answer==''):
        answer=participant[-1]
    return answer
    
    
participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]
solution(participant, completion)
