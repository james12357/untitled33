"""
Generate a random password. Merged into toolbox.py.
"""
while True:
    a = int(input("密码位数"))
    print(''.join(
        __import__('random').choice('ahui0-]}{?lubfGYUIABVEIIYYHULIAYUIIAWYAGO'
                                    'UGAUSHIuityrtwtbyui,xmjnhcgbd9456!@#$%^'
                                    '&*(526478253674][][') for i in range(0, a)))
