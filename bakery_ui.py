import tkinter
from tkinter import *


class BakeryView:
    def __init__(self, window):
        self.__init_window(window)

    def __init_window(self, window):
        window.title("빵집")
        window.geometry('400x200')
        label = Label(window, text='주문내역')
        label.pack()
        self.orderText = Text(window)
        self.orderText.pack()

    def add_order(self, orders):
        self.orderText.insert(0.0, orders + "\n")


class CustomerView:
    def __init__(self, name, window, bakery_view):
        self.name = name
        self.__init_window(window)
        self.bakeryView = bakery_view

    def __init_window(self, window):
        window.title("고객: " + self.name)
        window.geometry('350x200')

        san_label = Label(window, text="샌드위치 (5000원)")
        san_label.pack()
        self.san_orders = Entry(window)
        self.san_orders.pack()
        cak_label = Label(window, text="케이크 (20000원)")
        cak_label.pack()
        self.cak_orders = Entry(window)
        self.cak_orders.pack()

        button = Button(window, text="주문하기", command=self.send_order)
        button.pack()



    def send_order(self):
        try:
            x = int(self.san_orders.get())
        except ValueError:
            x = 0
        try:
            y = int(self.cak_orders.get())
        except ValueError:
            y = 0
        if x ==0:
            if y == 0:
                pass
            else:
                order_text = self.name + ": 케이크 (20000원) " + str(y) + "개"
        else:
            if y==0:
                order_text = self.name + ": 샌드위치 (5000원) " + str(x) + "개"
            else:
                order_text = self.name + ": 샌드위치 (5000원) " + str(x) + "개, 케이크 (20000원) "+str(y)+"개"
        self.bakeryView.add_order(order_text)


if __name__ == '__main__':
    app = Tk()
    bakery = BakeryView(app)
    CustomerView('고객A', Toplevel(app), bakery)
    CustomerView('고객B', Toplevel(app), bakery)
    app.mainloop()
