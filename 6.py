try:
    from tkinter import messagebox, simpledialog, Tk
    import pyperclip


    def g_t():
        ta = simpledialog.askstring("询问", "解密或加密?")
        return ta


    def g_m():
        ta1 = simpledialog.askstring("询问", "秘密消息?")
        return ta1


    def is_even_n(n):
        return n % 2 == 0


    def g_e_n(message):
        even = []
        for counter in range(0, len(message)):
            if is_even_n(counter):
                even.append(message[counter])
        return even


    def g_o_n(message):
        odd = []
        for counter in range(0, len(message)):
            if not is_even_n(counter):
                odd.append(message[counter])
        return odd


    def swap_letters(message):
        letter_list = []
        if not is_even_n(len(message)):
            message = message + "x"
        even_letters = g_e_n(message)
        odd_letters = g_o_n(message)
        for counter in range(0, int(len(message) / 2)):
            letter_list.append(odd_letters[counter])
            letter_list.append(even_letters[counter])
        new_message = "".join(letter_list)
        return new_message


    root = Tk()
    root.withdraw()
    while True:
        me = g_m()
        messagebox.showinfo("", me)
        encrypted = swap_letters(me)
        messagebox.showinfo("加密信息已复制！", encrypted)
        pyperclip.copy(encrypted)
    root.mainloop()
except BaseException:
    pass
