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
        self.myLibrary = Library(self.window)
        self.clicked = StringVar()
        # self.add_image = None
        # self.show_image = None
        # self.cancel_image = None
        # self.delete_image = None
        # self.edit_image = None
        # self.exit_image = None
        # self.reserva_image = None
        # self.search_image = None
        
    def set_background_image(self, window, image_path):
        background_image = tk.PhotoImage(file=image_path)
        background_label = tk.Label(window, image=background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)   
        
        
        
    def load_images(self):
        # Carga las imágenes usando PhotoImage
        self.add_image = tk.PhotoImage(file="add.png")
        self.show_image = tk.PhotoImage(file="show.png")
        self.cancel_image = tk.PhotoImage(file="cancel.png")
        self.delete_image = tk.PhotoImage(file="delete.png")
        self.edit_image = tk.PhotoImage(file="edit.png")
        self.exit_image = tk.PhotoImage(file="exit.png")
        self.reserva_image = tk.PhotoImage(file="reserva.png")
        self.search_image = tk.PhotoImage(file="search.png")

    def createStandardWindow(self, title, width, height):
        window = tk.Toplevel(self.window)
        window.title(title)
        window.geometry(f"{width}x{height}")
        return window
        

    def menu(self):
        
        
        menu_frame = tk.Frame(self.window)
        menu_frame.pack()

          


        
        tk.Label(menu_frame, text="Library Management System", font=("Helvetica", 16)).grid(row=0, columnspan=2, pady=10, padx=10)

        tk.Button(menu_frame, text="Add Book", command=self.addBook).grid(row=1, column=0, pady=10)
        tk.Button(menu_frame, text="Show Books", command=self.showBooks).grid(row=1, column=1, pady=10)
        tk.Button(menu_frame, text="Search Books",  command=self.search).grid(row=2, column=0, pady=10)
        tk.Button(menu_frame, text="Reserve Book", command=self.reserveBook).grid(row=2, column=1, pady=10)
        tk.Button(menu_frame, text="Cancel Reservation",  command=self.cancel).grid(row=3, column=0, pady=10)
        tk.Button(menu_frame, text="Edit Book", command=self.editBook).grid(row=3, column=1, pady=10)
        tk.Button(menu_frame, text="Delete Book", command=self.deleteBook).grid(row=4, column=0, pady=10)
        tk.Button(menu_frame, text="Exit", command=self.window.quit).grid(row=4, column=1, pady=10)
        
        menu_frame.mainloop()
        
        


   

        # if opt == 1:
        #     self.addBook()
        # elif opt == 2:
        #     self.showBooks()
        #     os.system('pause >NULL')
        # elif opt == 3:
        #     self.buscar()
        #     os.system('pause >NULL')
        # elif opt == 4:
        #     self.reserveBook()
        #     os.system('pause >NULL')
        # elif opt == 5:
        #     self.cancel()
        #     os.system('pause >NULL')
        # elif opt == 6:
        #     self.editBook()
        #     os.system('pause >NULL')
        # elif opt == 7:
        #     self.deleteBook()
        #     os.system('pause >NULL')




    def addBook(self):
        
        add_book_window = self.createStandardWindow("Add Book", 300, 200)

        

        title_label = tk.Label(add_book_window, text="Title:")
        title_label.pack()
        title_entry = tk.Entry(add_book_window)
        title_entry.pack()

        author_label = tk.Label(add_book_window, text="Author:")
        author_label.pack()
        author_entry = tk.Entry(add_book_window)
        author_entry.pack()

        genre_label = tk.Label(add_book_window, text="Genre:")
        genre_label.pack()
        genre_entry = tk.Entry(add_book_window)
        genre_entry.pack()

        year_label = tk.Label(add_book_window, text="Publication Year:")
        year_label.pack()
        year_entry = tk.Entry(add_book_window)
        year_entry.pack()

        add_button = tk.Button(add_book_window, text="Add Book", command=lambda: self.addBookToLibrary(title_entry.get(), author_entry.get(), genre_entry.get(), year_entry.get(), add_book_window))
        add_button.pack()

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
        show_books_window = self.createStandardWindow("Show Books", 300, 200)

        books_frame = tk.Frame(show_books_window)
        books_frame.pack(fill=tk.BOTH, expand=True)

        canvas = tk.Canvas(books_frame)
        scrollbar = tk.Scrollbar(books_frame, orient="vertical", command=canvas.yview)
        book_list = tk.Frame(canvas)

        scrollbar.pack(side="right", fill="y")
        canvas.create_window((0, 0), window=book_list, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        if not self.myLibrary.books:
            tk.Label(book_list, text="No hay libros en la biblioteca.").pack(pady=10)
        else:
            for book in self.myLibrary.books:
                tk.Label(book_list, text=f"Title: {book.title}").pack()
                tk.Label(book_list, text=f"Author: {book.author}").pack()
                tk.Label(book_list, text=f"Genre: {book.genre}").pack()
                tk.Label(book_list, text=f"Year: {book.year}").pack()
                tk.Label(book_list, text=f"Available: {'Disponible' if book.available else 'Reservado'}").pack()
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
# datatype of menu text 
        
        

        search_window = self.createStandardWindow("Search Books", 300, 200)

        options = ["title", "author", "genre", "year"]
        self.clicked.set("title")  # initial menu text

        drop = OptionMenu(search_window, self.clicked, *options)
        drop.pack()

        criterio_label = tk.Label(search_window, text="Criterio del libro:")
        criterio_label.pack()
        criterio_entry = tk.Entry(search_window)
        criterio_entry.pack()

        buscar_button = tk.Button(search_window, text="Buscar", command=lambda: self.myLibrary.searchUI(self.clicked.get(), criterio_entry.get()))
        buscar_button.pack()

    def reserveBook(self):
        reserve_window = self.createStandardWindow("Reserve Book", 300, 200)

        title_label = tk.Label(reserve_window, text="Título del libro a reservar:")
        title_label.pack()
        title_entry = tk.Entry(reserve_window)
        title_entry.pack()

        reserve_button = tk.Button(reserve_window, text="Reservar", command=lambda: self.myLibrary.reserveBook(title_entry.get()))
        reserve_button.pack()

    def cancel(self):
        cancel_window = self.createStandardWindow("Cancel Reservation", 300, 200)

        title_label = tk.Label(cancel_window, text="Título del libro a cancelar la reserva:")
        title_label.pack()
        title_entry = tk.Entry(cancel_window)
        title_entry.pack()

        cancel_button = tk.Button(cancel_window, text="Cancelar Reserva", command=lambda: self.myLibrary.cancelReservation(title_entry.get()))
        cancel_button.pack()

    def editBook(self):
        edit_window = self.createStandardWindow("Edit Book", 300, 200)

        title_label = tk.Label(edit_window, text="Título del libro a editar:")
        title_label.pack()
        title_entry = tk.Entry(edit_window)
        title_entry.pack()

        attribute_label = tk.Label(edit_window, text="Atributo a editar:")
        attribute_label.pack()
        attribute_entry = tk.Entry(edit_window)
        attribute_entry.pack()

        new_value_label = tk.Label(edit_window, text="Nuevo valor:")
        new_value_label.pack()
        new_value_entry = tk.Entry(edit_window)
        new_value_entry.pack()

        edit_button = tk.Button(edit_window, text="Editar", command=lambda: self.myLibrary.editBook( attribute_entry.get(), new_value_entry.get(),title_entry.get()))
        edit_button.pack()

    def deleteBook(self):
        delete_window = self.createStandardWindow("Delete Book", 300, 200)

        title_label = tk.Label(delete_window, text="Título del libro a eliminar:")
        title_label.pack()
        title_entry = tk.Entry(delete_window)
        title_entry.pack()

        delete_button = tk.Button(delete_window, text="Eliminar", command=lambda: self.myLibrary.deleteBook(title_entry.get()))
        delete_button.pack()


    def clear_frame(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()




class Login:
    def __init__(self, root, library):
        self.root = root
        self.library = library
        self.root.title("Inicio de Sesión")
        self.root.geometry("300x200")

        self.background_image = tk.PhotoImage(file="add.png")  # Reemplaza con la ruta de tu imagen

        # Crear un label con la imagen de fondo
        self.background_label = tk.Label(root, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)  
        
        # Etiqueta de nombre de usuario
        self.username_label = tk.Label(root, text="Usuario:")
        self.username_label.pack()

        # Campo de entrada de nombre de usuario
        self.username_entry = tk.Entry(root)
        self.username_entry.pack()

        # Etiqueta de contraseña
        self.password_label = tk.Label(root, text="Contraseña:")
        self.password_label.pack()

        # Campo de entrada de contraseña
        self.password_entry = tk.Entry(root, show="*")
        self.password_entry.pack()

        # Botón de inicio de sesión
        self.login_button = tk.Button(root, text="Iniciar Sesión", command=self.login)
        self.login_button.pack()

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
