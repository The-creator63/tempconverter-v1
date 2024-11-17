from tkinter import*

root = Tk()
root.geometry("500x250")
root.title("Celsius to Fahrenheit Converter")

main_hd = Label(root,text = "Celsius -> Fahrenheit",fg = "Black",font = ("Times",20,"bold"))
main_hd.pack()

frame = Frame(root)
frame.pack(pady = 20)
celsius_lbl = Label(frame,text = "Enter temperature in Celsius: ",font = ("Times",10,"bold"))
celsius_lbl.grid(row = 0,column = 0)
root.mainloop()