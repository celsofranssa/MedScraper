import scrapy
from source.item.QstAnsItem import QstAnsItem


class DoctoraliaSpider(scrapy.Spider):

    def __init__(self, start_urls):
        self.start_urls = start_urls
        self.name = "Doctor_Spider"
        super(DoctoraliaSpider, self).__init__()

    def parse(self, response):
        num_qst = 0
        for qst_page in response.xpath("//div[@class='dp-q-and-a']//a[@class='text-body']/@href").getall():
            num_qst += 1
            yield response.follow(qst_page, self.parse_qst)
        self.logger.info(f"Got {num_qst} questions from {response.url}")

        next_page = response.xpath("//a[contains(@class,'page-link-next')]/@href").get()
        if next_page is not None:
            self.logger.info(f"Creating request {next_page}")
            yield response.follow(next_page, self.parse, errback=self._errback)

    def parse_qst(self, qst):

        item = QstAnsItem()
        a = qst.xpath("//div[contains(@class,'doctor-question-body')]/text()").extract()
        item['question'] = " ".join(a).strip()

        answers = []
        for ans in qst.xpath("//div[contains(@class,'doctor-answer-content')]"):
            ans = "".join(ans.xpath(".//text()").extract())

            answers.append(ans.strip().replace("\n", " "))
        item['answers'] = answers

        yield item

    def _errback(self):
        self.logger.info(f"ERROR")

