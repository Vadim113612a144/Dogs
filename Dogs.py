import requests
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
from io import BytesIO

def get_random_dog_image():
    try:
        response = requests.get('https://dog.ceo/api/breeds/image/random')
        response.raise_for_status()
        data = response.json()
        return data['message']
    except Exception as e:
        messagebox.showerror("Ошибка", f"Ошибка при запросе к API: {e}")
        return None

def show_image():
    image_url = get_random_dog_image()  # ssylka na kartinku prishlet = функция
    if image_url:
        try: # защита от ошибок
            response = requests.get(image_url, stream=True) # на запрос получаем из интернета по ссылке
            response.raise_for_status() # обрабатываем ошибки
            img_data = BytesIO(response.content)  # загружаем контент в двоич коде
            img = Image.open(img_data) # ложим в img картинку
            img.thumbnail((300, 300))  # размер картинкти
            img = ImageTk.PhotoImage(img) # v Photo
            label.config(image=img)  # в лейбл картинку
            label.image = img  # чтоб не собрал мусор

        except requests.RequestException as e:
            messagebox.showerror("Ошибка", f"Не удалось загрузить изображение: {e}")

window = Tk()
window.title("Картинки с собачками")
window.geometry("360x420")

label = Label()
label.pack(padx=10, pady=10) # otstup

# knopka
button = Button(text="Загрузить изображение", command=show_image)
button.pack(padx=10, pady=10) # otstup


window.mainloop()
