import shutil
import os
import keyboard
from prettytable import PrettyTable
import click
lstmoveto=[]
lstmovefrom=[]
lstrash=[]
k=0
k1=0
table=PrettyTable()
table2=PrettyTable()
table.field_names=["Папки", "Место ввода/вывода", "Расширение"]
def moveFiles():
    needToMove = os.listdir(lstmovefrom[k1-1])
    if len(needToMove) == 0:
        return
    for file in needToMove:
        fExt = file[file.rfind('.')+1:]
        print(fExt)
        try:
            shutil.move(lstmovefrom[k1-1] + "\\\\" + file, lstmoveto[k-1] + "\\\\" + fExt + "\\\\" + file, copy_function=shutil.copy2)
        except FileNotFoundError:
            dirPath = os.path.join(lstmoveto[k-1], fExt) 
            os.mkdir(dirPath)
            shutil.move(lstmovefrom[k1-1] + "\\\\" + file, lstmoveto[k-1] + "\\\\" + fExt + "\\\\" + file, copy_function=shutil.copy2)
def movefilestrue():
    docs=(r"C:\Users\Andrey\Documents")
    pic=(r"C:\Users\Andrey\Pictures")
    vid=(r"C:\Users\Andrey\Videos")
    
    for file in needToMove:
        fExt = file[file.rfind('.')+1:]
        if fExt=='py':
            try:
                shutil.move(r'C:\Users\Andrey\Desktop' + "\\\\" + file, r'C:\Programming\Python' + "\\\\" + fExt + "\\\\" + file, copy_function=shutil.copy2)
            except FileNotFoundError:
                dirPath = os.path.join('C:\Programming\Python', fExt) 
                os.mkdir(dirPath)
                shutil.move(r'C:\Users\Andrey\Desktop' + "\\\\" + file, r'C:\Programming\Python' + "\\\\" + fExt + "\\\\" + file, copy_function=shutil.copy2)
        if fExt=='doc':
            try:
                shutil.move(r'C:\Users\Andrey\Desktop' + "\\\\" + file, docs + "\\\\" + fExt + "\\\\" + file, copy_function=shutil.copy2)
            except FileNotFoundError:
                dirPath = os.path.join(docs, fExt) 
                os.mkdir(dirPath)
                shutil.move(r'C:\Users\Andrey\Desktop' + "\\\\" + file, docs + "\\\\" + fExt + "\\\\" + file, copy_function=shutil.copy2)
        if fExt=='jpg' or fExt=='png' or fExt=='raw':
            try:
                shutil.move(r'C:\Users\Andrey\Desktop' + "\\\\" + file, pic + "\\\\" + fExt + "\\\\" + file, copy_function=shutil.copy2)
            except FileNotFoundError:
                dirPath = os.path.join(pic, fExt) 
                os.mkdir(dirPath)
                shutil.move(r'C:\Users\Andrey\Desktop' + "\\\\" + file, pic + "\\\\" + fExt + "\\\\" + file, copy_function=shutil.copy2)
        if fExt=='mpeg' or fExt=='mpg' or fExt=='avi' or fExt=='mkv':
            try:
                shutil.move(r'C:\Users\Andrey\Desktop' + "\\\\" + file, vid + "\\\\" + fExt + "\\\\" + file, copy_function=shutil.copy2)
            except FileNotFoundError:
                dirPath = os.path.join(vid, fExt) 
                os.mkdir(dirPath)
                shutil.move(r'C:\Users\Andrey\Desktop' + "\\\\" + file, vid + "\\\\" + fExt + "\\\\" + file, copy_function=shutil.copy2)
tableos=PrettyTable()
tableos.field_names=["В папку", "С раширением"]
tableos.add_row(["Documents",".doc"])
tableos.add_row(["Pictures",".jpg,.raw,.png"])
tableos.add_row(["Programming",".py"])
tableos.add_row(["Video",".mpeg, .mpg, .avi, .mkv"])
needToMove = os.listdir(r'C:\Users\Andrey\Desktop')
if len(needToMove) != 0:
    movefilestrue()
    print('Сортировка прошла успешно')
    print(table)
else:
    print('Нет файлов в корневой папке')
while 1:
    print('Хотите изменить параметры перемещения?')
    print('Yes(press "y")/No(press "n")')
    if keyboard.is_pressed('y'):
        while 1:
            print(table)
            insert=input('Ввод:')
            if insert=='moveto()':
                print('Введите место, куда нужно переместить')
                lstmoveto.append(input())
                print('Введите расширение файлов, которые будут отправляться в эту папку ')
                lstrash.append(input())
                table.add_row(['Переместить в', lstmoveto[k], lstrash[k]])  
            if insert=='movefrom()':
                print('Введите место, откуда нужно перемещать')
                lstmovefrom.append(input())
                print(k1)
                table.add_row(['Переместить из', lstmovefrom[k1], '---'])
            if insert=='exit()':
                break
            if insert=='go()':
                moveFiles()
            if insert=='moveto()': 
                k+=1
            if insert=='movefrom()': 
                k1+=1    
    if keyboard.is_pressed('n'):
        print('Выход из программы')
        break
    click.pause()

