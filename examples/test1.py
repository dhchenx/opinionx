from opinionx.text import get_opinion

text=open("test.txt",'r',encoding='utf-8').read()
opinion_words=['表示','认为','说','介绍','提出','透露','指出','强调','：']
list_opinion,_,_=get_opinion(text,lang='zh',opinion_words=opinion_words)
for opinion in list_opinion:
    print(opinion)