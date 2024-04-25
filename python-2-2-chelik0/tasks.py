import os

def t1():
    """
    Создайте программу возвращающую информацию о системе вида:
    Операционная система - ХХХ
    Имя компьютера - ХХХ
    Имя пользователя - ХХХ
    """
    print(f"Операционная система - {'Windows' if os.name == 'nt' else 'unix'}\n",
        f"\bИмя компьютера - {os.environ["COMPUTERNAME"]}\n",
        f"\bИмя пользователя - {os.environ["USERNAME"]}")


def t2(dir: str, num: int):
    """
    Создайте программу создающую папку dir внутри которой еще num папок,
    имена которых цифры от 1 до num
    """
    if not os.path.exists(dir):
        os.mkdir(dir)
        for i in range(1, num+1):
            os.mkdir(fr".\{dir}\{i}")


def t3(dir: str, name: str):
    """
    Напишите программу-вирус, которая переименовывает папки c четными номерами 
    в ранее созданной папке dir, новые имена должны начинаться со строки name.
    """
    if os.path.exists(dir):
        for i in os.listdir(dir):
            if int(i)%2 == 0:
                os.rename(fr".\{dir}\{i}", fr".\{dir}\{name}_{i}")


def t4(dir: str, text: str):
    """
    Напишите программу которая создает папку dir и записывает 
    текст text в файл answer.txt
    """
    if not os.path.exists(dir):
        os.mkdir(dir)
        if not os.path.exists("answer.txt"):
            with open(fr".\{dir}\answer.txt", 'w') as file:
                file.write(text)
    
# t1()
# t2("diiiir", 20)
# t3("diiiir", "soks")
# t4("for_text", "hello world")