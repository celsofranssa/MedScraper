from scrapy import Field, Item


class QstAnsItem(Item):
    qst = Field()
    ans = Field()
