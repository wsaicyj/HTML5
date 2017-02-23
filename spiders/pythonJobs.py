from scrapy import Field,Item

class PythonjobsItem(Item):
    title = Field()
    city = Field()
    company = Field()
    location = Field()
    url = Field()
