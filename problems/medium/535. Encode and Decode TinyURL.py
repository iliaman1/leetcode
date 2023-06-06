class Codec:
    basket = {}
    counter = 0

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        self.basket[str(self.counter)] = longUrl
        self.counter += 1
        return str(self.counter - 1)

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.basket[shortUrl]


if __name__ == '__main__':
    url = "https://leetcode.com/problems/design-tinyurl"
    codec = Codec()
    assert codec.decode(codec.encode(url)) == url
