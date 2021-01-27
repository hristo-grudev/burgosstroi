BOT_NAME = 'burgosstroi'

SPIDER_MODULES = ['burgosstroi.spiders']
NEWSPIDER_MODULE = 'burgosstroi.spiders'
FEED_EXPORT_ENCODING = 'utf-8'
LOG_LEVEL = 'ERROR'
DOWNLOAD_DELAY = 0

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
	'burgosstroi.pipelines.BurgosstroiPipeline': 100,

}