class Twitter:

    def __init__(self):
        self.t_count = 0
        # tweetMap, publisher: [(tweetID, tweetTime), ...]
        self.tweetMap = defaultdict(list)
        # followMap, follower: [followee0, ...]
        self.followMap = defaultdict(set)

        
    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.followMap:
            self.followMap[userId].add(userId)
        self.tweetMap[userId].append((tweetId, self.t_count))
        self.t_count+=1
        return

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.followMap:
            return []
        max_heap = [] # (tweetTime, tweetID, publisher, i)
        res = []
        for pub in self.followMap[userId]:
            if len(self.tweetMap[pub])>0:
                temp_tweet_id, temp_tweet_time = self.tweetMap[pub][-1]
                heapq.heappush(max_heap, (-temp_tweet_time, temp_tweet_id, pub, 1))

        while len(res)<10 and len(max_heap)>0:
            t_time, t_id, t_pub, t_i = heapq.heappop(max_heap)
            res.append(t_id)
            if len(self.tweetMap[t_pub])>=(t_i+1):
                temp_tweet_id, temp_tweet_time = self.tweetMap[t_pub][-t_i-1]
                heapq.heappush(max_heap, (-temp_tweet_time, temp_tweet_id, t_pub, t_i+1))
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followMap:
            self.followMap[followerId].add(followerId)
        if followeeId not in self.followMap:
            self.followMap[followeeId].add(followeeId)
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followMap:
            return
        try:
            self.followMap[followerId].remove(followeeId)
        except:
            return

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)