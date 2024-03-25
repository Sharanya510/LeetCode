class Twitter:

    def __init__(self):
        self.time = 0
        self.posts = {}
        self.follows = {}
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        p = self.posts
        p[userId] = [(self.time, tweetId)] + p.get(userId, [])
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        users = list(self.follows.get(userId, set())) + [userId]
        feeds = []
        for u in users:
            tweets = copy.deepcopy(self.posts.get(u, []))
            if tweets:
                heapq.heappush(feeds, (tweets[0][0], tweets))
        news = []
        while feeds and len(news) < 10:
            _, tweets = heapq.heappop(feeds)
            news.append(tweets[0][1])
            tweets.pop(0)
            if tweets:
                heapq.heappush(feeds, (tweets[0][0], tweets))
        return news

    def follow(self, followerId: int, followeeId: int) -> None:
        f = self.follows
        s = f.get(followerId, set())
        s.add(followeeId)
        f[followerId] = s

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follows.get(followerId, set()).discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)