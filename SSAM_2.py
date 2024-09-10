#!/usr/bin/env python
# coding: utf-8

# # Sophie Samuels COP3035 HW4 Z23748744

# Exercise 1: Simple Library System
# Background: Create a system to manage books and users within a library.
# Tasks:
# • Define a Book class with attributes for title, author, and ISBN.
# • Define a User class with attributes for the user's name and a list of borrowed books.
# • Implement methods in the User class for borrowing and returning books.
# • Demonstrate the system's functionality with examples of several Book and User objects in
# action.

# ## Simple Library System
# ### Create a system to manage books and users within a library

# In[1]:


#Define a Book class with attributes for title, author, and ISBN

class Book:
    
    def __init__(self, title, author, ISBN):
        self.title = title
        self.author = author
        self.ISBN = ISBN

#Define a User class with attributes for the user's name and a list of borrowed books

class User:
    
    def __init__(self, name):
        self.name = name
        self.borrowedbooks = []
        
#Implement methods in the User class for borrowing and returning books     

    def add_book(self, string_borrowedbooks):
        self.borrowedbooks.append(string_borrowedbooks)
        
    def return_book(self, string_borrowedbooks):
            self.borrowedbooks.remove(string_borrowedbooks)
            
##I have added the method print_books to produce a string of books each user currently is borrowing
        
    def print_books(self):
        borrowedbooks_string = ", ".join([book.title for book in self.borrowedbooks])
        print(f"{self.name} is borrowing: {borrowedbooks_string}")


# In[2]:


#Demonstrate the system's functionality with examples of several Book and User objects in action
        
book1 = Book("The Hobbit", "J.R.R. Tolkien", "0-8057-8807-7")
book2 = Book("War and Peace", "Leo Tolstoy", "1-85326-062-2")
book3 = Book("1984", "George Orwell", "0-451-52493-4")
book4 = Book("The Old Man and the Sea", "Ernest Hemmingway", "0-68416-326-8")

user1 = User("Phil Styles")
user2 = User("Kate Lemons")


# In[3]:


user1.add_book(book1)
user1.print_books()


# In[4]:


user2.add_book(book2)
user2.add_book(book3)
user2.add_book(book4)
user2.print_books()


# In[5]:


user2.return_book(book2)
user2.return_book(book4)
user2.print_books()


# In[ ]:




