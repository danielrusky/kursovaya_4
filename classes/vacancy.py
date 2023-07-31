class Vacancy:

    def __init__(self, title, url, salary, experience):
        self.title = title
        self.url = url
        self.salary = salary
        self.experience = experience

    def to_dict(self):
        return {
            "title": self.title,
            "url": self.url,
            "salary": self.salary,
            "experience": self.experience
        }

    def __str__(self):
        return f"{self.title}\n{self.url}"

    def __lt__(self, other):
        return self.salary < other.salary

#
