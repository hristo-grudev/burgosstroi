import re

import scrapy

from scrapy.loader import ItemLoader
from w3lib.html import remove_tags

from ..items import BurgosstroiItem


class BurgosstroiSpider(scrapy.Spider):
	name = 'burgosstroi'
	start_urls = ['https://www.burgosstroi.com/']

	def parse(self, response):
		page_text = response.xpath('//div[@class="mymessage"]').getall()

		for p in page_text:
			description = remove_tags(p)
			description = re.sub(r"^[^:]+:", '', description).strip()
			print(description)
			item = ItemLoader(item=BurgosstroiItem(), response=response)
			item.add_value('description', description)

			yield item.load_item()

		old_news = response.xpath('//div[@style="text-align: right;"]/strong/a/@href')
		yield from response.follow_all(old_news, self.parse_old)

	def parse_old(self, response):
		page_text = response.xpath('//div[@class="entry-content"]/child::node()[normalize-space() and not(self::h2 | self::h3)]').getall()
		messages = []
		message = ''
		counter = 1
		for el in page_text:
			el = remove_tags(el).strip()
			if el[:5].isupper() and counter > 1:
				message = re.sub(r"^[^:]+:", '', message).strip()
				messages.append(message)
				message = ''
			counter += 1
			message += el
		message = re.sub(r"^[^:]+:", '', message).strip()
		messages.append(message)

		for m in messages:
			item = ItemLoader(item=BurgosstroiItem(), response=response)
			item.add_value('description', m)

			yield item.load_item()


