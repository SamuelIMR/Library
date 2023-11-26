#BIBLIOTECA 12/11/23
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 09:32:45 2023

@author: Samuel Israel Medina Rodriguez
        Emanuel de Jesus Vazquez Rosales
"""

#Biblioteca V1
import csv
import os
import re
import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage
from tkinter import OptionMenu


# Import module 
from tkinter import *

class Book:
    def __init__(self, title, author, genre, year,available = True) -> None:
        self.title = title
        self.author = author
        self.genre = genre
        self.year = year
        self.available = available


class Library:
    def __init__(self,window, filename='library.csv') -> None:
        self.books = []
        self.filename = filename
        self.loadBooksFromCSV()
        self.window = window
        

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
            messagebox.showinfo('Error','No hay books')
        else:
            results_window = tk.Toplevel(self.window)
            results_window.title("Books Found")
            for book in self.books:
                

                tk.Label(results_window, text="Books Found").pack()
                estado = "Disponible" if book.available else "Reservado"
                result_text = f"Title: {book.title}\nAuthor: {book.author}\nGenre: {book.genre}\nYear: {book.year}\nAvailable: {estado}\n---------------------------"
                tk.Label(results_window, text=result_text).pack()

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
                    #book.available = True if available.lower() == "sí" else False
                    self.books.append(book)
        except FileNotFoundError:
             messagebox.showinfo("No se encontró el a'Error',rchivo de registros.")
#                    autor     messi  
    def searchUI(self, atributo, criterio):
        booksFound = []
        
        for book in self.books:
            if criterio.lower() in getattr(book, atributo).lower():
                booksFound.append(book)

        if not booksFound:
            messagebox.showinfo("No books found", "No books found. Please try again")
        else:
            results_window = tk.Toplevel(self.window)
            results_window.title("Books Found")
            results_window.geometry("300x200")  # Modifica el tamaño de la ventana

            tk.Label(results_window, text="Books Found").pack()

            for book in booksFound:
                estado = "Disponible" if book.available else "Reservado"

                result_text = f"Title: {book.title}\nAuthor: {book.author}\nGenre: {book.genre}\nYear: {book.year}\nAvailable: {estado}\n---------------------------"
                tk.Label(results_window, text=result_text).pack()

        return booksFound
    
    
    def search(self, atributo, criterio):
        booksFound = []
        
        #for book in self.books:
        #    if criterio.lower() == getattr(book, atributo).lower():
        #        booksFound.append(book)
        for book in self.books:
            if criterio.lower() in getattr(book, atributo).lower():
               booksFound.append(book)


        if not booksFound:
            return None
 
        return booksFound
       

    
        
        

    def reserveBook(self, title):

        foundBook = self.search("title",title)[0]
        if foundBook:
            if foundBook.available == True or foundBook.available == "True":
                messagebox.showinfo("Success",f"¡Resebox exitosa! 'Success',El book '{foundBook.title}' ha sido reservado.")
                foundBook.available = False
                self.addBooks()
            else:
                messagebox.showinfo("Error",f"El book '{foundBook.title}' ya está reservado.")
        else:
            messagebox.showinfo("No se encontró el book especificado.")
             
    def cancelReservation(self,title):
        foundBook = self.search("title",title)[0]

        if foundBook:
            if foundBook.available == False or foundBook.available == "False":
                messagebox.showinfo("Success",f"¡Cancelacion exitosa! El book '{foundBook.title}' ha sido cancelada la reserva.")
                foundBook.available = True
                self.addBooks()
            else:
                messagebox.showinfo("Error",f"El book '{foundBook.title}' no cuenta con reservacion.")
        else:
             messagebox.showinfo("Error","No se encontró el book especificado.")

    def editBook(self, atributo, criterio, titulo):
        booksToEdit = self.search("title",titulo)

        if booksToEdit:
            setattr(booksToEdit[0], atributo, criterio)
            messagebox.showinfo("Success",f"Libro modificado con exito")
        else:
            messagebox.showinfo("Error","El libro no existe")
        self.addBooks()

        
    def deleteBook(self, title):
        for book in self.books:
            if book.title.lower() ==title.lower():
                self.books.remove(book)
                self.addBooks()
                messagebox.showinfo("Success",f"Libro '{book.title}' eliminado con éxito.")
                self.addBooks()
                return
        messagebox.showinfo("Error","El libro no fue encontrado en la biblioteca.")
        
    

class UI:
    def __init__(self) -> None:
        
        self.window = tk.Tk()
        self.window.title("Library Management System")
        self.window.geometry("800x400")
        self.window.configure(bg="#2d3e50")
        self.myLibrary = Library(self.window)
        self.clicked = tk.StringVar()
        self.font_size = 16


    def set_font_size(self, widget):
        widget.configure(font=("Arial", self.font_size))
        
        
        


    def createStandardWindow(self, title, width, height):
        window = tk.Toplevel(self.window)
        window.title(title)
        window.geometry(f"{width}x{height}")


        return window
        

    def menu(self):
        
        
        menu_frame = tk.Frame(self.window)
        menu_frame = tk.Frame(self.window, bg="#2d3e50")
        menu_frame.pack()

        
        
        tk.Label(menu_frame, text="Library Management System", font=("Arial", 25),bg="#2d3e50",fg="white").grid(row=0, columnspan=2, pady=10, padx=10)

    

        tk.Button(menu_frame, text="Add Book",bg="#1bbb9c", command=self.addBook, font=("Arial", 16)).grid(row=1, column=0, pady=10)
        tk.Button(menu_frame, text="Show Books",bg="#1bbb9c", command=self.showBooks, font=("Arial", 16)).grid(row=1, column=1, pady=10)
        tk.Button(menu_frame, text="Search Books",bg="#1bbb9c",  command=self.search, font=("Arial", 16)).grid(row=2, column=0, pady=10)
        tk.Button(menu_frame, text="Reserve Book",bg="#1bbb9c", command=self.reserveBook, font=("Arial", 16)).grid(row=2, column=1, pady=10)
        tk.Button(menu_frame, text="Cancel Reservation",bg="#1bbb9c",  command=self.cancel, font=("Arial", 16)).grid(row=3, column=0, pady=10)
        tk.Button(menu_frame, text="Edit Book",bg="#1bbb9c", command=self.editBook, font=("Arial", 16)).grid(row=3, column=1, pady=10)
        tk.Button(menu_frame, text="Delete Book",bg="#1bbb9c", command=self.deleteBook, font=("Arial", 16)).grid(row=4, column=0, pady=10)
        tk.Button(menu_frame, text="Exit",bg="#1bbb9c", command=self.window.quit, font=("Arial", 16)).grid(row=4, column=1, pady=10)
        
        menu_frame.mainloop()
        



    def addBook(self):
        
        add_book_window = self.createStandardWindow("Add Book", 400, 300)
        add_book_window.configure(bg="#2d3e50")
        

        title_label = tk.Label(add_book_window, text="Title:",bg="#2d3e50",fg="white")
        self.set_font_size(title_label)
        title_label.pack()
        title_entry = tk.Entry(add_book_window)
        title_entry.pack(pady=5)

        author_label = tk.Label(add_book_window, text="Author:",bg="#2d3e50",fg="white")
        self.set_font_size(author_label)
        author_label.pack()
        author_entry = tk.Entry(add_book_window)
        author_entry.pack(pady=5)

        genre_label = tk.Label(add_book_window, text="Genre:",bg="#2d3e50",fg="white")
        self.set_font_size(genre_label)
        genre_label.pack()
        genre_entry = tk.Entry(add_book_window)
        genre_entry.pack(pady=5)

        year_label = tk.Label(add_book_window, text="Publication Year:",bg="#2d3e50",fg="white")
        self.set_font_size(year_label)
        year_label.pack()
        year_entry = tk.Entry(add_book_window)
        year_entry.pack(pady=5)

        add_button = tk.Button(add_book_window, text="Add Book", font=("Arial", 12),bg="#1bbb9c", command=lambda: self.addBookToLibrary(title_entry.get(), author_entry.get(), genre_entry.get(), year_entry.get(), add_book_window))
        add_button.pack(pady=10)

    def addBookToLibrary(self, title, author, genre, year, add_book_window):
        book = Book(title, author, genre, year)
        title_books = []
        for check_book in self.myLibrary.books:
            title_books.append(check_book.title)
        if title in title_books:
            messagebox.showinfo("Error", "Book duplicated!")
        else:
            self.myLibrary.addBook(book)
            messagebox.showinfo("Success", "Book added successfully!")
        add_book_window.destroy()

    def showBooks(self):
        show_books_window = self.createStandardWindow("Show Books", 400, 300)
        show_books_window.configure(bg="#2d3e50")

        books_frame = tk.Frame(show_books_window,bg="#2d3e50")
        books_frame.pack(fill=tk.BOTH, expand=True)

        canvas = tk.Canvas(books_frame)
        scrollbar = tk.Scrollbar(books_frame, orient="vertical", command=canvas.yview)
        book_list = tk.Frame(canvas)

        scrollbar.pack(side="right", fill="y")
        canvas.create_window((0, 0), window=book_list, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        if not self.myLibrary.books:
            tk.Label(book_list, text="No hay libros en la biblioteca.",bg="#2d3e50", font=("Arial",12)).pack(pady=10)
        else:
            for book in self.myLibrary.books:
                tk.Label(book_list, text=f"Title: {book.title}", font=("Arial",12)).pack()
                tk.Label(book_list, text=f"Author: {book.author}", font=("Arial",12)).pack()
                tk.Label(book_list, text=f"Genre: {book.genre}", font=("Arial",12)).pack()
                tk.Label(book_list, text=f"Year: {book.year}", font=("Arial",12)).pack()
                tk.Label(book_list, text=f"Available: {'Disponible' if book.available else 'Reservado'}", font=("Arial",12)).pack()
                tk.Label(book_list, text="---------------------------").pack()

        def on_mousewheel(event):
            canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

        def configure_scroll_region(event):
            canvas.configure(scrollregion=canvas.bbox("all"))

        def center_content(event):
            canvas.update_idletasks()
            canvas_width = canvas.winfo_width()
            content_width = book_list.winfo_reqwidth()
            if canvas_width > content_width:
                canvas.itemconfigure(book_list, width=canvas_width)

        book_list.bind("<Configure>", configure_scroll_region)
        canvas.bind("<Configure>", configure_scroll_region)
        canvas.bind("<Configure>", center_content)
        canvas.bind_all("<MouseWheel>", on_mousewheel)

        canvas.pack(side="left", fill="both", expand=True)

        def configure_scroll_region(event):
            canvas.configure(scrollregion=canvas.bbox("all"))

        def center_content(event):
            canvas.update_idletasks()
            canvas_width = canvas.winfo_width()
            content_width = book_list.winfo_reqwidth()
            if canvas_width > content_width:
                canvas.itemconfigure(book_list, width=canvas_width)
        
        book_list.bind("<Configure>", configure_scroll_region)
        canvas.bind("<Configure>", configure_scroll_region)
        canvas.bind("<Configure>", center_content)

        canvas.pack(side="left", fill="both", expand=True)

        def configure_scroll_region(event):
            canvas.configure(scrollregion=canvas.bbox("all"))

        book_list.bind("<Configure>", configure_scroll_region)
        canvas.bind("<Configure>", configure_scroll_region)

        canvas.pack(side="left", fill="both", expand=True)

    def search(self):
        
        search_window = self.createStandardWindow("Search Books", 400, 300)
        search_window.configure(bg="#2d3e50")

        options = ["title", "author", "genre", "year"]
        self.clicked.set("title")  # initial menu text

        drop = OptionMenu(search_window, self.clicked, *options)
        drop.pack(pady=5)

        criterio_label = tk.Label(search_window, text="Criterio del libro:",bg="#2d3e50",fg="white")
        self.set_font_size(criterio_label)
        criterio_label.pack()
        criterio_entry = tk.Entry(search_window)
        criterio_entry.pack(pady=5)

        buscar_button = tk.Button(search_window, text="Buscar",bg="#1bbb9c", font=("Arial", 12), command=lambda: self.myLibrary.searchUI(self.clicked.get(), criterio_entry.get()))

        buscar_button.pack(pady=10)

    def reserveBook(self):
        reserve_window = self.createStandardWindow("Reserve Book", 400, 300)
        reserve_window.configure(bg="#2d3e50")

        title_label = tk.Label(reserve_window, text="Título del libro a reservar:",bg="#2d3e50",fg="white")
        self.set_font_size(title_label)
        title_label.pack()
        title_entry = tk.Entry(reserve_window)
        title_entry.pack(pady=5)

        reserve_button = tk.Button(reserve_window, text="Reservar",bg="#1bbb9c",font=("Arial", 12), command=lambda: self.myLibrary.reserveBook(title_entry.get()))
        #self.set_font_size(reserve_button)
        reserve_button.pack(pady=10)

    def cancel(self):
        cancel_window = self.createStandardWindow("Cancel Reservation", 400, 300)
        cancel_window.configure(bg="#2d3e50")

        title_label = tk.Label(cancel_window, text="Título del libro a cancelar la reserva:",bg="#2d3e50",fg="white")
        self.set_font_size(title_label)
        title_label.pack()
        title_entry = tk.Entry(cancel_window)
        title_entry.pack(pady=5)

        cancel_button = tk.Button(cancel_window, text="Cancelar Reserva",bg="#1bbb9c", font=("Arial", 12), command=lambda: self.myLibrary.cancelReservation(title_entry.get()))
        #self.set_font_size(cancel_button)
        cancel_button.pack(pady=10)

    def editBook(self):
        edit_window = self.createStandardWindow("Edit Book", 400, 300)
        edit_window.configure(bg="#2d3e50")

        title_label = tk.Label(edit_window, text="Título del libro a editar:",bg="#2d3e50",fg="white")
        self.set_font_size(title_label)
        title_label.pack()
        title_entry = tk.Entry(edit_window)
        title_entry.pack(pady=5)

        attribute_label = tk.Label(edit_window, text="Atributo a editar:",bg="#2d3e50",fg="white")
        self.set_font_size(attribute_label)
        attribute_label.pack()
        attribute_entry = tk.Entry(edit_window)
        attribute_entry.pack(pady=5)

        new_value_label = tk.Label(edit_window, text="Nuevo valor:",bg="#2d3e50",fg="white")
        self.set_font_size(new_value_label)
        new_value_label.pack()
        new_value_entry = tk.Entry(edit_window)
        new_value_entry.pack(pady=5)

        edit_button = tk.Button(edit_window, text="Editar",bg="#1bbb9c", font=("Arial", 12), command=lambda: self.myLibrary.editBook( attribute_entry.get(), new_value_entry.get(),title_entry.get()))
        #self.set_font_size(edit_button)
        edit_button.pack(pady=10)

    def deleteBook(self):
        delete_window = self.createStandardWindow("Delete Book", 400, 300)
        delete_window.configure(bg="#2d3e50")

        title_label = tk.Label(delete_window, text="Título del libro a eliminar:",bg="#2d3e50",fg="white")
        self.set_font_size(title_label)
        title_label.pack()
        title_entry = tk.Entry(delete_window)
        title_entry.pack(pady=5)

        delete_button = tk.Button(delete_window, text="Eliminar",bg="#1bbb9c", font=("Arial", 12), command=lambda: self.myLibrary.deleteBook(title_entry.get()))
        #self.set_font_size(delete_button)
        delete_button.pack(pady=10)


    def clear_frame(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()




class Login:
    def __init__(self, root, library):
        self.root = root
        self.library = library
        self.root.title("Inicio de Sesión")
        self.root.geometry("300x200")
        self.root.configure(bg="#2d3e50")

        # self.background_image = tk.PhotoImage(file="login.png") 

        # # Crear un label con la imagen de fondo
        # self.background_label = tk.Label(root, image=self.background_image)
        # self.background_label.place(x=0, y=0, relwidth=1, relheight=1)  
        
        # Etiqueta de nombre de usuario
        self.username_label = tk.Label(root, text="Usuario:", font=("Arial",12),bg="#2d3e50",fg="white")
        self.username_label.pack()

        # Campo de entrada de nombre de usuario
        self.username_entry = tk.Entry(root)
        self.username_entry.pack()

        # Etiqueta de contraseña
        self.password_label = tk.Label(root, text="Contraseña:", font=("Arial",12),bg="#2d3e50",fg="white")
        self.password_label.pack()

        # Campo de entrada de contraseña
        self.password_entry = tk.Entry(root, show="*")
        self.password_entry.pack()

        # Botón de inicio de sesión
        self.login_button = tk.Button(root, text="Iniciar Sesión", font=("Arial",12),bg="#1bbb9c", command=self.login)
        self.login_button.pack(pady=15)

    def login(self):
        # Verificar si el nombre de usuario y la contraseña son correctos
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == "admin" and password == "admin":
            # Iniciar sesión exitosa
            self.root.destroy()  # Cerrar la ventana de inicio de sesión
            self.library.menu()  # Mostrar el menú principal de la biblioteca
        else:
            messagebox.showerror("Error", "Nombre de usuario o contraseña incorrectos")







root = tk.Tk()
ui = UI()
#library = Library(root)
login = Login(root, ui)
root.mainloop()
