class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        teamVotes = collections.defaultdict(lambda: [0] * len(votes[0]))
        for vote in votes:
            for pos, team in enumerate(vote):
                teamVotes[team][pos] += 1
        # print(teamVotes)
        # res = dict(sorted(teamVotes.items(), reverse = True, key = lambda x: (x[1], x[0])))
        # return ''.join(res.keys())
        return ''.join(sorted(teamVotes.keys(), reverse=True, key=lambda team: (teamVotes[team], -ord(team))))
    
#     dic = defaultdict(lambda : [0]*len(votes[0]))
#     for vote in votes:
#         for p,t in enumerate(vote):                # p-> postion(rank), t->teamName
#             dic[t][p]-=1
#     res = dict(sorted(dic.items(),key=lambda x: (x[1],x[0])))
	
#     return ''.join(res.keys())