import scrapy


class LightingparsSpider(scrapy.Spider):
    name = "lightingpars"
    allowed_domains = ["https://divan.ru"]
    start_urls = ["https://www.divan.ru/category/svet"]

    def parse(self, response):
        lights = response.css('div._Ud0k')
        for light in lights:
            yield {
                'name': light.css('div.lsooF span::text').get(),
                'price': light.css('div.tPt2t span::text').get(),
                'url': light.css('a').attrib['href']
            }

