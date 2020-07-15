import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'https://crea-am.org.br/src/site/licitacao.php',
    ]

    def parse(self, response):
        for li in response.css('li'):
            yield {
                'licitacao': li.xpath('p/text()').get(),
                'data': li.xpath('span/text()').get(),
            }