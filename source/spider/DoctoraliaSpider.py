import scrapy

from source.item.QstAnsItem import QstAnsItem


class DoctoraliaSpider(scrapy.Spider):


    def __init__(self, params):
        super(DoctoraliaSpider, self).__init__()
        self.start_url = params.start_url

    def parse_item(self, response):
        pass
        # self.logger.info('Hi, this is an item page! %s', response.url)
        # item = QstAnsItem()
        # item['qst'] = #response.xpath('//td[@id="item_description"]/text()').get()
        # item['ans'] =  # response.xpath('//td[@id="item_description"]/text()').get()
        # item['id'] = response.xpath('//td[@id="item_id"]/text()').re(r'ID: (\d+)')
        # item['name'] = response.xpath('//td[@id="item_name"]/text()').get()
        # item['description'] = response.xpath('//td[@id="item_description"]/text()').get()
        # item['link_text'] = response.meta['link_text']
        # url = response.xpath('//td[@id="additional_data"]/@href').get()
        # return response.follow(url, self.parse_additional_page, cb_kwargs=dict(item=item))

    def parse_additional_page(self, response, item):
        item['additional_data'] = response.xpath('//p[@id="additional_data"]/text()').get()
        return item