#slave.py
#只负责抓取当前网页内存在的链接、向master发送链接

current_url = request_from_master()
to_send = []
for next_url in extract_urls(current_url)
	to_send.append(next_url)

store(current_url)
send_to_master(to_send)



#master.py
#负责确定未抓取的链接、存储已抓取的链接、向slave发送链接

distributed_queue = DistributedQueue()
bf = BloomFilter() # 搜索未抓取的链接

initial_page = "www.renmingribao.com"
while(True):
	if request == 'GET': # 仅请求资源
		if(distributed_queue.size()>0:
			send(distributed_queue.get())
		else:
			break
	elif request == 'POST': # 请求资源+用户数据(html中的body)
		bf.put(request.url)