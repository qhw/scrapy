# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html

class DmozPipeline(object):
	def process_item(self, item, spider):
		print item['title']
      	  	return item
	
	def open_spider(self, spider):
		print 'open spider'
	
