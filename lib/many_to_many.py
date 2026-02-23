class Author:
    all = []
    
    def __init__(self, name):
        self.name = name
        self.contracts = []
        Author.all.append(self)
    
    def add_contract(self, contract):
        self.contracts.append(contract)
    
    def contracts(self):
        return self.contracts
    
    def books(self):
        books = []
        for contract in self.contracts:
            books.append(contract.book)
        return books
    
    def sign_contracts(self, book, date, royalties):
        contract = Contract(self, book, date, royalties)
        return contract
    
    def total_royalties(self):
        total = 0
        for contract in self.contracts:
            total += contract.royalties
        return total

class Book:
    all = []
    
    def __init__(self, title):
        self.title = title
        self.contracts = []
        Book.all.append(self)
    
    def add_contract(self, contract):
        self.contracts.append(contract)
    
    def contracts(self):
        return self.contracts
    
    def authors(self):
        authors = []
        for contract in self.contracts:
            authors.append(contract.author)
        return authors

class Contract:
    all = []
    
    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)
    
    def contracts_by_date(self, date):
        contracts = []
        for contract in Contract.all:
            if contract.date == date:
                contracts.append(contract)
        return contracts
    pass