import scrapy

class TermekekSpider(scrapy.Spider):
    name = "termekek"
    start_urls = ["https://kallofem.hu/shop/group/keriteselemek"]

    def parse(self, response):
        for termek in response.css('article.product-row'):
            yield {
                'termeknev': termek.css('h4::text').get(default='').strip(),
                'ar': termek.css('span.product-price::text').get(default='').strip(),
                'kep_url': response.urljoin(termek.css('img::attr(src)').get())
            }

        kovetkezo_oldal = response.css('a.page-link[rel="next"]::attr(href)').get()
        if kovetkezo_oldal:
            yield response.follow(kovetkezo_oldal, callback=self.parse)
