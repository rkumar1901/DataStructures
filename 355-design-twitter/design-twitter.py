from collections import defaultdict
class Twitter(object):

    def __init__(self):
        self.tweets = defaultdict(list)   # userId -> [(time, tweetId)]
        self.following = defaultdict(set) # userId -> set of followees
        self.time = 0

    def postTweet(self, userId, tweetId):
        self.time += 1
        self.tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId):
        heap = []

        # user should follow themselves
        self.following[userId].add(userId)

        for followee in self.following[userId]:
            tweets = self.tweets[followee]

            # take last tweet (most recent)
            if tweets:
                time, tweetId = tweets[-1]
                idx = len(tweets) - 1
                heapq.heappush(heap, (-time, tweetId, followee, idx))

        res = []

        while heap and len(res) < 10:
            time, tweetId, user, idx = heapq.heappop(heap)
            res.append(tweetId)

            # move to next tweet of same user
            if idx - 1 >= 0:
                time, tweetId = self.tweets[user][idx - 1]
                heapq.heappush(heap, (-time, tweetId, user, idx - 1))

        return res

    def follow(self, followerId, followeeId):
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        if followeeId != followerId:
            self.following[followerId].discard(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)