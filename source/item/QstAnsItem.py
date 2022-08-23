from scrapy import Field, Item


class QstAnsItem(Item):
    question = Field()
    answers = Field()
