class Content:
    def __init__(self, title: str, text: str):
        self.title = title
        self.text = text


class Article(Content):
    def __init__(self, title, text, is_breaking_news=False):
        super().__init__(title, text)
        self.is_breaking_news = is_breaking_news

    def display(self):
        displayed_title = (
            f"BREAKING: {self.title}" if self.is_breaking_news else self.title
        )
        return f"<h2>{displayed_title}</h2><p>{self.text}</p>"


class Ad(Content):
    def display(self):
        return f"<h2>{self.title.upper()}</h2><p>{self.text}</p>"


class Vacancy(Content):
    def display(self):
        return f"<h2>{self.title} - apply now!</h2><p>{self.text}</p>"


articles = [
    Article("Python Basics", "Learn the fundamentals of Python programming."),
    Article("Han is learning Python", "Python is the future!", is_breaking_news=True),
    Ad("Special Offer", "Get 20% off on selected items!"),
    Vacancy("Software Engineer", "Join our team and work on exciting projects"),
]

for content in articles:
    print(content.display())
