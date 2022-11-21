from Publication import Publication


class Book(Publication):
    def __init__(self, name, author):
        self.author = author
        super().__init__(name)

    def print_info(self):
        super().print_info()
        print(f"kirjoittaja nimi: {self.author}")
