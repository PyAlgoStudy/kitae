def solution(numbers):
    strNumbers=list(map(str,numbers))
    strNumbers.sort(key=lambda x:4*x,reverse=True)
    answer=''.join(strNumbers)
    if(answer[0]=='0'):
        answer='0'
    return answer
