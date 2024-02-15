import pyautogui
import time
import pyperclip
import tkinter as tk
from tkinter import ttk

# Function to search for Dollar price
def SearchDolar():
    pyautogui.press("win")
    time.sleep(2)

    # Open Microsoft Edge
    pyautogui.write("microsoft edge")
    time.sleep(2)
    pyautogui.press("enter")
    time.sleep(3)

    # Search for Dollar price
    pyautogui.write("google")
    pyautogui.press("enter")
    time.sleep(3)
    
    pyautogui.write("valor do dolar")  # Search term
   
    pyautogui.press("enter")
    time.sleep(3)

    # Copy Dollar value from the web page
    pyautogui.click(x=249, y=441, clicks=2, interval=0.25)
    pyautogui.hotkey("ctrl", "c")

    # Retrieve copied value
    dolar_str = pyperclip.paste()

    # Convert the retrieved value to float
    dolar = float(dolar_str.replace(',', '.'))

    # Print Dollar value
    print("Valor do dólar:", dolar)

    # Calculate multiplications
    result_str = ""
    for contador in range(2, 11):
        resultado = dolar * contador
        result_str += f"{dolar} x {contador} = {resultado:.2f}\n"

    # Update control variables to update labels in the GUI
    dolarWindow.set("Valor da Moeda escolhida: {:.2f}".format(dolar))
    dolarMultiplicado.set("Multiplicações da moeda escolhida:\n" + result_str)

# Function to search for Euro price
def SearchEuro():
    pyautogui.press("win")
    time.sleep(2)

    # Open Microsoft Edge
    pyautogui.write("microsoft edge")
    time.sleep(2)
    pyautogui.press("enter")
    time.sleep(3)

    # Search for Euro price
    pyautogui.write("google")
    pyautogui.press("enter")
    time.sleep(3)
    
    pyautogui.write("valor do euro")  # Search term
   
    pyautogui.press("enter")
    time.sleep(3)

    # Copy Euro value from the web page
    pyautogui.click(x=249, y=441, clicks=2, interval=0.25)
    pyautogui.hotkey("ctrl", "c")

    # Retrieve copied value
    euro_str = pyperclip.paste()

    # Convert the retrieved value to float
    euro = float(euro_str.replace(',', '.'))

    # Print Euro value
    print("Valor do euro:", euro)

    # Calculate multiplications
    result_str = ""
    for contador in range(2, 11):
        resultado = euro * contador
        result_str += f"{euro} x {contador} = {resultado:.2f}\n"

    # Update control variables to update labels in the GUI
    dolarWindow.set("Valor da Moeda escolhida: {:.2f}".format(euro))
    dolarMultiplicado.set("Multiplicações da moeda escolhida:\n" + result_str)

root = tk.Tk()
root.title("Exemplo com ttk")
root.geometry("400x300")

# Control variables for the texts displayed in the interface
dolarWindow = tk.StringVar()
dolarMultiplicado = tk.StringVar()

# Label for Dollar value
label_dolar = ttk.Label(root, textvariable=dolarWindow)
label_dolar.pack()

# Label for Dollar multiplications
label_multiplicado = ttk.Label(root, textvariable=dolarMultiplicado)
label_multiplicado.pack()

# Button to search for Dollar price
buttonDolar = ttk.Button(root, text="Buscar preço do Dólar", command=SearchDolar)
buttonDolar.pack()

# Button to search for Euro price
buttonEuro = ttk.Button(root, text="Buscar preço do Euro", command=SearchEuro)
buttonEuro.pack()

root.mainloop()
