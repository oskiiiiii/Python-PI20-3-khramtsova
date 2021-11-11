import os
import sys
import shutil

import settings as sett

sett.start()

def help():
    print('''Помощь - help
Текущее расположение - dir
Создать папку - makeDir [название папки]
Удалить папку - delDir [название папки]
Создать текстовый файл - makeFile [название файла]
Записать текст в файл - addFile [название файла]
Посмотреть содержимое файла - viewFile [название файла]
Удалить файл - delFile [название файла]
Скопировать файл - copyFile [название файла] [путь]
Переместить файл [команда, имя_файла, путь] - moveFile [название файла] [путь]
Переимновать файл - renameFile [название файла] [новое название файла]
Открыть папку - cd [название папки]
Закрыть папку - up
Выйти - exit''')


def pwd():
    print(os.getcwd())


def makeDir(dirName):
    try:
        os.mkdir(dirName)
    except:
        print('file already exists')


def delDir(dirName):
    try:
        os.rmdir(dirName)
    except:
        print('Файл не существует')


def makeFile(fileName):
    file = open(fileName, "w+")
    file.close()


def addFile(filename, w):
    try:
        f = open(filename, "a")
        f.write(w)
        f.close()
    except:
        print('Файл не существует')


def viewFile(fileName):
    try:
        file = open(fileName, "r")
        print(file.read())
        file.close()
    except:
        print('Файл не существуетs')


def delFile(fileName):
    try:
        os.remove(fileName)
    except:
        print('Файл не существует')


def copyFile(fileName, newFilename):
    try:
        shutil.copy(fileName, newFilename)
    except:
        print('Файл не существует')


def moveFile(fileName, newFilename):
    try:
        shutil.move(fileName, newFilename)
    except:
        print('Файл не существует')


def renameFile(fileName, newFilename):
    try:
        os.rename(fileName, newFilename)
    except:
        print('Файл не существует')


def chpwd(dirName):
    try:
        OS = sys.platform
        if OS == 'darwin':
            a = os.getcwd()
            os.chdir(a + '/' + dirName)
            print(os.getcwd())

        elif OS == 'cygwin' or OS == 'win32':
            a = os.getcwd()
            os.chdir(a+'\\'+dirName)
            print(os.getcwd())
    except:
        print('Папка не существует')


def chpwdUp():
    try:
        z=os.getcwd()
        OS = sys.platform
        if OS == 'darwin':
            a = os.getcwd()
            b = a.split('/')
            del b[-1]
            a = '/'.join([str(item) for item in b])
        elif OS == 'cygwin' or OS == 'win32':
            a = os.getcwd()
            b = a.split('\\')
            del b[-1]
            a='\\'.join([str(item) for item in b])
        
        if (sett.path in b):
            os.chdir(a)
            print(os.getcwd())
        else:
            print("Действие недоступно")
            print(os.getcwd())
    except:
        print('Действие недоступно!')


print("Добро пожаловать в демо файловый менеджер")
while True:
    command = input('Введите команду: ')
    command = command.split(' ')
    if command[0] == 'exit':
        sys.exit()
    elif command[0] == 'help':
        help()
    elif command[0] == 'makeDir':
        makeDir(command[1])
    elif command[0] == 'delDir':
        delDir(command[1])
    elif command[0] == 'makeFile':
        makeFile(command[1])
    elif command[0] == 'viewFile':
        viewFile(command[1])
    elif command[0] == 'addFile':
        contentWrap = input("Текст: ")
        addFile(command[1], contentWrap)
    elif command[0] == 'dir':
        pwd()
    elif command[0] == 'delFile':
        delFile(command[1])
    elif command[0] == 'copyFile':
        copyFile(command[1], command[2])
    elif command[0] == 'moveFile':
        moveFile(command[1], command[2])
    elif command[0] == 'renameFile':
        renameFile(command[1], command[2])
    elif command[0] == 'cd':
        chpwd(command[1])
    elif command[0] == 'up':
        chpwdUp()
    else:
        print('команды не существует')
