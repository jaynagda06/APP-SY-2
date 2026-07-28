def title_decorator(func):
    def wrapper(self):
        print("=" * 40)
        func(self)
        print("=" * 40)
    return wrapper


class Report:
    template = "General Report"

    def __init__(self, title, content):
        self.title = title
        self.content = content

    @classmethod
    def set_template(cls, name):
        cls.template = name

    @title_decorator
    def display(self):
        print("Template :", Report.template)
        print("Title    :", self.title)
        print("Content  :", self.content)

    def __str__(self):
        return self.title

    def __len__(self):
        return len(self.content)


Report.set_template("Student Report")

r1 = Report("Python Project", "This report explains the project using basic Python concepts.")

r1.display()

print("Report Name :", r1)
print("Content Length :", len(r1))