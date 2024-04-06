def rep_char(c, n):
    print(c * n)

def draw_line_string(msg1, msg2):
    nstr = len(msg1) if (len(msg1) > len(msg2)) else len(msg2)
    rep_char('-', nstr + 7)
    print(f'{msg1}')
    print(f'{msg2}')
    rep_char('-', nstr + 7)
    

name = input("Input his/her name: ")
welcome_msg = "Welcome to Seoul."

draw_line_string(f'Hello {name},', welcome_msg)
