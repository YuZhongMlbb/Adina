# def text_file(text):

#     lines = 0
#     words = 0
#     symbols = 0

#     with open(text, 'r') as file:
#         for line in file:
#             lines += 1
#             words += len(line.split())
#             symbols += len(line)
    
#     return f"Линии: {lines}\nСлова: {words}\nСимволы: {symbols}"


# all = list()

# def students(name='', age='', grade='', action=0):
#     global all
#     if action == 1:
#         student = dict()
#         student['name'] = name
#         student['age'] = age
#         student['grade'] = grade
#         all.append(student)
#     elif action == 2:
#         num = int(input("Напишите номер ученика: "))
#         if num in range(1, len(all) + 1):
#             all[num - 1]['name'] = name
#             all[num - 1]['age'] = age
#             all[num - 1]['grade'] = grade
#     elif action == 3:
#         num = int(input("Напишите номер ученика: "))
#         if num in range(1, len(all) + 1):
#             all.pop(num - 1)

#     return all

# def calc(action='', num_1=0, num_2=0):
#     if action == '+':
#         return num_1 + num_2
#     elif action == '-':
#         return num_1 - num_2
#     elif action == '*':
#         return num_1 * num_2
#     elif action == '/':
#         return num_1 / num_2

# def parser(file):

#     with open(file, 'r') as f:
#         keys = list()
#         values = list()
#         my = list()
#         counter = 0
#         for line in f:
#             counter += 1
#             if counter == 1:
#                 keys = line.split(',')
#                 continue
#             d = dict()
#             count = 0
#             values = line.split(',')
#             for ik, k in enumerate(keys):
#                 for iy, v in enumerate(values):
#                     if ik == iy:
#                         d[f"{k}"] = v
#                 count += 1
#                 if count == 1:
#                     continue
#                 my.append(d) 
#     return my

# def text(action, file):
#     if action == 'read':
#         with open(file, 'r') as f:
#             a = f.read()
#             return a
#     elif action == 'update':
#         with open(file, 'w') as f:
#             t = input("Введите текст: ")
#             f.write(t)
#             return "Запись обновлена"
#     elif action == "add":
#         with open(file, 'a') as f:
#             t = input("Введите текст: ")
#             f.write(t)
#             return "Запись добавлена"
#     elif action == 'remove':
#         with open(file, 'w') as f:
#             f.write('')
#             return "Запись удалена"

# print(text('remove', 'text.txt'))

# def valid(name, email, age):
#     if len(name) >= 5 and '@' in email and age >= 18:
#         return True
#     return False

# def go(lst):
#     for elem in lst:
#         for k, v in elem.items():
#             with open('new.txt', 'a') as f:
#                 f.write(f"{k} = {v}\n")
#     return "Запись завершена"

# class Bank():

#     def __init__(self) -> None:
#         self.all = list()
#         self.rem = list()
    
#     def add(self, task):
#         self.all.append(task)
#         return "Задача добавлена"
    
#     def remove(self, task):
#         self.all.remove(task)
#         self.rem.append(task)
#         return "Задача удалена"
    
#     def scr_all(self):
#         return self.all
    
#     def scr_rem(self):
#         return self.rem

# def data(data, my_action, action):

#     if action == 'add':
#         with open('action.txt', 'a') as f:
#             f.write(f"Число: {data}, Событие: {my_action}\n")
#         return "Добавлено"
#     elif action == 'remove':
#         with open('action.txt', 'r') as f:
#             lines = f.readlines()
#             with open('finish.txt', 'w') as a:
#                 for line in lines:
#                     if line.find(data) == -1 and line.find(my_action) == -1:
#                         a.write(line)
#         return "Удалено"
#     elif action == "watch":
#         with open("finish.txt", 'r') as f:
#             a = f.read()
#         return a

# import requests
# from bs4 import BeautifulSoup

# class Enter():

#     def __init__(self) -> None:
#         self.url = 'https://enter.kg/monitory_bishkek'
#         self.file = "annur.txt"

#     def parse(self):
#         r = requests.get(url = self.url)
#         soup = BeautifulSoup(r.content,'html.parser')
#         items = soup.find_all('div',class_ ='product vm-col vm-col-1')
#         new_list = []
#         for i in items:
#             try:
#                 new_list.append({
#                     'title': i.find('span',class_ ='prouct_name').get_text(strip = True),
#                     'price': i.find('span',class_ ='price').get_text(strip=True),
#                     'articul': i.find('span', class_="sku").get_text(strip=True)
#             })
#             except Exception as error:
#                 print(f"{error}")
#         return new_list
    

#     def save(self,items):
#         with open(self.file, 'w') as f:
#             for elem in items:
#                 f.write(f"Название: {elem['title']}, Цена: {elem['price']}, Артикул: {elem['articul']}\n")
#         return "Сделано"

# def words(text):
#     text = text.lower()
#     word = text.split(' ')
#     sets = set()
#     for w in word:
#         sets.add(f"{w} = {word.count(w)}")
#     return sets

# def find_even_index(arr):
#     left = 0
#     right = 0
#     for ind, num in arr:
#         if ind == 0:
#             right += sum(arr[1:])
#             if left == right:
#                 return 


# print((find_even_index([1,2,3,4,3,2,1]))) #3