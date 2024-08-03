class meeting:
    def __init__(self, start, end, pos):
        self.start = start
        self.end = end
        self.pos = pos
        
        
class Solution:
    def maximumMeetings(self,n,start,end):
        meet=[meeting(start[i],end[i],i+1) for i in range(n)]
        meet=sorted(meet, key=lambda x: (x.end,x.pos))
        answer=[]
        limit= meet[0].end
        answer.append(meet[0].pos)
        for i in range(1,n):
            if meet[i].start>limit:
                limit=meet[i].end
                answer.append(meet[i].pos)
        return len(answer)