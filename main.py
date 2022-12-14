import os

import hydra
import scrapy
from omegaconf import OmegaConf
from scrapy.crawler import CrawlerProcess

from source.spider.DoctoraliaSpider import DoctoraliaSpider


def scrape(disease, start_urls):
    settings = {
        "USER_AGENT": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36",
        "HTTPCACHE_ENABLED": True,
        "ROBOTSTXT_OBEY": False,
        "LOG_LEVEL": 'INFO',
        "EXTENSIONS": {
            'scrapy.telnet.TelnetConsole': None
        },
        "DOWNLOAD_TIMEOUT": 30,
        "CONCURRENT_REQUESTS": 4,
        "FEEDS": {
            f"resource/data/{disease}.jsonl": {"format": "jsonlines", 'encoding': 'utf8'},
        }
    }

    process = CrawlerProcess(settings=settings)  # settings=settings.crawler_process)
    process.crawl(DoctoraliaSpider, start_urls)
    # # the script will block here until the crawling is finished
    process.start()




if __name__ == '__main__':
    start_urls = ["https://www.doctoralia.com.br/doencas/diabetes/perguntas"]
    disease = "diabetes"
    scrape(disease, start_urls)
