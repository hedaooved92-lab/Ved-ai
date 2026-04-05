import tkinter as tk
from tkinter import scrolledtext, filedialog
import subprocess

def generate_code():

    prompt = entry.get().lower()

    if "calculator" in prompt:

        code = '''
print("Calculator")

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Add:", a+b)
print("Sub:", a-b)
print("Mul:", a*b)
print("Div:", a/b)
'''

    elif "game" in prompt:

        code = '''
import random

num = random.randint(1,10)

guess = int(input("Guess number: "))

if guess == num:
    print("Win")
else:
    print("Lose")
'''

    else:

        code = f'''
print("AI Generated Code")

print("Project:", "{prompt}")
'''

    output.delete(1.0, tk.END)
    output.insert(tk.END, code)


def run_code():

    code = output.get(1.0, tk.END)

    with open("temp.py","w") as f:
        f.write(code)

    subprocess.Popen(["py","-3.11","temp.py"])


def save_code():

    code = output.get(1.0, tk.END)

    file = filedialog.asksaveasfile(
        defaultextension=".py"
    )

    if file:
        file.write(code)
        file.close()


window = tk.Tk()
window.title("AI Code Generator Pro")
window.geometry("800x600")

entry = tk.Entry(window,width=60)
entry.pack(pady=10)

tk.Button(
window,
text="Generate Code",
command=generate_code
).pack()

tk.Button(
window,
text="Run Code",
command=run_code
).pack()

tk.Button(
window,
text="Save Code",
command=save_code
).pack()

output = scrolledtext.ScrolledText(
window,
width=90,
height=25
)

output.pack(pady=10)

window.mainloop()