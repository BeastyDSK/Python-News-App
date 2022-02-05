import json
from urllib3 import PoolManager

def getNewsData(topic=None):
    """
    Used to get the latest news feed from Bing News API.
    """
    http = PoolManager()
    url = f"https://bing-news-search1.p.rapidapi.com/news/search?count=10&freshness=Day&textFormat=Raw&safeSearch=Off&originalImg=true&q={topic}" if topic!=None else "https://bing-news-search1.p.rapidapi.com/news?count=10&freshness=Day&textFormat=Raw&safeSearch=Off&originalImg=true"

    header = {
        "x-rapidapi-host": "bing-news-search1.p.rapidapi.com",
        "x-rapidapi-key": "95659ef623msh1d168c347be55b1p107a62jsnf8575138f456"
	}
    resp = http.request_encode_url(method="GET",url=url,headers=header)
    resp = json.loads(resp.data.decode("utf-8"))
    return resp['value']
