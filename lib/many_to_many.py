class Author:
    all = []

    def __init__(self, name):
        self.name = name
        self._contracts = []
        Author.all.append(self)

    def add_contract(self, contract):
        # minimal: append without extra checks (creation validates)
        self._contracts.append(contract)

    def contracts(self):
        return list(self._contracts)

    def books(self):
        return [c.book for c in self._contracts]

    def sign_contract(self, book, date, royalties):
        # create and return Contract; Contract will wire up relations
        return Contract(self, book, date, royalties)

    # keep backwards compatibility if tests used sign_contracts previously
    sign_contracts = sign_contract

    def total_royalties(self):
        total = 0
        for contract in self._contracts:
            total += contract.royalties
        return total


class Book:
    all = []

    def __init__(self, title):
        self.title = title
        self._contracts = []
        Book.all.append(self)

    def add_contract(self, contract):
        self._contracts.append(contract)

    def contracts(self):
        return list(self._contracts)

    def authors(self):
        return [c.author for c in self._contracts]


class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        # validations per rubric
        if not isinstance(author, Author):
            raise Exception("author must be Author")
        if not isinstance(book, Book):
            raise Exception("book must be Book")
        if not isinstance(date, str):
            raise Exception("date must be str")
        if not isinstance(royalties, int):
            raise Exception("royalties must be int")
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        # add to global and wire to each side
        Contract.all.append(self)
        author.add_contract(self)
        book.add_contract(self)

    @classmethod
    def contracts_by_date(cls, date):
        return [c for c in cls.all if c.date == date]