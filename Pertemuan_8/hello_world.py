# import tkinter as tk

# def show_message():
#     label.config(text="Hello World!")
    
# root = tk.Tk()
# root.title("Hello World App")

# button = tk.Button(root, text="Click Me", command=show_message)
# button.pack(pady=20)

# label = tk.Label(root, text="")
# label.pack(pady=20)

# root.mainloop()

# import tkinter as tk

# class HelloWorldApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Hello World App")

#         self.button = tk.Button(self.root, text="Click Me", command=self.show_message)
#         self.button.pack(pady=20)

#         self.label = tk.Label(self.root, text="")
#         self.label.pack(pady=20)

#     def show_message(self):
#         self.label.config(text="Hello World!")

# # Inisialisasi dan jalankan aplikasi
# if __name__ == "__main__":
#     root = tk.Tk()
#     app = HelloWorldApp(root)
#     root.mainloop()

import tkinter as tk

class WelcomeButton:
    def __init__(self, root, label):
        self.label = label
        self.button = tk.Button(root, text="Tampilkan Selamat Datang", command=self.show_welcome)
        self.button.pack(pady=10)

    def show_welcome(self):
        self.label.config(text="Selamat Datang!")

class HelloWorldApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hello World App")

        self.label = tk.Label(self.root, text="")
        self.label.pack(pady=10)

        self.entry = tk.Entry(self.root)
        self.entry.pack(pady=10)
        self.entry.bind("<Return>", self.show_user_text)  # Tekan Enter

        self.hello_button = tk.Button(self.root, text="Click Me", command=self.show_hello)
        self.hello_button.pack(pady=10)

        self.welcome_button = WelcomeButton(self.root, self.label)

    def show_hello(self):
        self.label.config(text="Hello World!")

    def show_user_text(self, event=None):
        user_text = self.entry.get()
        self.label.config(text=user_text)

# Jalankan aplikasi
if __name__ == "__main__":
    root = tk.Tk()
    app = HelloWorldApp(root)
    root.mainloop()

