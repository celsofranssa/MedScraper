import scrapy


class QstAnsItem(scrapy.Item):

    def __init__(self):
        super(QstAnsItem, self).__init__()
        self.qst = scrapy.Field()
        self.ans = scrapy.Field()
