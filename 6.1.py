from tkinter import messagebox, simpledialog, Tk
from random import choice


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
    for counter in range(0, int(len(message)/2)):
        letter_list.append(odd_letters[counter])
        letter_list.append(even_letters[counter])
    new_message = "".join(letter_list)
    return new_message


def fl(message):
    en_list = []
    fake_letters = ["a", "s", "v", "r", "b"]
    for counter in range(0, len(message)):
        en_list.append(message[counter])
        a = choice[fake_letters]
        en_list.append()
    new_message = "".join(en_list)
    new_message2 = swap_letters(new_message)
    return new_message2


def de_fl(message):
    even_letters = g_e_n(message)
    new_message = "".join(even_letters)
    new_message2 = swap_letters(new_message)
    return new_message2


def encrypt(message):
    swapped_message = swap_letters(message)
    encrypted_message = "".join(reversed(swapped_message))
    return encrypted_message


def decrypt(message):
    unreversed_message = "".join(reversed(message))
    decrypted_message = swap_letters(unreversed_message)
    return decrypted_message


root = Tk()
while True:
    t = g_t()
    if t == "加密":
        me = g_m()
        encrypted = fl(me)
        messagebox.showinfo("", encrypted)
    elif t == "解密":
        me = g_m()
        decrypted = de_fl(me)
        messagebox.showinfo("", decrypted)
    else:
        break
root.mainloop()
