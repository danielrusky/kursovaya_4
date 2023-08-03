class Vacancy:
    def __init__(self, name, salary_from, salary_to, url, info, responsibility):
        self.name = name
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.url = url
        self.info = info
        self.responsibility = responsibility

    def __repr__(self):
        return self.name

    def __str__(self):
        return f"{self.name}\n{self.url}"

    def __lt__(self, other):
        return self.salary_to < other.salary_to






