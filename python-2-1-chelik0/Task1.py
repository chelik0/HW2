"""
Напишите скрипт который выводит надпись "Hello, world",
 если не было передано никаких аргументов.
Если 1 из аргументов "--name" то следующий аргумент должен быть имя. 
В таком случае выведите надпись "Hello, {Имя}"
Пример ввода: python file.py Argument --name John
Пример вывода: Hello, John
"""
import sys

name = "world"

if len(sys.argv) > 2 and "--name" in sys.argv:
    i = sys.argv.index("--name") + 1
    name = sys.argv[i]
    
print(f"Hello {name}")