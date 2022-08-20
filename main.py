import os

import hydra
import scrapy
from omegaconf import OmegaConf
from scrapy.crawler import CrawlerProcess

from source.spider.DoctoraliaSpider import DoctoraliaSpider


class MySpider(scrapy.Spider):
    # Your spider definition
    ...


@hydra.main(config_path="setting", config_name="settings.yaml", version_base=None)
def perform_tasks(settings):
    os.chdir(hydra.utils.get_original_cwd())
    OmegaConf.resolve(settings)
    process = CrawlerProcess(settings=settings)

    spider = DoctoraliaSpider(settings)

    process.crawl(spider)
    # the script will block here until the crawling is finished
    process.start()


if __name__ == '__main__':
    perform_tasks()
