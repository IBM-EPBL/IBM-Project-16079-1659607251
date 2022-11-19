
from gnewsclient import gnewsclient

client = gnewsclient.NewsClient(language='english',
                                location='india',
                                topic='sports',
                                max_results=3)

news_list = client.get_news()
for item in news_list:


    print(item['title'])


    print("Title : ", item['title'])
    print("Link : ", item['link'])
    print("")