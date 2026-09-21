class Codec:

    def __init__(self):
        self.url_map = {}
        self.counter = 0

    def encode(self, longUrl):
        self.counter += 1

        shortUrl = "http://tinyurl.com/" + str(self.counter)

        self.url_map[self.counter] = longUrl

        return shortUrl

    def decode(self, shortUrl):
        key = int(shortUrl.split("/")[-1])

        return self.url_map[key]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))