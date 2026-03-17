import tkinter as tk

def f2c(temp_f):
    return (temp_f - 32) * 5.0/9.0

def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)

def HolZzack(num):
    return "짝수" if num % 2 == 0 else "홀수"

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def even_sum(n):
    return sum([x for x in range(1, n + 1) if x % 2 == 0])

def run():
    try:
        choice = var.get()
        num = float(entry.get())

        if choice == "온도변환":
            result = f"{num}°F → {f2c(num):.2f}°C"

        elif choice == "팩토리얼":
            result = f"{int(num)}! = {fact(int(num))}"

        elif choice == "홀짝판별":
            result = f"{int(num)}은 {HolZzack(int(num))}"

        elif choice == "소수판별":
            result = "소수입니다" if is_prime(int(num)) else "소수가 아닙니다"

        elif choice == "짝수합":
            result = f"1~{int(num)} 짝수합 = {even_sum(int(num))}"

        result_label.config(text=result)

    except:
        result_label.config(text="입력 오류")

root = tk.Tk()
root.title("🔥 멀티 계산기 🔥")
root.geometry("1000x600")
root.config(bg="#222831")

title = tk.Label(root, text="hw02 programes",
                 font=("Arial", 16, "bold"),
                 fg="white", bg="#222831")
title.pack(pady=10)

var = tk.StringVar(value="온도변환")

options = ["온도변환", "팩토리얼", "홀짝판별", "소수판별", "짝수합"]
menu = tk.OptionMenu(root, var, *options)
menu.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 12), justify="center")
entry.pack(pady=10)

btn = tk.Button(root, text="실행",
                font=("Arial", 12, "bold"),
                bg="#00ADB5", fg="white",
                command=run)
btn.pack(pady=10)

result_label = tk.Label(root, text="결과가 여기에 표시됩니다",
                        font=("Consolas", 11),
                        fg="#EEEEEE", bg="#222831",
                        wraplength=300)
result_label.pack(pady=20)

root.mainloop()