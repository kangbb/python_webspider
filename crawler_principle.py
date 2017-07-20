#python爬虫伪代码

import Queue

initial_page = ""http://www.renminribao.com"  # 开始爬行的起点

url_queue = Queue.Queue() 
seen = set()  # 已经爬过的url

while(True):
	if url_queue.size() > 0: # 存储url里还有其他的url的队列
		current_url = url_queue.get() #拿出队例中第一个的url
		store(current_url)            #把这个url代表的网页存储好
		for next_url in extract_urls(current_url): # 提取这个url里链向的url
			if next_url not in seen:
				seen.put(next_url)
				url_queue.put(next_url)
	 else:
		break