def change(equ: str):
    if "=" not in equ:
        return equ
    formatted = equ.split("=")
    formatted[0] = f"{formatted[0]}-({formatted[1]})"
    return formatted[0]


if __name__ == '__main__':
    print(change(input(">")))
