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
table.field_names=["Папки", "Место ввода/вывода", "Расширение"]
tableos=PrettyTable()
tableos.field_names=["В папку", "С раширением"]
def moveFiles():
    needToMove = os.listdir(lstmovefrom[k1-1])
    if len(needToMove) == 0:
        return
    for file in needToMove:
        k3=1
        fExt = file[file.rfind('.')+k3:]
        while fExt!=lstrash[k-1]:
            k3+=1
            fExt=file[file.rfind('.'+k3)]
        k3=1
        try:
            shutil.move(lstmovefrom[k1-1] + "\\\\" + file, lstmoveto[k-1] + "\\\\" + fExt + "\\\\" + file, copy_function=shutil.copy2)
        except FileNotFoundError:
            dirPath = os.path.join(lstmoveto[k-1], fExt) 
            os.mkdir(dirPath)
            shutil.move(lstmovefrom[k1-1] + "\\\\" + file, lstmoveto[k-1] + "\\\\" + fExt + "\\\\" + file, copy_function=shutil.copy2)
def movefilestrue():
    docs=(f"{os.environ['USERPROFILE']}\\Documents")
    pic=(f"{os.environ['USERPROFILE']}\\Pictures")
    vid=(f"{os.environ['USERPROFILE']}\\Videos")
    
    for file in needToMove:
        fExt = file[file.rfind('.')+1:]
        if fExt=='py':
            tableos.add_row(["Programming", fExt])
            try:
                shutil.move(f"{os.environ['USERPROFILE']}\\Desktop" + "\\\\" + file, r'D:\Programing\Python' + "\\\\" + fExt + "\\\\" + file, copy_function=shutil.copy2)
            except FileNotFoundError:
                dirPath = os.path.join('D:\Programming\Python', fExt) 
                os.mkdir(dirPath)
                shutil.move(f"{os.environ['USERPROFILE']}\\Desktop" + "\\\\" + file, r'D:\Programing\Python' + "\\\\" + fExt + "\\\\" + file, copy_function=shutil.copy2)
        if fExt=='doc' or fExt=='docx' or fExt=='xls' or fExt=='xlsx' or fExt=='odt' or fExt=='ods' or fExt=='odp' or fExt=='pdf' or fExt=='rtf' or fExt=='txt':
            tableos.add_row(["Documents", fExt])
            try:
                shutil.move(f"{os.environ['USERPROFILE']}\\Desktop" + "\\\\" + file, docs + "\\\\" + fExt + "\\\\" + file, copy_function=shutil.copy2)
            except FileNotFoundError:
                dirPath = os.path.join(docs, fExt) 
                os.mkdir(dirPath)
                shutil.move(f"{os.environ['USERPROFILE']}\\Desktop" + "\\\\" + file, docs + "\\\\" + fExt + "\\\\" + file, copy_function=shutil.copy2)
        if fExt=='jpg' or fExt=='png' or fExt=='raw':
            tableos.add_row(["Pictures",fExt])
            try:
                shutil.move(f"{os.environ['USERPROFILE']}\\Desktop" + "\\\\" + file, pic + "\\\\" + fExt + "\\\\" + file, copy_function=shutil.copy2)
            except FileNotFoundError:
                dirPath = os.path.join(pic, fExt) 
                os.mkdir(dirPath)
                shutil.move(f"{os.environ['USERPROFILE']}\\Desktop" + "\\\\" + file, pic + "\\\\" + fExt + "\\\\" + file, copy_function=shutil.copy2)
        if fExt=='mpeg' or fExt=='mpg' or fExt=='avi' or fExt=='mkv':
            tableos.add_row(["Video", fExt])
            try:
                shutil.move(f"{os.environ['USERPROFILE']}\\Desktop" + "\\\\" + file, vid + "\\\\" + fExt + "\\\\" + file, copy_function=shutil.copy2)
            except FileNotFoundError:
                dirPath = os.path.join(vid, fExt) 
                os.mkdir(dirPath)
                shutil.move(f"{os.environ['USERPROFILE']}\\Desktop" + "\\\\" + file, vid + "\\\\" + fExt + "\\\\" + file, copy_function=shutil.copy2)
needToMove = os.listdir(f"{os.environ['USERPROFILE']}\\Desktop")
if len(needToMove) != 0:
    movefilestrue()
    print('Сортировка прошла успешно')
    print(tableos)
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
                print('Введите расширение для файлов, которые будут отправляться в эту папку ')
                lstrash.append(input())
                table.add_row(['Переместить в', lstmoveto[k], lstrash[k]])  
            if insert=='movefrom()':
                print('Введите место, откуда нужно перемещать')
                lstmovefrom.append(input())
                table.add_row(['Переместить из', lstmovefrom[k1], '---'])
            if insert=='exit()':
                break
            if insert=='go()':
                moveFiles()
            if insert=='moveto()': 
                k+=1
            if insert=='movefrom()': 
                k1+=1    
    click.pause()
    if keyboard.is_pressed('n'):
            print('Выход из программы')
            break
