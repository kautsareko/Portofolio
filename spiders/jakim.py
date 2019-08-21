import scrapy
from ..items import JakimItem

class crawljakim(scrapy.Spider):
    name = 'jakim'
    page_number = 2
    #allowed_domains = ['http://www.halal.gov.my']
    start_urls = ['http://www.halal.gov.my/v4/index.php?data=ZGlyZWN0b3J5L2luZGV4X2RpcmVjdG9yeTs7Ozs=&negeri=14&category=PR&page=1&ty=PR']
    #start_urls = ['http://www.halal.gov.my/v4/directory/slm_viewdetail.php?comp_code=COMP-20100123-004526&type=C',
              #   'http://www.halal.gov.my/v4/directory/slm_viewdetail.php?comp_code=COMP-20100130-191337&type=C']

    def parse(self, response):
        list_of_row = response.xpath("//li[@class='clearfix search-result-data']")
        for row in list_of_row:
            item = JakimItem()

            product_name    = row.xpath(".//span[1]/text()").extract_first()
            product_brand   = row.xpath(".//span[3]//i/text()").extract_first()
            product_expire  = row.xpath(".//div[3]/text()").extract_first()

            item['product_name'] = product_name    
            item['product_brand'] = product_brand
            item['product_expire'] = product_expire

            yield item

        #-------------------------------------parse untuk sebelum per element-----------------------
        #items = JakimItem()

        #product_name    = response.xpath("//span[@class='company-name']/text()").extract()
        #product_brand   = response.xpath("//span[@class='company-address']//i/text()").extract()
        #product_expire  = response.xpath("//div[@class='search-date-expired']/text()").extract()

        #items ['product_name'] = product_name    
        #items ['product_brand'] = product_brand
        #items ['product_expire'] = product_expire

        #yield items
        #-------------------------------------------------------------------------------------------

        next_page = 'http://www.halal.gov.my/v4/index.php?data=ZGlyZWN0b3J5L2luZGV4X2RpcmVjdG9yeTs7Ozs=&negeri=14&category=PR&page=' + str(crawljakim.page_number) + '&ty=PR'
        if crawljakim.page_number <= 245:
             crawljakim.page_number += 1
             yield response.follow(next_page, callback = self.parse)