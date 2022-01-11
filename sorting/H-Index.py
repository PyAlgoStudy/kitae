def solution(citations):
    citations.sort(reverse=True)
    citation=0
    while(True):
        count=0
        for k in range(len(citations)):
            if(citation<=citations[k]):
                count+=1
            else:
                break
        if(citation>count):
            return citation-1
        citation+=1
