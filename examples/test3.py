from opinionx.text import get_leader_opinions
from quick_crawler.page import quick_read_csv_model
text=open("test.txt",'r',encoding='utf-8').read()

for news in quick_read_csv_model("data/dataset-china5e.csv"):
    text=news["text"]
    list_opinion = get_leader_opinions(text, save_path="", search_keywords_path="data/search_keywords.csv",
                                       leader_path="data/g20_leaders.csv")
    if len(list_opinion)!=0:
        for opinion in list_opinion:
            print(opinion["opinion"])
            # print(opinion["first_found_keyword"])
            # print(opinion["first_found_leader"])
            # print()
        print()


