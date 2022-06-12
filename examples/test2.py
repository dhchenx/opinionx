from opinionx.text import get_leader_opinions

text=open("test.txt",'r',encoding='utf-8').read()

list_opinion = get_leader_opinions(text,save_path="", search_keywords_path="data/search_keywords.csv",leader_path="data/g20_leaders.csv")
print()
for opinion in list_opinion:
    print(opinion)
    print(opinion["opinion"])
    print(opinion["first_found_keyword"])
    print(opinion["first_found_leader"])
    print()
