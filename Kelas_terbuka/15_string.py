data = "ini adalah string"
print(data)
print(type(data))

'''
    1. dengan menggunakan single quote
    2. dengan menggunakan double quote
'''

data = 'menggunakan single quote'
print(data)
data = "menggunakan double quote"
print(data)

print('"Halo, apa kabar?"') # double quote di dalam
print("'Halo, apa kabar?'") # single quote di dalam

print('mari salat jum\'at') # apostrope
print("C:\\user\\ucup") # backslash
print("ucup\t\totong, semakin jauhan") # tab
print("ucup  \botong, jadi deketan") # backspace
print("baris pertama. \nbaris kedua.") # newline (LF)
print("baris pertama. \rbaris kedua.") # carriage return (CR)
print("baris pertama. \r\nbaris kedua.") # carriage return + newline (CRLF)
print(r'C:\new folder') # raw string
# multiline literal string
print("""
Nama  : Ucup
Kelas : 3 SD
""")