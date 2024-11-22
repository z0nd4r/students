import sqlite3
import tkinter
import tkinter.messagebox


class Students:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.__build_main_window()
        tkinter.mainloop()

        conn = sqlite3.connect(r'C:\Users\Kirito\Desktop\Programmki\Students_info\student_info.db')
        cur = conn.cursor()
        try:
            cur.execute('PRAGMA foreign_keys=ON')
            cur.execute('CREATE TABLE Majors (MajorID INTEGER PRIMARY KEY NOT NULL, Name TEXT)')
            cur.execute('CREATE TABLE Departments (DeptID INTEGER PRIMARY KEY NOT NULL, Name TEXT)')
            cur.execute('''CREATE TABLE Students (StudentID INTEGER PRIMARY KEY NOT NULL, Name TEXT, MajorID INTEGER, DeptID INTEGER,
                                                FOREIGN KEY (MajorID) REFERENCES Majors(MajorID),
                                                FOREIGN KEY (DeptID) REFERENCES Departments(DeptID))''')
            print('Таблица создана!')
        except sqlite3.OperationalError:
            print('Ошибка, такая таблица уже существует!')

    def __build_main_window(self):  # главное окно
        self.main_window.title('Студенты')
        self.__build_frame()
        self.__build_listbox()
        self.__populate_listbox()
        self.__build_scrollbar()
        self.__build_buttons()

    def __build_frame(self):  # фреймы к главному окну
        self.frame_1 = tkinter.Frame(self.main_window)
        self.frame_2 = tkinter.Frame(self.main_window)
        self.frame_3 = tkinter.Frame(self.main_window)
        self.frame_4 = tkinter.Frame(self.main_window)
        self.frame_1.pack()
        self.frame_2.pack()
        self.frame_3.pack()
        self.frame_4.pack()

    def __build_listbox(self):  # листбокс к главному окну
        self.listbox_students = tkinter.Listbox(self.frame_1, selectmode=tkinter.SINGLE, exportselection=False)
        self.listbox_students.pack(side='left', ipadx=40)

    def __populate_listbox(self):  # заполнить листбокс в главном окне
        self.listbox_students.delete(0, tkinter.END)
        for students in self.__get_students():
            self.listbox_students.insert(tkinter.END, students[0])

    def __build_scrollbar(self):  # скроллбар к листбоксу главного окна
        self.scrollbar = tkinter.Scrollbar(self.frame_1)
        self.scrollbar.config(command=self.listbox_students.yview)
        self.listbox_students.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side='left', fill=tkinter.Y)

    def __build_buttons(self):  # кнопки главного окна
        self.button_1 = tkinter.Button(self.frame_2, text='Инфо', command=self.__show_info_of_student)
        self.button_2 = tkinter.Button(self.frame_2, text='Добавить', command=self.__add)
        self.button_3 = tkinter.Button(self.frame_2, text='Изменить', command=self.__change_student_1)
        self.button_4 = tkinter.Button(self.frame_2, text='Удалить', command=self.__delete_student)
        self.button_5 = tkinter.Button(self.frame_3, text='Специальности', command=self.__show_majors)
        self.button_6 = tkinter.Button(self.frame_3, text='Факультеты', command=self.__show_dept)
        self.button_7 = tkinter.Button(self.frame_4, text='Обновить', command=self.__populate_listbox)
        self.button_8 = tkinter.Button(self.frame_4, text='Выйти', command=self.main_window.destroy)
        self.button_1.pack(side='left')
        self.button_2.pack(side='left')
        self.button_3.pack(side='left')
        self.button_4.pack(side='left')
        self.button_5.pack(side='left')
        self.button_6.pack(side='left')
        self.button_7.pack(side='left')
        self.button_8.pack(side='left')

    def __get_students(self):  # заполнить листбокс главного окна со студентами
        conn = None
        try:
            conn = sqlite3.connect(r'C:\Users\Kirito\Desktop\Programmki\Students\student_info.db')
            cur = conn.cursor()

            cur.execute('SELECT Name FROM Students')

            return cur.fetchall()
        except sqlite3.Error as err:
            print('__get_students', err)
        finally:
            if conn is not None:
                conn.close()

    def __get_students_id(self):
        conn = None
        try:
            conn = sqlite3.connect(r'C:\Users\Kirito\Desktop\Programmki\Students\student_info.db')
            cur = conn.cursor()

            cur.execute('SELECT StudentID FROM Students')

            return cur.fetchall()
        except sqlite3.Error as err:
            print('__get_students_id', err)
        finally:
            if conn is not None:
                conn.close()

    def __add(self):  # КНОПКА ДОБАВИТЬ главного окна
        self.main_window_2 = tkinter.Tk()
        self.main_window_2.title('Добавить')

        self.button_1 = tkinter.Button(self.main_window_2, text='Студент', command=self.__add_student)
        self.button_2 = tkinter.Button(self.main_window_2, text='Специальность', command=self.__add_major)
        self.button_3 = tkinter.Button(self.main_window_2, text='Факультет', command=self.__add_dept)
        self.button_4 = tkinter.Button(self.main_window_2, text='Отмена', command=self.main_window_2.destroy)
        self.button_1.pack()
        self.button_2.pack(padx=70)
        self.button_3.pack()
        self.button_4.pack(pady=10)

    def __add_student(self):  # добавить инфо о студенте
        self.main_window_5 = tkinter.Tk()
        self.main_window_5.title('Добавить студента')

        self.frame_1 = tkinter.Frame(self.main_window_5)
        self.frame_2 = tkinter.Frame(self.main_window_5)
        self.frame_3 = tkinter.Frame(self.main_window_5)
        self.frame_4 = tkinter.Frame(self.main_window_5)
        self.frame_1.pack()
        self.frame_2.pack()
        self.frame_3.pack()
        self.frame_4.pack(pady=10)

        self.label_1 = tkinter.Label(self.frame_1, text='Фамилия И.О.     ')
        self.label_2 = tkinter.Label(self.frame_2, text='Факультет                 ')
        self.label_3 = tkinter.Label(self.frame_3, text='Специальность        ')
        self.label_1.pack(side='left')
        self.label_2.pack(side='left')
        self.label_3.pack(side='left')

        self.entry_student = tkinter.Entry(self.frame_1)
        self.entry_student.pack(side='left')
        self.listbox_1 = tkinter.Listbox(self.frame_2, selectmode=tkinter.SINGLE, height=5, exportselection=False)
        self.listbox_2 = tkinter.Listbox(self.frame_3, selectmode=tkinter.SINGLE, height=5, exportselection=False)
        self.listbox_1.pack(side='left')
        self.listbox_2.pack(side='left')

        self.scrollbar = tkinter.Scrollbar(self.frame_2)
        self.scrollbar.config(command=self.listbox_1.yview)
        self.listbox_1.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side='left', fill=tkinter.Y)

        self.scrollbar_1 = tkinter.Scrollbar(self.frame_3)
        self.scrollbar_1.config(command=self.listbox_2.yview)
        self.listbox_2.config(yscrollcommand=self.scrollbar_1.set)
        self.scrollbar_1.pack(side='left', fill=tkinter.Y)

        for dept_item in self.__get_dept():
            self.listbox_1.insert(tkinter.END, dept_item[0])

        for major_item in self.__get_majors():
            self.listbox_2.insert(tkinter.END, major_item[0])

        self.button_1 = tkinter.Button(self.frame_4, text='OK', command=self.__add_student_2)
        self.button_2 = tkinter.Button(self.frame_4, text='Отмена', command=self.main_window_5.destroy)
        self.button_1.pack(side='left')
        self.button_2.pack(side='left')

    def __add_student_2(self):  # продолжение обратной функции __add_student
        self.student = self.entry_student.get()
        self.major = self.listbox_2.curselection()
        self.dept = self.listbox_1.curselection()

        conn = None
        try:
            conn = sqlite3.connect(r'C:\Users\Kirito\Desktop\Programmki\Students\student_info.db')
            cur = conn.cursor()

            print(self.student, self.dept[0], self.major[0])

            cur.execute('INSERT INTO Students (Name, MajorID, DeptID) VALUES (?,?,?)',
                        (self.student, self.major[0] + 1, self.dept[0] + 1,))

            conn.commit()
        except sqlite3.Error as err:
            print('__add_student_2', err)
        finally:
            if conn is not None:
                conn.close()
        self.main_window_5.destroy()
        self.__populate_listbox()

    def __change_student_1(self):  # изменить инфо о студенте
        self.main_window_10 = tkinter.Tk()
        self.main_window_10.title('Изменить информацию о студенте')

        self.frame_1 = tkinter.Frame(self.main_window_10)
        self.frame_2 = tkinter.Frame(self.main_window_10)
        self.frame_3 = tkinter.Frame(self.main_window_10)
        self.frame_4 = tkinter.Frame(self.main_window_10)
        self.frame_1.pack()
        self.frame_2.pack()
        self.frame_3.pack()
        self.frame_4.pack(pady=10)

        self.label_1 = tkinter.Label(self.frame_1, text='Фамилия И.О.     ')
        self.label_2 = tkinter.Label(self.frame_2, text='Факультет                 ')
        self.label_3 = tkinter.Label(self.frame_3, text='Специальность        ')
        self.label_1.pack(side='left')
        self.label_2.pack(side='left')
        self.label_3.pack(side='left')

        self.entry_student = tkinter.Entry(self.frame_1)
        self.entry_student.pack(side='left')
        self.listbox_1 = tkinter.Listbox(self.frame_2, selectmode=tkinter.SINGLE, height=5, exportselection=False)
        self.listbox_2 = tkinter.Listbox(self.frame_3, selectmode=tkinter.SINGLE, height=5, exportselection=False)
        self.listbox_1.pack(side='left')
        self.listbox_2.pack(side='left')

        self.scrollbar = tkinter.Scrollbar(self.frame_2)
        self.scrollbar.config(command=self.listbox_1.yview)
        self.listbox_1.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side='left', fill=tkinter.Y)

        self.scrollbar_1 = tkinter.Scrollbar(self.frame_3)
        self.scrollbar_1.config(command=self.listbox_2.yview)
        self.listbox_2.config(yscrollcommand=self.scrollbar_1.set)
        self.scrollbar_1.pack(side='left', fill=tkinter.Y)

        for dept_item in self.__get_dept():
            self.listbox_1.insert(tkinter.END, dept_item[0])

        for major_item in self.__get_majors():
            self.listbox_2.insert(tkinter.END, major_item[0])

        self.button_1 = tkinter.Button(self.frame_4, text='OK', command=self.__change_student_2)
        self.button_2 = tkinter.Button(self.frame_4, text='Отмена', command=self.main_window_10.destroy)
        self.button_1.pack(side='left')
        self.button_2.pack(side='left')

    def __change_student_2(self):  # продолжение обратной функции __change_student_1
        indexes = self.listbox_students.curselection()
        self.student = self.entry_student.get()
        self.major = self.listbox_2.curselection()
        self.dept = self.listbox_1.curselection()
        if len(indexes) == 0:
            tkinter.messagebox.showinfo(message='Ни один элемент не выбран')
        else:
            for i in indexes:
                z = self.__get_students_id()[i]
                self.change_student = z[0]

        conn = None
        try:
            conn = sqlite3.connect(r'C:\Users\Kirito\Desktop\Programmki\Students\student_info.db')
            cur = conn.cursor()

            cur.execute('UPDATE Students SET Name = ?, MajorID = ?, DeptID = ? WHERE StudentID == ?',
                        (self.student, self.major[0] + 1, self.dept[0] + 1, self.change_student,))

            conn.commit()
        except sqlite3.Error as err:
            print('__change_student_2', err)
        finally:
            if conn is not None:
                conn.close()
        self.main_window_10.destroy()
        self.__populate_listbox()

    def __delete_student(self):
        indexes = self.listbox_students.curselection()
        if len(indexes) == 0:
            tkinter.messagebox.showinfo(message='Ни один элемент не выбран')
        else:
            for i in indexes:
                z = self.__get_students_id()[i]
                self.delete_student = z[0]

        conn = None
        try:
            conn = sqlite3.connect(r'C:\Users\Kirito\Desktop\Programmki\Students\student_info.db')
            cur = conn.cursor()

            cur.execute('DELETE FROM Students WHERE StudentID == ?', (self.delete_student,))

            conn.commit()
        except sqlite3.Error as err:
            print('__delete_student', err)
        finally:
            if conn is not None:
                conn.close()
        self.__populate_listbox()

    def __add_major(self):  # добавить специальность
        self.main_window_6 = tkinter.Tk()
        self.main_window_6.title('Добавить специальность')

        self.frame_1 = tkinter.Frame(self.main_window_6)
        self.frame_2 = tkinter.Frame(self.main_window_6)
        self.frame_1.pack()
        self.frame_2.pack(pady=10)

        self.label_1 = tkinter.Label(self.frame_1, text='Название специальности')
        self.label_1.pack(side='left')
        self.entry_major = tkinter.Entry(self.frame_1)
        self.entry_major.pack(side='left')

        self.button_1 = tkinter.Button(self.frame_2, text='OK', command=self.__add_major_1)
        self.button_2 = tkinter.Button(self.frame_2, text='Отмена', command=self.main_window_6.destroy)
        self.button_1.pack(side='left')
        self.button_2.pack(side='left')

    def __add_major_1(self):  # добавить специальность в БД
        major = self.entry_major.get()

        conn = None
        try:
            conn = sqlite3.connect(r'C:\Users\Kirito\Desktop\Programmki\Students\student_info.db')
            cur = conn.cursor()

            cur.execute('INSERT INTO Majors (Name) VALUES (?)', (major,))

            conn.commit()
        except sqlite3.Error as err:
            print('__add_major_1', err)
        finally:
            if conn is not None:
                conn.close()
        self.main_window_6.destroy()

    def __add_dept(self):  # добавить факультет
        self.main_window_7 = tkinter.Tk()
        self.main_window_7.title('Добавить факультет')

        self.frame_1 = tkinter.Frame(self.main_window_7)
        self.frame_2 = tkinter.Frame(self.main_window_7)
        self.frame_1.pack()
        self.frame_2.pack(pady=10)

        self.label_1 = tkinter.Label(self.frame_1, text='Название факультета')
        self.label_1.pack(side='left')
        self.entry_dept = tkinter.Entry(self.frame_1)
        self.entry_dept.pack(side='left')

        self.button_1 = tkinter.Button(self.frame_2, text='OK', command=self.__add_dept_1)
        self.button_2 = tkinter.Button(self.frame_2, text='Отмена', command=self.main_window_7.destroy)
        self.button_1.pack(side='left')
        self.button_2.pack(side='left')

    def __add_dept_1(self):  # добавить факультет в БД
        dept = self.entry_dept.get()

        conn = None
        try:
            conn = sqlite3.connect(r'C:\Users\Kirito\Desktop\Programmki\Students\student_info.db')
            cur = conn.cursor()

            cur.execute('INSERT INTO Departments (Name) VALUES (?)', (dept,))

            conn.commit()
        except sqlite3.Error as err:
            print('__add_major_1', err)
        finally:
            if conn is not None:
                conn.close()
        self.main_window_7.destroy()

    def __show_info_of_student(self):
        indexes = self.listbox_students.curselection()
        for i in indexes:
            index_one = i
            z = self.__get_students()[index_one]
            self.show_students_1 = z[0]

        conn = None
        try:
            conn = sqlite3.connect(r'C:\Users\Kirito\Desktop\Programmki\Students\student_info.db')
            cur = conn.cursor()
            print(self.show_students_1)
            cur.execute('PRAGMA foreign_keys=ON')
            cur.execute('''SELECT Students.Name, Majors.Name, Departments.Name
                                FROM Students, Majors, Departments
                                WHERE Students.Name == ? AND Students.MajorID == Majors.MajorID AND Students.DeptID == Departments.DeptID''',
                        (self.show_students_1,))
            self.show_students = cur.fetchall()[0]
            print(self.show_students)
        except sqlite3.Error as err:
            print('__show_info_of_student', err)
        finally:
            if conn is not None:
                conn.close()
                msg = f'Фио: {self.show_students[0]} \
                    \nСпециальность: {self.show_students[1]} \
                    \nФакультет: {self.show_students[2]}'
                tkinter.messagebox.showinfo('Информация о студенте', message=msg)

    def __show_majors(self):  # КНОПКА СПЕЦИАЛЬНОСТИ главного окна
        self.main_window_3 = tkinter.Tk()
        self.main_window_3.title('Список специальностей')

        self.frame_1 = tkinter.Frame(self.main_window_3)
        self.frame_2 = tkinter.Frame(self.main_window_3)
        self.frame_3 = tkinter.Frame(self.main_window_3)
        self.frame_1.pack()
        self.frame_2.pack()
        self.frame_3.pack(pady=10)

        self.listbox_majors = tkinter.Listbox(self.frame_1)
        self.listbox_majors.pack(side='left')

        self.scrollbar = tkinter.Scrollbar(self.frame_1)
        self.scrollbar.config(command=self.listbox_majors.yview)
        self.listbox_majors.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side='left', fill=tkinter.Y)

        self.__populate_listbox_majors()

        self.button_1 = tkinter.Button(self.frame_2, text='Изменить', command=self.__change_major_1)
        self.button_2 = tkinter.Button(self.frame_2, text='Удалить', command=self.__delete_major)
        self.button_3 = tkinter.Button(self.frame_3, text='Обновить', command=self.__populate_listbox_majors)
        self.button_4 = tkinter.Button(self.frame_3, text='Выйти', command=self.main_window_3.destroy)
        self.button_1.pack(side='left')
        self.button_2.pack(side='left')
        self.button_3.pack(side='left')
        self.button_4.pack(side='left')

    def __get_majors(self):  # заполнить листбокс СПЕЦИАЛЬНОСТЕЙ
        conn = None
        try:
            conn = sqlite3.connect(r'C:\Users\Kirito\Desktop\Programmki\Students\student_info.db')
            cur = conn.cursor()

            cur.execute('SELECT Name FROM Majors')

            return cur.fetchall()
        except sqlite3.Error as err:
            print('__get_students', err)
        finally:
            if conn is not None:
                conn.close()

    def __show_dept(self):  # КНОПКА ФАКУЛЬТЕТЫ главного окна
        self.main_window_4 = tkinter.Tk()
        self.main_window_4.title('Список факультетов')

        self.frame_1 = tkinter.Frame(self.main_window_4)
        self.frame_2 = tkinter.Frame(self.main_window_4)
        self.frame_3 = tkinter.Frame(self.main_window_4)
        self.frame_1.pack()
        self.frame_2.pack()
        self.frame_3.pack(pady=10)

        self.listbox_dept = tkinter.Listbox(self.frame_1)
        self.listbox_dept.pack(side='left')

        self.scrollbar = tkinter.Scrollbar(self.frame_1)
        self.scrollbar.config(command=self.listbox_dept.yview)
        self.listbox_dept.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side='left', fill=tkinter.Y)

        self.__populate_listbox_dept()

        self.button_1 = tkinter.Button(self.frame_2, text='Изменить', command=self.__change_dept_1)
        self.button_2 = tkinter.Button(self.frame_2, text='Удалить', command=self.__delete_dept)
        self.button_3 = tkinter.Button(self.frame_3, text='Обновить', command=self.__populate_listbox_dept)
        self.button_4 = tkinter.Button(self.frame_3, text='Выйти', command=self.main_window_4.destroy)
        self.button_1.pack(side='left')
        self.button_2.pack(side='left')
        self.button_3.pack(side='left')
        self.button_4.pack(side='left')

    def __get_dept(self):  # заполнить листбокс факультетов
        conn = None
        try:
            conn = sqlite3.connect(r'C:\Users\Kirito\Desktop\Programmki\Students\student_info.db')
            cur = conn.cursor()

            cur.execute('SELECT Name FROM Departments')

            return cur.fetchall()
        except sqlite3.Error as err:
            print('__get_students', err)
        finally:
            if conn is not None:
                conn.close()

    def __populate_listbox_majors(self):  # заполнить листбокс СПЕЦИАЛЬНОСТЕЙ
        self.listbox_majors.delete(0, tkinter.END)
        for majors in self.__get_majors():
            self.listbox_majors.insert(tkinter.END, majors[0])

    def __populate_listbox_dept(self):  # заполнить листбокс факультетов
        self.listbox_dept.delete(0, tkinter.END)
        for dept in self.__get_dept():
            self.listbox_dept.insert(tkinter.END, dept[0])

    def __change_major_1(self):
        self.main_window_8 = tkinter.Tk()
        self.main_window_8.title('Изменить специальность')

        self.frame_1 = tkinter.Frame(self.main_window_8)
        self.frame_2 = tkinter.Frame(self.main_window_8)
        self.frame_1.pack()
        self.frame_2.pack(pady=10)

        self.label_1 = tkinter.Label(self.frame_1, text='Название специальности')
        self.label_1.pack(side='left')
        self.entry_major_change = tkinter.Entry(self.frame_1)
        self.entry_major_change.pack(side='left')

        self.button_1 = tkinter.Button(self.frame_2, text='OK', command=self.__change_major_2)
        self.button_2 = tkinter.Button(self.frame_2, text='Отмена', command=self.main_window_8.destroy)
        self.button_1.pack(side='left')
        self.button_2.pack(side='left')

    def __change_major_2(self):
        self.major = tkinter.StringVar()
        self.major_new = tkinter.StringVar()
        self.major_new.set(self.entry_major_change.get())
        indexes = self.listbox_majors.curselection()
        if len(indexes) == 0:
            tkinter.messagebox.showinfo(message='Ни один элемент не выбран')
        else:
            for i in indexes:
                z = self.__get_majors()[i]
                self.major = z[0]

        conn = None
        try:
            conn = sqlite3.connect(r'C:\Users\Kirito\Desktop\Programmki\Students\student_info.db')
            cur = conn.cursor()

            major = self.major
            major_new = self.major_new.get()

            cur.execute('UPDATE Majors SET Name = ? WHERE Name == ?', (major_new, major))

            conn.commit()
        except sqlite3.Error as err:
            print('__change_major_2', err)
        finally:
            if conn is not None:
                conn.close()
        self.main_window_8.destroy()

    def __change_dept_1(self):
        self.main_window_9 = tkinter.Tk()
        self.main_window_9.title('Изменить факультет')

        self.frame_1 = tkinter.Frame(self.main_window_9)
        self.frame_2 = tkinter.Frame(self.main_window_9)
        self.frame_1.pack()
        self.frame_2.pack(pady=10)

        self.label_1 = tkinter.Label(self.frame_1, text='Название факультета')
        self.label_1.pack(side='left')
        self.entry_dept_change = tkinter.Entry(self.frame_1)
        self.entry_dept_change.pack(side='left')

        self.button_1 = tkinter.Button(self.frame_2, text='OK', command=self.__change_dept_2)
        self.button_2 = tkinter.Button(self.frame_2, text='Отмена', command=self.main_window_9.destroy)
        self.button_1.pack(side='left')
        self.button_2.pack(side='left')

    def __change_dept_2(self):
        self.dept = tkinter.StringVar()
        self.dept_new = tkinter.StringVar()
        self.dept_new.set(self.entry_dept_change.get())
        indexes = self.listbox_dept.curselection()
        if len(indexes) == 0:
            tkinter.messagebox.showinfo(message='Ни один элемент не выбран')
        else:
            for i in indexes:
                z = self.__get_dept()[i]
                self.dept = z[0]

        conn = None
        try:
            conn = sqlite3.connect(r'C:\Users\Kirito\Desktop\Programmki\Students\student_info.db')
            cur = conn.cursor()

            dept = self.dept
            dept_new = self.dept_new.get()

            cur.execute('UPDATE Departments SET Name = ? WHERE Name == ?', (dept_new, dept))

            conn.commit()
        except sqlite3.Error as err:
            print('__change_dept_2', err)
        finally:
            if conn is not None:
                conn.close()
        self.main_window_9.destroy()

    def __delete_major(self):  # удалить специальность
        indexes = self.listbox_majors.curselection()
        self.major = tkinter.StringVar()
        if len(indexes) == 0:
            tkinter.messagebox.showinfo(message='Ни один элемент не выбран')
        else:
            for i in indexes:
                z = self.__get_majors()[i]
                self.major = z[0]

        conn = None
        try:
            conn = sqlite3.connect(r'C:\Users\Kirito\Desktop\Programmki\Students\student_info.db')
            cur = conn.cursor()

            major = self.major

            cur.execute('DELETE FROM Majors WHERE Name == ?', (major,))

            conn.commit()
        except sqlite3.Error as err:
            print('__delete_major', err)
        finally:
            if conn is not None:
                conn.close()

    def __delete_dept(self):  # удалить факультет
        indexes = self.listbox_dept.curselection()
        self.dept = tkinter.StringVar()
        if len(indexes) == 0:
            tkinter.messagebox.showinfo(message='Ни один элемент не выбран')
        else:
            for i in indexes:
                z = self.__get_dept()[i]
                self.dept = z[0]
        conn = None
        try:
            conn = sqlite3.connect(r'C:\Users\Kirito\Desktop\Programmki\Students\student_info.db')
            cur = conn.cursor()

            dept = self.dept

            cur.execute('DELETE FROM Departments WHERE Name == ?', (dept,))

            conn.commit()
        except sqlite3.Error as err:
            print('__delete_dept', err)
        finally:
            if conn is not None:
                conn.close()


if __name__ == '__main__':
    Students = Students()
