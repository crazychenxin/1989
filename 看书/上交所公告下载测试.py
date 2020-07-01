import requests

r = requests.get('http://query.sse.com.cn/security/stock/queryCompanyBulletin.do?jsonCallBack=jsonpCallback82873&isPagination=true&productId=&keyWord=%E9%80%80%E5%B8%82%E6%95%B4%E7%90%86%E6%9C%9F%E4%BA%A4%E6%98%93&securityType=0101%2C120100%2C020100%2C020200%2C120200&reportType2=&reportType=ALL&beginDate=2020-06-28&endDate=2020-06-30&pageHelp.pageSize=25&pageHelp.pageCount=50&pageHelp.pageNo=1&pageHelp.beginPage=1&pageHelp.cacheSize=1&pageHelp.endPage=5&_=1593502879059',
                headers={'Referer':'http://www.sse.com.cn/disclosure/listedinfo/announcement/'})

print(r.text)