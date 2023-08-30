# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 09:32:45 2023

@author: samme
"""

#Biblioteca V1
import csv
import os

class Book:
    def __init__(self, title, author, genre, year) -> None:
        self.title = title
        self.author = author
        self.genre = genre
        self.year = year

class Library:
    def __init__(self, filename='library.csv') -> None:
        self.books = []
        self.filename = filename
        self.loadBooksFromCSV()

    def addBook(self, book):
        self.books.append(book)
        self.saveBookToCSV(book)

    def showBooks(self):
        if not self.books:
            print('No hay libros')
        else:
            for book in self.books:
                print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
                print(f'Titulo: {book.title}')
                print(f'Autor: {book.author}')
                print(f'Genero: {book.genre}')
                print(f'Anio: {book.year}')
                print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")

    def saveBookToCSV(self, book):
        with open(self.filename, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([book.title, book.author, book.genre, book.year])

    def loadBooksFromCSV(self):
        self.books = []
        try:
            with open(self.filename, 'r') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    if len(row) == 4:
                        book = Book(row[0], row[1], row[2], row[3])
                        self.books.append(book)
        except FileNotFoundError:
            pass

class UI:
    def __init__(self) -> None:
        self.myLibrary = Library()

    def menu(self):
        opt = 1
        while opt != 0:
            clear = lambda: os.system('cls')
            clear()
            print('''
            ---------MENU--------------------
            1. agregar libro 
            2. mostrar libro
            3. buscar libros
            4. reservar libro cancelar reserva de libro 
            5. prestar libro
            6. devolver libro 
            7. actualizar información
            0. salir
            -----------------------------------
            ''')
            opt = int(input("Seleccione una opcion: "))

            if opt == 1:
                self.addBook()
            elif opt == 2:
                self.showBooks()
                os.system('pause >NULL')
            
                

    def addBook(self):
        title = input("Ingresa el titulo del libro: ")
        author = input("Ingresa el autor del libro: ")
        genre = input("Ingresa el genero del autor: ")
        year = input("Ingresa el año de publicacion: ")

        book = Book(title, author, genre, year)

        self.myLibrary.addBook(book)
        print('Se agrego correctamente')

    def showBooks(self):
        self.myLibrary.showBooks()

ui = UI()
ui.menu()