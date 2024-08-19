import pyautogui
import time
import tkinter as tk
from tkinter import ttk
import keyboard

is_running = False  # Biến trạng thái để kiểm tra tiến trình đang chạy hay không
unlimited_clicks = False  # Biến trạng thái cho checkbox

def start_autoclick():
    global is_running, unlimited_clicks
    is_running = True
    clicks = float("inf") if unlimited_clicks else int(clicks_entry.get())  # Số lần click vô hạn nếu checkbox được chọn
    interval = float(interval_entry.get())
    button = button_var.get()

    print("Bắt đầu autoclick...")

    while is_running:  # Vòng lặp vô hạn nếu không giới hạn số lần click
        if not unlimited_clicks and clicks <= 0:  # Kiểm tra số lần click nếu không chọn checkbox
            break
        pyautogui.click(button=button)
        time.sleep(interval)
        if not unlimited_clicks:
            clicks -= 1  # Giảm số lần click nếu không chọn checkbox

    print("Dừng autoclick")
    is_running = False

def toggle_autoclick():
    global is_running
    if is_running:
        is_running = False
    else:
        start_autoclick()

def toggle_unlimited_clicks():
    global unlimited_clicks
    unlimited_clicks = not unlimited_clicks  # Đảo ngược trạng thái checkbox

# Tạo cửa sổ giao diện
window = tk.Tk()
window.title("AutoClicker")

# Nhập số lần click
clicks_label = ttk.Label(window, text="Số lần click:")
clicks_label.grid(column=0, row=0, padx=5, pady=5)
clicks_entry = ttk.Entry(window)
clicks_entry.grid(column=1, row=0, padx=5, pady=5)

# Nhập khoảng cách giữa các lần click
interval_label = ttk.Label(window, text="Khoảng cách (giây):")
interval_label.grid(column=0, row=1, padx=5, pady=5)
interval_entry = ttk.Entry(window)
interval_entry.grid(column=1, row=1, padx=5, pady=5)

# Chọn nút chuột
button_label = ttk.Label(window, text="Nút chuột:")
button_label.grid(column=0, row=2, padx=5, pady=5)
button_var = tk.StringVar(value="left")
button_left = ttk.Radiobutton(window, text="Trái", variable=button_var, value="left")
button_left.grid(column=1, row=2, sticky="w")
button_right = ttk.Radiobutton(window, text="Phải", variable=button_var, value="right")
button_right.grid(column=1, row=3, sticky="w")
# Checkbox không giới hạn số lần click
unlimited_var = tk.BooleanVar(value=False)
unlimited_check = ttk.Checkbutton(window, text="Không giới hạn số lần click", variable=unlimited_var, command=toggle_unlimited_clicks)
unlimited_check.grid(column=0, row=4, columnspan=2, padx=5, pady=5)
# Lable Hướng dẫn
button_label = ttk.Label(window, text="Nhấn nút (F8) để bắt đầu hoặc kết thúc tiến trình")
button_label.grid(column=0, row=5, columnspan=2, padx=5, pady=10)
# Nút bắt đầu
start_button = ttk.Button(window, text="Bắt đầu", command=start_autoclick)
start_button.grid(column=0, row=6, columnspan=2, padx=5, pady=10)

keyboard.add_hotkey("f8", toggle_autoclick)  # Sử dụng phím F8 để bắt đầu/dừng
window.mainloop()
