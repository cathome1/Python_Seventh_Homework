# Создать телефонный справочник с возможностью импорта и экспорта данных в формате CSV.
import os

def main():
    global file
    ch = int(input('Телефонный справочник\n1)Импортировать номера\n2)Эксортировать номера\n\n0)Выход\n'))
    if ch == 1:
        file = input('Введите название файла для импорта(например test.csv): ')
        if file[-4:] != ".csv":
            print('\nФайл должен иметь расширение .csv\n')
            return main()
        imp_ch = input('''\nТелефонный справочник
1) Добавить номер
2) Добавить несколько номеров вручную
3) Добавить несколько номеров из файла

0) Закрыть Программу
''')
        match (imp_ch) :
            case "1":
                return EnterOneNum()
            case '2':
                return EnterSomeNumbers()
            case '3':
                return EnterFromFile()
            case '0':
                exit()
            case _:
                print('\nВведено некорректное значение\n')
                return main()
        
    elif ch == 2: 
        exp_ch = input('''Телефонный справочник
1) Вывести информацию о телефоне на экран
2) Вывести информацию о нескольких номерах на экран
3) Вывести информацию о нескольких номерах в файл\n''')
        file = input('Введите название файла-справочника: ')
        if file[-4:] != ".csv":
            print('\nФайл должен иметь расширение .csv\n')
            return main()
        match (exp_ch):
            case '1':
                FindOneLine()
            case '2':
                FindAllLines()
            case "3":
                FindToFile()
            case _:
                print('\nВведено некорректное значение\n')
                return main()    


def EnterOneNum(flag = True):
     with open(file, 'a', encoding='utf-8') as imp:
        fam = input("Введите Фамилию: ")
        if len(fam) < 2:
            print("\nФамилия слишком короткая, минимум 2 символа.\n")
            return EnterOneNum() if flag == True else EnterSomeNumbers()
        imya = input('Введите имя: ')
        if len(imya) < 2:
            print("\nИмя слишком короткое, минимум 2 символа.\n")
            return EnterOneNum() if flag == True else EnterSomeNumbers()
        otch = input('Введите отчество (при наличии): ')
        if len(otch)>0 and len(otch)<5:
            print("\nОтчество слишком короткое, минимум 5 символов.\n")
            return EnterOneNum() if flag == True else EnterSomeNumbers()
        num = input("Введите номер без +: ")
        if not num.isdigit():
            print("\nНомер должен состоять только из цифр\n")
            return EnterOneNum() if flag == True else EnterSomeNumbers()
        note = input("Введите заметку(не более 20 символов): ")
        if len(note) > 20:
            print("\nЗаметка должна содержать не более 20 символов\n")
            return EnterOneNum() if flag == True else EnterSomeNumbers()
        res = [fam,imya,otch,num,note]
        imp.write(f"{';'.join(res)}\n")
        print(f"\nНомер успешно импортирован файл {file}\n")
        imp.close()
        if flag:
            return main()

def EnterSomeNumbers():
    count = input("Введите количество импортируемых номеров: ")
    if count.isdigit() and int(count)>0:
        for i in range(1, int(count) + 1):
            print(f"======= Импорт номера №{i} =======")
            EnterOneNum(0)
    else:
        print("\nВведено некорректное значение.\n")
        return EnterSomeNumbers()
    return main()

def EnterFromFile():
    with open(file, 'a', encoding='utf-8') as to_imp:
        f = input('Введите название файла откуда импортировать контакты: ')
        if f[-4:] != ".csv":
            print('\nФайл должен иметь расширение .csv\n')
            return EnterFromFile()
        try:
            with open(f,"r", encoding="utf-8") as from_imp:
                for i in from_imp:
                    to_imp.write(i)
            from_imp.close()
            print(f"\nКонтакты из файла {f} успешно импортированы в файл {file}\n")
        except:
            print('\nДанного файла не существует.\n')
        to_imp.close()
        return main()

def FindOneLine():
    res = ''
    count = 0
    try:
        with open(file, 'r', encoding='utf-8') as exp:
            ch = input('''По какому критерию осуществляется поиск?
1)Фамилия
2)Имя
3)Отчество
4)Телефон

0)Назад\n''')
            if ch == 0: return main
            find = input("Введите данные для поиска: ")
            for i in exp.readlines():
                if i.split(';')[int(ch)-1].lower() == find.lower():
                    count += 1
                    res = i.split(';')
            if count == 1:
                print(res)
            elif count==0:
                print('\nПо вашему запросу ничего не найдено, попробуйте снова\n')
            elif count>1:
                print('По вашему запросу найдено более 1го номера, попробуйте поиск по дугому критерию ')
            return main()
    except:
        print('\nФайл не найден\n')
        return main()

def FindAllLines(flag = True):
    global fal 
    fal = []
    count = 0
    try:
        with open(file, 'r', encoding='utf-8') as exp:
            ch = input('''По какому критерию осуществляется поиск?
1)Фамилия
2)Имя
3)Отчество
4)Телефон

0)Назад\n''')
            if ch == 0: return main
            find = input("Введите данные для поиска: ")
            for i in exp.readlines():
                i = i.replace('\n','')
                if i.split(';')[int(ch)-1].lower() == find.lower():
                    print(i.split(';'))
                    count += 1
                    fal.append(i.split(';'))
            print('')
            if count == 0:
                print('\nПо вашему запросу ничего не найдено, попробуйте снова\n')
                return main()
    except:
        print('\nФайл не найден\n')
    if flag == True: return main()

def FindToFile():
    exfile = input('Введите название файла куда экспортировать данные(например test.csv): ')
    if exfile[-4:] != ".csv":
        print('\nФайл должен иметь расширение .csv\n')
        return main()
    with open(exfile, 'a', encoding='utf-8')as to_exp:
        if os.path.isfile(file):
            with open(file, 'r', encoding='utf-8') as from_exp:
                lines = from_exp.readlines()
                print(f'\nВ файле {len(lines)} контактов\n')
                ch = input('Выберите каким способом выбираем номера для экспорта?\n1)Поиск по критерию\n2)Диапозон номеров строк\n3)Весь файл\n\n0)Назад в меню\n')
                if ch == '1':
                    FindAllLines(False)
                    for k in fal:
                        to_exp.write(f'{";".join(k)}\n')
                    print(f'{len(fal)} контактов импортировано в файл {exfile}\n')
                elif ch == '2':
                    count = 0
                    start = input('Введите с какой строки начать выгрузку: ')
                    if not start.isdigit() or int(start) <= 0 or int(start) > len(lines) :
                        print('Введено некорректное значение, попробуйте снова.')
                        return FindToFile()
                    end = input('Введите на какой строке закончить выгрузку (включительно): ')
                    if not end.isdigit() or int(end) > len(lines) or int(end) < int(start):
                        print('Введено некорректное значение, попробуйте снова.')
                        return FindToFile()
                    for j in lines:
                        count += 1
                        if count>=int(start) and count <= int(end):
                            to_exp.write(f'{j}')
                    print(f'\nНомера успешно экспортированы в файл {exfile}\n')
                elif ch == '3':
                    for i in lines:
                        to_exp.write(i)
                    print(f'\nНомера успешно экспортированы в файл {exfile}\n')
                elif ch == '0':
                    return main()
                else:
                    print('\nВведено некорректное значение, попробуйте заново.\n')
                    return FindToFile()
            from_exp.close()
        else:
            print('\nФайл не найден\n')
    to_exp.close()
    return main()
main()