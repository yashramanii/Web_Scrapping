import scrapy

class newsSpider(scrapy.Spider):
    name = "news"

    start_urls = [
        'https://news.google.com/topics/CAAqJQgKIh9DQkFTRVFvSUwyMHZNRE55YXpBU0JXVnVMVWRDS0FBUAE?hl=en-IN&gl=IN&ceid=IN%3Aen'
    ]

    def parse(self, response):
        news_title = response.css('h3.ipQwMb ekueJc RD0gLb').extract()

        yield {'Title' : news_title}