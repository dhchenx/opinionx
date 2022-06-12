from autobr.baidu import BaiduNewsSearch
'''
    pip install autobr
'''

baidu_pages=BaiduNewsSearch(
    raw_keywords="俄罗斯 双碳",
    webdriver_path="browsers/chromedriver.exe",
    save_path="data/list_search_news_result.txt",
    max_pages=100
)

baidu_pages.fetch()

