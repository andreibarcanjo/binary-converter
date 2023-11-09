import tkinter as tk

def decimal_para_binario():
    try:
        decimal_num = int(input_field.get())
        binary_num = bin(decimal_num).replace("0b","")
        output_label.config(text=f"Binary: {binary_num}")
    except ValueError:
        output_label.config(text="Texto invalido por favor coloque um número decimal")
