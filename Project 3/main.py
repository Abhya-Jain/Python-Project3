class Library:

    def __init__(self, listOfBooks):
        self.books = listOfBooks

    def displayAvailableBooks(self):
        print("Books present in this library are: ")
        for book in self.books:
            print(" * " + book)

    def borrowBook(self, bookName):
        if bookName in self.books:
            print(f"You have been issued {bookName}. keep it safe and return on time")
            self.books.remove(bookName)
            return True
        else:
            print("Sorry, either this book is not availabe or issued to someone else , wait until the book is available")
            return False
        
    def returnBook(self,bookName):
        self.books.append(bookName)
        print("Thanks for adding\returning the book, hope you enjoyed reading it!")
    

class Student:
    
    def requestBoook(self):
        self.book = input("Enter then name of the book you want to borrow: ")
        return self.book
    
    def returnBook(self):
        self.book = input("Enter then name of the book you want to return: ")
        return self.book
    

if __name__ =="__main__":
    centralLibrary = Library(["Algorithms", "Django", "CLRS", "Python", ])
    Student = Student()
    # centralLibrary.displayAvailableBooks()
    while(True):
        welcomeMsg = '''\n ======= Welcome to Central Library ======
        Please choose option: 
        1. List all the books
        2. Request a book
        3. Add\Return a book
        4. Exit the Library
        '''

        print(welcomeMsg)
        a = int(input("Enter a choice: "))
        if a == 1:
            centralLibrary.displayAvailableBooks()
        elif a == 2:
            centralLibrary.borrowBook(Student.requestBoook())
        elif a == 3:
            centralLibrary.returnBook(Student.returnBook())
        elif a == 4:
            print("Thanks for choosing central library.")
            exit()
        else:
            print("Invalid Choice")

        