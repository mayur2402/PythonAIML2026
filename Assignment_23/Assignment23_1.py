class BookStore:
    NOOFBOOKS = 0
    def __init__(self,name,author):
        self.name = name
        self.author = author
        BookStore.NOOFBOOKS += 1

    def display(self):
        print(self.name + " by " + self.author + " No of books :" + str(BookStore.NOOFBOOKS))
    
ob1 = BookStore("Linux","Linux")
ob1.display()
ob2 = BookStore("windows","windows")
ob2.display()