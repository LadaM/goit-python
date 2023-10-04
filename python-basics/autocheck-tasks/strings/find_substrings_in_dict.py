articles_dict = [
    {
        "title": "Endless ocean waters.",
        "author": "Jhon Stark",
        "year": 2019,
    },
    {
        "title": "Oceans of other planets are full of silver",
        "author": "Artur Clark",
        "year": 2020,
    },
    {
        "title": "An ocean that cannot be crossed.",
        "author": "Silver Name",
        "year": 2021,
    },
    {
        "title": "The ocean that you love.",
        "author": "Golden Gun",
        "year": 2021,
    },
]


def find_articles(key: str, letter_case=False):
    result = []
    for article in articles_dict:
        title = str(article.get("title"))
        match_title = is_matching(key, letter_case, title)
        author = str(article.get("author"))
        match_author = is_matching(key, letter_case, author)
        if match_title or match_author:
            result.append(article)
    print(len(result))
    return result
    

def is_matching(key: str, letter_case: bool, title: str):
    return title.find(key) != -1 if letter_case else title.lower().find(key.lower()) != -1

# find_articles('ocean')
# find_articles('Ocean', letter_case=True) # expecting 1 res
# find_articles('silver') # 2 res 
# find_articles('Silver', letter_case=True) # 1 res
find_articles('Florida', letter_case=True) # 0
