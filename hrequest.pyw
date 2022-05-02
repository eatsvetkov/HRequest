import requests
import csv
from tkinter import filedialog as fd

from tkinter import messagebox
import tkinter as tk
from tkinter import ttk

PAD = 5
IPAD = 5

"""def pth_to_file_fn(pth_to_file):
    try:
        id_list = []

        with open(pth_to_file) as file:
            line = file.readline()
            while line:
                id_list.append(line)
                line = file.readline()
        id_list = [line.rstrip() for line in id_list]
    except Exception:
        print('Error')
        exit()
    ("Возврат")
    return id_list"""
# --------------------------------------------------------------------------- #


def check_connection(idd):
    url = 'https://api.hh.ru/vacancies/' + idd
    r_temp = requests.get(url)
    if r_temp.status_code == 200:
        r = 'ok'
    else:
        r = "problem"
    # checking connection
    return r
# --------------------------------------------------------------------------- #


def id_vac(idd):
    url = 'https://api.hh.ru/vacancies/' + idd
    r = requests.get(url)
    response_dict = r.json()
    try:
        id_vac = response_dict['id']
    except Exception:
        id_vac = ''
    return id_vac
# --------------------------------------------------------------------------- #


def name(idd):
    url = 'https://api.hh.ru/vacancies/' + idd
    r = requests.get(url)
    response_dict = r.json()
    try:
        name = response_dict['name']
    except Exception:
        name = ''
    return name
# --------------------------------------------------------------------------- #


def employer(idd):
    url = 'https://api.hh.ru/vacancies/' + idd
    r = requests.get(url)
    response_dict = r.json()
    try:
        employer = response_dict['employer']['name']
    except Exception:
        employer = ''
    return employer
# --------------------------------------------------------------------------- #


def salary_from_vac(idd):
    url = 'https://api.hh.ru/vacancies/' + idd
    r = requests.get(url)
    response_dict = r.json()
    try:
        salary_from_vac = response_dict['salary']['from']
    except Exception:
        salary_from_vac = ''
    return salary_from_vac
# --------------------------------------------------------------------------- #


def salary_to_vac(idd):
    url = 'https://api.hh.ru/vacancies/' + idd
    r = requests.get(url)
    response_dict = r.json()
    try:
        salary_to_vac = response_dict['salary']['to']
    except Exception:
        salary_to_vac = ''
    return salary_to_vac
# --------------------------------------------------------------------------- #


def schedule_name_vac(idd):
    url = 'https://api.hh.ru/vacancies/' + idd
    r = requests.get(url)
    response_dict = r.json()
    try:
        schedule_name_vac = response_dict['schedule']['name']
    except Exception:
        schedule_name_vac = ''
    return schedule_name_vac
# --------------------------------------------------------------------------- #


def experience(idd):
    url = 'https://api.hh.ru/vacancies/' + idd
    r = requests.get(url)
    response_dict = r.json()
    try:
        experience = response_dict['experience']['name']
    except Exception:
        experience = ''
    return experience
# --------------------------------------------------------------------------- #


def address_city(idd):
    url = 'https://api.hh.ru/vacancies/' + idd
    r = requests.get(url)
    response_dict = r.json()
    try:
        address_city = response_dict['area']['name']
    except Exception:
        address_city = ''
    return address_city
# --------------------------------------------------------------------------- #


def address_metro(idd):
    url = 'https://api.hh.ru/vacancies/' + idd
    r = requests.get(url)
    response_dict = r.json()
    try:
        address_metro = response_dict['address']['metro']['station_name']
    except Exception:
        address_metro = ''
    return address_metro
# --------------------------------------------------------------------------- #


main_line = [
    'connection',
    'id',
    'name',
    'employer',
    'salary from',
    'salary to',
    'schedule',
    'experience',
    'city',
    'metro']
# --------------------------------------------------------------------------- #


def csv_writer(path, fieldnames, data):
    """
    Функция для записи в файл csv
    path - путь до файла
    fieldnames - название столбцов
    data - список из списков
    """
    with open(path, "w", newline='') as out_file:
        '''
        out_file - выходные данные в виде объекта
        delimiter - разделитель :|;
        fieldnames - название полей (столбцов)
        '''
        writer = csv.DictWriter(out_file, delimiter=';', fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)
# --------------------------------------------------------------------------- #


'''
вывод:
столбцы ['lang', 'name', 'level']
ячейки(строки) [['PHP', 'Ivan', '1'],\
['Python', 'Vladimir', '2'],\
['Javascript', 'Egor', '3']]
строки ['PHP', 'Ivan', '1']
строки ['Python', 'Vladimir', '2']
строки ['Javascript', 'Egor', '3']
'''


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('HREQUEST')
        # Создаём элементы
        self.frm_input = ttk.LabelFrame(self, text='Задание пути к файлу')
        self.pth_work_dir = tk.StringVar(value='Пока не задан')
        self.bttn_work_dir = ttk.Button(
            self.frm_input,
            text='Задать',
            command=self.getFolder)
        self.lbl_work_dir = ttk.Entry(
            self.frm_input,
            textvariable=self.pth_work_dir)
        self.bttn_start_dir = ttk.Button(
            self.frm_input,
            text='Начать',
            command=self.start_program)
        # Размещаем элементы
        self.frm_input.pack(
            fill=tk.X,
            expand=True,
            padx=10 * PAD,
            pady=PAD)
        self.bttn_work_dir.pack(
            fill=tk.X,
            expand=True,
            padx=PAD,
            pady=PAD)
        self.lbl_work_dir.pack(
            side=tk.LEFT,
            fill=tk.X,
            expand=True,
            padx=PAD,
            pady=PAD)
        self.bttn_start_dir.pack(
            fill=tk.X,
            expand=True,
            padx=PAD,
            pady=PAD)

    def getFolder(self):
        self.work_dir = fd.askopenfilename(
            title="Укажите файл",
            initialdir='/')
        self.pth_work_dir.set(self.work_dir)

    def paste(self):
        self.pth_work_dir.set(self.clipboard_get())

    def list_creation(self, id_list):
        list_of_line = []
        # print('Start')
        id_list_item = 0
        while id_list_item < len(id_list):
            temp_lst = []
            check_connection_1 = check_connection(idd=id_list[id_list_item])
            temp_lst.append(check_connection_1)

            id_vac_1 = id_vac(idd=id_list[id_list_item])
            temp_lst.append(id_vac_1)

            name_1 = name(idd=id_list[id_list_item])
            temp_lst.append(name_1)

            employer_1 = employer(idd=id_list[id_list_item])
            temp_lst.append(employer_1)

            salary_from_vac_1 = salary_from_vac(idd=id_list[id_list_item])
            temp_lst.append(salary_from_vac_1)

            salary_to_vac_1 = salary_to_vac(idd=id_list[id_list_item])
            temp_lst.append(salary_to_vac_1)

            schedule_name_vac_1 = schedule_name_vac(idd=id_list[id_list_item])
            temp_lst.append(schedule_name_vac_1)

            experience_1 = experience(idd=id_list[id_list_item])
            temp_lst.append(experience_1)

            address_city_1 = address_city(idd=id_list[id_list_item])
            temp_lst.append(address_city_1)

            address_metro_1 = address_metro(idd=id_list[id_list_item])
            temp_lst.append(address_metro_1)

            list_of_line.append(temp_lst)
            # print("id_" + str(id_list_item))
            id_list_item += 1
            label.configure(
                text="Подождите. Обработано " +
                str(id_list_item) + " из " + str(len(id_list)) + ".")
            label.update()
        # print("Success")
        return list_of_line

    def start_program(self):
        self.pth_to_file = self.pth_work_dir.get()
        # pth_to_file_fn(self.pth_to_file)

        print("pth is recieved")
        try:
            id_list = []

            with open(self.pth_to_file) as file:
                line = file.readline()
                while line:
                    id_list.append(line)
                    line = file.readline()
            id_list = [line.rstrip() for line in id_list]
        except Exception:
            print('Error')
            exit()
        prog_list = self.list_creation(id_list)
        list_of_line = prog_list
        my_list = []
        fieldnames = main_line
        data = list_of_line
        cell = data[0:]
        # print('столбцы', fieldnames)
        # print('ячейки(строки)', cell)
        for values in cell:
            # print('строки', values)
            inner_dict = dict(zip(fieldnames, values))
            my_list.append(inner_dict)

        path = "dict_output.csv"
        csv_writer(path, fieldnames, my_list)

        messagebox.showinfo("Инфо", "Успешно")


if __name__ == '__main__':
    app = App()
    label = ttk.Label(app, text="Добро пожаловать!")
    label.pack()
    app.mainloop()
