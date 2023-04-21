from rzd import Train
import tkinter as tk
import os
window = tk.Tk()
window.geometry("400x500")
window.title("Продавец")
window["bg"] = "#FCFFFC"
window.iconphoto(False, tk.PhotoImage(file="rzdproject/telegram.png"))
window.resizable(False, False)
new = Train()


def pprint():
    if fio.get() == "ФИО" or fio.get() == "":
        fio["bg"] = "Red"  
        fioL["text"] = "Область обязательная для заполнения"
        return
    else:
        fio["bg"] = "White"
        fioL["text"] = "введите ФИО"
    if city1.get() == "название1" or city1.get() == "":
        city1["bg"] = "Red"
        city1L["text"] = "Область обязательная для заполнения"
        return
    else:
        city1["bg"] = "White"
        city1L["text"] = "город отправления"
    if city2.get() == "название2" or city2.get() == "":
        city2["bg"] = "Red"
        city2L["text"] = "Область обязательная для заполнения"
        return
    else:
        city2["bg"] = "White"
        city2L["text"] = "город приезд"

    new.FIO1(fio.get())
    new.city(city1.get(), city2.get())
    new.services(service.get())
    new.ages(int(ages.get()))
    new.train1(int(Trrain.get()))
    new.ppprint()
    Buy["text"] = "Билет куплен!"
    Buy["bg"] = "Gray"
    Buy["state"] = "disabled"
    os.system("start РЖДбилет.png")


Tim = tk.PhotoImage(file="rzdproject\Train.png")
Rzgimg = tk.PhotoImage(file="rzdproject\РЖД.png").subsample(3, 3)
Timage = tk.Label(master=window, image=Tim, height=500, bg="White")
RzgLab = tk.Label(window, image=Rzgimg, bg="White")
Timage.place(x=0, y=0)
RzgLab.place(x=290, y=10)
Buy = tk.Button(master=window, text="Купить билет!", bg="Red", fg="Black",
                font=(50), command=pprint)
ins = tk.Label(master=window, text="Федеоальная гос\nкомпания", bg="White",
               fg="Red")
fioL = tk.Label(master=window, text="введите ФИО", fg="Black", bg="White")
fio = tk.Entry(master=window, fg="Black", bg="White")
serviceL = tk.Label(master=window, text="согласны на сервис(Да или Нет)",
                    fg="Black", bg="White")
service = tk.Entry(master=window, fg="Black", bg="White")
agesL = tk.Label(master=window, text="Сколько вам лет?", fg="Black", bg="White")
ages = tk.Entry(master=window, fg="Black", bg="White")
TrainL = tk.Label(master=window, text="какое вы хотите место?", fg="Black",
                  bg="White")
Trrain = tk.Entry(master=window, fg="Black", bg="White")
city1L = tk.Label(master=window, text="город отправления", fg="Black",
                  bg="White")
city1 = tk.Entry(master=window, fg="Black", bg="White")
city2L = tk.Label(master=window, text="город приезда", fg="Black", bg="White")
city2 = tk.Entry(master=window, fg="Black", bg="White")
Buy.place(x=125, y=400)
ins.place(x=25, y=25)
fioL.pack()
fio.pack(pady=10)
fio.insert(0, "ФИО")
serviceL.pack()
service.pack(pady=10)
service.insert(0, "Нет")
agesL.pack()
ages.pack(pady=10)
ages.insert(0, 0)
TrainL.pack()
Trrain.pack(pady=10)
Trrain.insert(0, 1)
city1L.pack()
city1.pack(pady=10)
city1.insert(0, "название1")
city2L.pack()
city2.pack(pady=10)
city2.insert(0, "название2")
window.mainloop()
