from tkinter import *
from tkinter import messagebox

db_file = 'db.txt'

class App(Frame):
    def __init__(self, master):
        super(App, self).__init__(master)
        self.current_string_num = 0

        self.surname = StringVar()
        self.name = StringVar()
        self.lastname = StringVar()
        self.birthdate = StringVar()
        self.numbers = StringVar()

        data_frame = Frame(window)
        data_frame.grid(column=0, row=0)

        lbl_surname = Label(data_frame, text="Фамилия", padx=10, pady=5)
        lbl_surname.grid(column=0, row=0, sticky="W")
        self.txt_surname = Entry(data_frame, width=30)
        self.txt_surname.grid(column=1, row=0, sticky="W")

        lbl_name = Label(data_frame, text="Имя", padx=10, pady=5)
        lbl_name.grid(column=0, row=1, sticky="W")
        self.txt_name = Entry(data_frame, width=30)
        self.txt_name.grid(column=1, row=1, sticky="W")

        lbl_lastname = Label(data_frame, text="Отчество", padx=10, pady=5)
        lbl_lastname.grid(column=0, row=2, sticky="W")
        self.txt_lastname = Entry(data_frame, width=30)
        self.txt_lastname.grid(column=1, row=2, sticky="W")

        lbl_birthdate = Label(data_frame, text="Дата рождения", padx=10, pady=5)
        lbl_birthdate.grid(column=0, row=3, sticky="W")
        self.txt_birthdate = Entry(data_frame, width=30)
        self.txt_birthdate.grid(column=1, row=3, sticky="W")

        lbl_numbers = Label(data_frame, text="Телефон(ы)", padx=10, pady=5)
        lbl_numbers.grid(column=0, row=4, sticky="W")
        self.txt_numbers = Entry(data_frame, width=50)
        self.txt_numbers.grid(column=1, row=4, sticky="W")

        nav_frame = Frame(window, borderwidth=5)
        nav_frame.grid(column=0, row=1)

        btn_prev = Button(nav_frame, text="Предыдущий", command=self.prev_item)
        btn_prev.pack(side=LEFT, padx=10)

        btn_next = Button(nav_frame, text="Следующий", command=self.next_item)
        btn_next.pack(padx=10)

        self.read_file(db_file, self.current_string_num)

    def read_file(self, filename, str_number):
        file = open(filename, 'r', encoding='utf8')
        strings = file.readlines()
        file_len = len(strings)
        for i in range(file_len):
            if i == str_number:
                string = strings[i]
                surname = string[0:30]
                name = string[30:50]
                lastname = string[50:70]
                birthdate_Y = string[70:74]
                birthdate_M = string[74:76]
                birthdate_D = string[76:78]
                birthdate = [birthdate_D, birthdate_M, birthdate_Y]
                birthdate = '/'.join(birthdate)
                numbers = string[78:128]
                self.update_entry(surname.strip(), name.strip(), lastname.strip(), birthdate.strip(), numbers.strip())
                break
            file.close()
        if str_number > file_len - 1:
            self.current_string_num = file_len - 1
            messagebox.showinfo("Сообщение", "Конец файла достигнут")

    def clearing(self):
        self.txt_surname.delete(0, END)
        self.txt_name.delete(0, END)
        self.txt_lastname.delete(0, END)
        self.txt_birthdate.delete(0, END)
        self.txt_numbers.delete(0, END)

    def update_entry(self, surname, name, lastname, birthdate, numbers):
        self.clearing()
        self.txt_surname.insert(0, surname)
        self.txt_name.insert(0, name)
        self.txt_lastname.insert(0, lastname)
        self.txt_birthdate.insert(0, birthdate)
        self.txt_numbers.insert(0, numbers)

    def next_item(self):
        self.current_string_num += 1
        self.read_file(db_file, self.current_string_num)

    def prev_item(self):
        self.current_string_num -= 1
        if self.current_string_num >= 0:
            self.read_file(db_file, self.current_string_num)
        else:
            self.current_string_num = 0
            messagebox.showinfo("Сообщение", "Начало файла достигнуто")


window = Tk()
window.title("Технологии обработки информации. ЛР 1")
window.geometry('430x185')
app = App(window)

window.mainloop()
