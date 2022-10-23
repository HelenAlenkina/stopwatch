# Tkinter - это графическая библиотека,
# позволяющая создавать программы с оконным интерфейсом в Python
# Импортируется Tkinter точно так же, как и любая другая библиотека на Python
# Модуль datetime предоставляет классы для обработки времени и даты разными способами.
# Определим имя для импортированного модуля, используя оператор import as.
# Название - аналогичное
# Функция datetime импортируется из модуля datetime
import tkinter as Tkinter
from datetime import datetime
counter = 0
working = False


# Label - виджет для отображение текста и картинок
# Создадим функцию counter_label
def counter_label(label):
    def count():
        if working:
            global counter
            #Здесь переменная counter была объявлена в функции count() с помощью
            #ключевого слова global.В процессе работы программы можно увидеть,
            #что изменение значения внутри функции отражается на глобальном значении переменной.
            #Зададим начальное значение.
            if counter == 0:
                start = 'Старт!' #зададим переменной start название во время запуска
            else:
                time = datetime.utcfromtimestamp(counter)
                #возвращает время в секундах с начала момента, с которого время пошло
                string = time.strftime('%H:%M:%S')
                # Функция strftime возвращает строку в зависимости от использованного формата.
                # Здесь %H,%M,%S- час, минута, секунда  как десятичное число с добавлением нуля.
                start = string

            label['text'] = start #text- устанавливает текст/Текст-имя кнопки



            # Метод Tkinter after используется для запуска функции через определенное
            # количество времени.Метод after принимает два параметра: временную задержку и имя функции.
            # Переданная функция будет вызвана по истечении заданной временной задержки.
            # Функция after() занимает время в миллисекундах. От 5000 миллисекунд до 5 секунд.
            label.after(1000, count)
            counter += 1

    #Запускаем счет
    count()


# Запускаем секундомер
def START(label):
    global working
    working = True
    counter_label(label)
    start['state'] = 'disabled'
    stop['state'] = 'normal'
    reset['state'] = 'normal'
#normal - Кнопка может быть нажата
#disabled - кнопка не щелкает
#state - состояние

# Останавливаем секундомер
def STOP():
    global working
    start['state'] = 'normal'
    stop['state'] = 'disabled'
    reset['state'] = 'normal'
    working = False


# Перезапуск секундомера

def RESET(label):
    global counter
    counter = 0
    #перезапуск нажат после нажатия кнопки stop.
    if not working:
        reset['state'] = 'disabled'
        label['text'] = '00:00:00'
    #перезапуск нажат во время работы секундомера
    else:
        label['text'] = '00:00:00'
#title - заголовок окна
#lable - виджет для отображения текста или изображения


root = Tkinter.Tk() # Создаем новое окно
root.title("СЕКУНДОМЕР") #Добавляем заголовок окна

# Зададим размеры окна,minsize и maxsize - минимальный и максимальный размеры окна.
root.minsize(width=300, height=150)
root.maxsize(width=800, height=600)
label = Tkinter.Label(root, text='Начнём!', fg='green', font='arial 30')

#text - какой текст будет отображён на кнопке
#width,height - ширина и длина кнопки
#bg - цвет кнопки (background)
#fg - цвет текста на кнопке (foreground)
#font - шрифт и его размер
#frame - рамка
label.pack()
#Упаковщик pack().При использовании этого упаковщика с помощью свойства side
#нужно указать к какой стороне родительского виджета он должен примыкать.
#Как правило этот упаковщик используют для размещения виджетов
#друг за другом (слева направо или сверху вниз)
#side ("left"/"right"/"top"/"bottom") - к какой стороне должен примыкать
#(влево, вправо, вверх, вниз, соот-но)
#размещаемый виджет
f = Tkinter.Frame(root, bg='green', bd=2)
#cвойство bd отвечает за толщину края рамки
start = Tkinter.Button(f, text='START', width=8, height=4, command=lambda: START(label))
stop = Tkinter.Button(f, text='STOP', width=8, height=4, state='disabled', command=STOP)
reset = Tkinter.Button(f, text='RESET', width=8, height=4, state='disabled', command=lambda: RESET(label))
f.pack(anchor='center', padx=10, pady=10)
#anchor: устанавливает опции растяжения элемента. Может принимать значения n, e, s, w, ne, nw, se, sw, c,
#которые являются сокращениями от North(север - вверх), South (юг - низ),
#East (восток - правая сторона), West (запад - левая сторона) и center (по центру).
#Параметры padx и pady позволяют установить отступ между виджетами
start.pack(side='left')
stop.pack(side='left')
reset.pack(side='left')
root.mainloop() #Запускаем бесконечный цикл окна (до момента его закрытия- постоянно будет открыт)