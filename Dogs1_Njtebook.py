import requests
from tkinter import *
from tkinter import messagebox
from tkinter import ttk  # импортировали ttk
from PIL import Image, ImageTk
from io import BytesIO

def get_random_dog_image():
    try:
        response = requests.get('https://dog.ceo/api/breeds/image/random') # на запрос получаем из интернета по ссылке
        response.raise_for_status()  # получаем статус (если 200 ок)
        data = response.json() # в data -> положили ответ в формате JSON
        print(data)
        print(data['message'])
        print(data['status'])
        return data['message']  # возвращаем информацию по ключу 'message'
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
            img_size = (int(width_spinbox.get()), int(height_spinbox.get()))
            img.thumbnail(img_size)  # размер картинкти из spinbox.get()
            img = ImageTk.PhotoImage(img) # v Photo

            tab = ttk.Frame(notebook)
            # notebook.add(tab, text=f"Изобр ")
            # Нумеруем изображения: к индексу окна (это 0) + 1
            notebook.add(tab, text=f"Изобр № {notebook.index('end') + 1}")
            lb = ttk.Label(tab, image=img) # изображение в новое око
            lb.pack()

            lb.image = img  # чтоб не собрал мусор

        except requests.RequestException as e:
            messagebox.showerror("Ошибка", f"Не удалось загрузить изображение: {e}")
    # Останавливаем прогрессбар после загрузки картинки
    progress.stop()


def progress():
    # Ставим прогрессбар в начальное положение
    progress['value'] = 0
    # Запускаем прогрессбар и увеличиваем значение от 0 до 100 за 3 секунды
    progress.start(30)
    window.after(3000, show_image)


window = Tk()
window.title("Картинки с собачками")
window.geometry("360x420")

label = ttk.Label()
label.pack(padx=10, pady=10) # otstup

# knopka
button = ttk.Button(text="Загрузить изображение", command=progress)
button.pack(padx=10, pady=10) # otstup

# Используем ttk.Progressbar для индикации загрузки
progress = ttk.Progressbar(mode='determinate', length=300)
progress.pack(padx=10, pady=10)

# Ширина
width_label = ttk.Label(text="Ширина:")
width_label.pack(side='left', padx=(10, 0))
width_spinbox = ttk.Spinbox(from_=200, to=500, increment=50, width=5)
width_spinbox.pack(side='left', padx=(0, 10))
width_spinbox.set(300)

# Высота
height_label = ttk.Label(text="Высота:")
height_label.pack(side='left', padx=(10, 0))
height_spinbox = ttk.Spinbox(from_=200, to=500, increment=50, width=5)
height_spinbox.pack(side='left', padx=(0, 10))
height_spinbox.set(300)

# Создаем отдельное окно для Notebook
top_level_window = Toplevel(window)
top_level_window.title("Изображения пёсиков")

notebook = ttk.Notebook(top_level_window)
notebook.pack(expand=True, fill='both', padx=10, pady=10)


window.mainloop()
