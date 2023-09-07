import tkinter as tk
import os
import random
import string
import tkinter.messagebox
from tkinter import filedialog


def generate_password(length=8, use_uppercase=True, use_digits=True, use_special_chars=True):
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def generate_button_clicked():
    length = int(length_entry.get())
    use_uppercase = uppercase_var.get()
    use_digits = digits_var.get()
    use_special_chars = special_chars_var.get()

    password = generate_password(length, use_uppercase, use_digits, use_special_chars)
    name = name_entry.get()

    result_label.config(text="Сгенерированный пароль для '{}' : {}".format(name, password))

    save_button.config(state=tk.NORMAL)  # Активировать кнопку "Сохранить пароль"
    generated_password.set(password)


def save_password():
    password = generated_password.get()
    name = name_entry.get()

    app_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(app_path, "passwords.txt")

    with open(file_path, "a") as file:
        file.write("Name: {}\nPassword: {}\n\n".format(name, password))
        file.close()

    tkinter.messagebox.showinfo("Сохранено", "Пароль сохранен в файле 'passwords.txt'")
    save_button.config(state=tk.DISABLED)  # Деактивировать кнопку после сохранения


def open_faq():
    faq_text = """
    **Часто задаваемые вопросы (FAQ)**

    1. **Для чего предназначен этот генератор паролей?**
       Этот генератор паролей создан для генерации случайных и безопасных паролей, которые могут быть использованы для защиты ваших онлайн аккаунтов.

    2. **Могу ли я выбрать длину пароля и какие символы использовать?**
       Да, вы можете выбрать длину пароля и указать, следует ли использовать заглавные буквы, цифры и специальные символы.

    3. **Как мне сохранить сгенерированный пароль?**
       После генерации пароля, введите имя или описание пароля, затем нажмите "Сгенерировать пароль". После этого кнопка "Сохранить пароль" станет активной.

    4. **Где будут сохранены пароли?**
       Пароли сохраняются в файле 'passwords.txt', который находится в том же каталоге, где находится это приложение.

    """
    tkinter.messagebox.showinfo("FAQ", faq_text)


# Создание графического интерфейса
root = tk.Tk()
root.title("Генератор паролей")

name_label = tk.Label(root, text="Имя/Описание пароля:")
name_label.pack()

name_entry = tk.Entry(root)
name_entry.pack()

length_label = tk.Label(root, text="Длина пароля:")
length_label.pack()

length_entry = tk.Entry(root)
length_entry.pack()

uppercase_var = tk.IntVar()
uppercase_check = tk.Checkbutton(root, text="Использовать заглавные буквы", variable=uppercase_var)
uppercase_check.pack()

digits_var = tk.IntVar()
digits_check = tk.Checkbutton(root, text="Использовать цифры", variable=digits_var)
digits_check.pack()

special_chars_var = tk.IntVar()
special_chars_check = tk.Checkbutton(root, text="Использовать специальные символы", variable=special_chars_var)
special_chars_check.pack()

generate_button = tk.Button(root, text="Сгенерировать пароль", command=generate_button_clicked)
generate_button.pack()

save_button = tk.Button(root, text="Сохранить пароль", command=save_password, state=tk.DISABLED)
save_button.pack()

faq_button = tk.Button(root, text="FAQ", command=open_faq)
faq_button.pack()

generated_password = tk.StringVar()  # Переменная для хранения сгенерированного пароля

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
