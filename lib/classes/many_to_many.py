class Article:
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        
class Author:
    def __init__(self, name):
        self.name = name
        self.authored_articles = []

    def articles(self):
        return self.authored_articles

    def magazines(self):
        return list({article.magazine for article in self.authored_articles})

    def add_article(self, magazine, title):
        new_article = Article(self, magazine, title)
        self.authored_articles.append(new_article)

    def topic_areas(self):
        return list({article.magazine.category for article in self.authored_articles})


class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    def articles(self):
        pass

    def contributors(self):
        pass

    def article_titles(self):
        pass

    def contributing_authors(self):
        pass