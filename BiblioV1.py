# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 09:32:45 2023

@author: Samuel Israel Medina Rodriguez
        Emanuel de Jesus Vazquez Rosales
"""

#Biblioteca V1
import csv
import os

class Book:
    def __init__(self, title, author, genre, year,available = True) -> None:
        self.title = title
        self.author = author
        self.genre = genre
        self.year = year
        self.available = available


class Library:
    def __init__(self, filename='library.csv') -> None:
        self.books = []
        self.filename = filename
        self.loadBooksFromCSV()

    def addBook(self, book):
        self.books.append(book)
        self.saveBookToCSV(book)

    def addBooks(self):
        with open("library.csv", mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Título", "Autor", "Género", "Año de publicación", "Disponible"])
            for book in self.books:
                print(book)
                writer.writerow([book.title, book.author, book.genre, book.year, book.available])

    def showBooks(self):
        if not self.books:
            print('No hay books')
        else:
            for book in self.books:
                print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
                print(f'Titulo: {book.title}')
                print(f'Autor: {book.author}')
                print(f'Genero: {book.genre}')
                print(f'Anio: {book.year}')
                print(f'Disponible: {book.available}')
                print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")

    def saveBookToCSV(self, book):
        with open(self.filename, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([book.title, book.author, book.genre, book.year, book.available])

    """def loadBooksFromCSV(self):
        self.books = []
        try:
            with open(self.filename, 'r') as csvfile:
                reader = csv.reader(csvfile)
                #next(reader)
                for row in reader:
                    if len(row) == 4:
                        book = Book(row[0], row[1], row[2], row[3])
                        self.books.append(book)
        except FileNotFoundError:
            pass"""
    
    def loadBooksFromCSV(self):
        try:
            with open("library.csv", mode="r") as file:
                reader = csv.reader(file)
                next(reader)  # Saltar la primera fila (encabezados)
                for row in reader:
                    title, author, genre, year, available = row
                    book = Book(title, author, genre, year, available)
                    book.available = True if available.lower() == "sí" else False
                    self.books.append(book)
        except FileNotFoundError:
            print("No se encontró el archivo de registros.")
#                    autor     messi  
    def search(self, atributo, criterio):
        booksFinded = []
        print(self.books)
        for book in self.books:
            if criterio.lower() == getattr(book,atributo).lower():
                booksFinded.append(book)

        if not booksFinded:
            print("No books finded. Please try again")
      
        else:
            print("Books Finded")
            for book in booksFinded:
                estado = "Disponible" if book.available else "Reservado"
                print(f"Titulo: {book.title}")
                print(f"Autor: {book.author}")
                print(f"Genero: {book.genre}")
                print(f"Anio: {book.year}")
                print(f"Displonible: {book.available}")
                print("---------------------------")
        return booksFinded
        
        

    def reserveBook(self, title):

        foundBook = self.search("title",title)[0]
        if foundBook:
            if foundBook.available == True or foundBook.available == "True":
                print(f"¡Reserva exitosa! El book '{foundBook.title}' ha sido reservado.")
                foundBook.available = False
                self.addBooks()
            else:
                print(f"El book '{foundBook.title}' ya está reservado.")
        else:
             print("No se encontró el book especificado.")
             
    def cancelReservation(self,title):
        foundBook = self.search("title",title)[0]

        if foundBook:
            if foundBook.available == False or foundBook.available == "False":
                print(f"¡Cancelacion exitosa! El book '{foundBook.title}' ha sido cancelada la reserva.")
                foundBook.available = True
                self.addBooks()
            else:
                print(f"El book '{foundBook.title}' no cuenta con reservacion.")
        else:
             print("No se encontró el book especificado.")

    

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
            1. agregar book 
            2. mostrar book
            3. buscar books
            4. reservar book 
            5. cancelar reserva de book 
            6. prestar book
            7. devolver book 
            8. actualizar información
            0. salir
            -----------------------------------
            ''')
            opt = int(input("Seleccione una opcion: "))

            if opt == 1:
                self.addBook()
            elif opt == 2:
                self.showBooks()
                os.system('pause >NULL')
            elif opt == 3:
                self.buscar()
                os.system('pause >NULL')
            elif opt == 4:
                self.reserveBook()
                os.system('pause >NULL')
            elif opt == 5:
                self.cancel()
                os.system('pause >NULL')




    def addBook(self):
        title = input("Ingresa el titulo del book: ")
        author = input("Ingresa el autor del book: ")
        genre = input("Ingresa el genero del autor: ")
        year = input("Ingresa el año de publicacion: ")

        book = Book(title, author, genre, year)

        self.myLibrary.addBook(book)
        print('Se agrego correctamente')

    def showBooks(self):
        self.myLibrary.showBooks()

    def buscar(self):
        atributo = input("Ingresa el atributo a buscar: ")
        criterio = input("Ingresa el criterio del book: " )
        
        self.myLibrary.search(atributo, criterio)

    def reserveBook(self):
        title = input("Ingrese el titulo del libro que desea reservar: ")
        self.myLibrary.reserveBook(title)

    def cancel(self):
        title = input("Ingrese el titulo del libro que desea cancelar la reservacion: ")
        self.myLibrary.cancelReservation(title)



ui = UI()
ui.menu()
