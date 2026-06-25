
def main():

    b = bytes([0x41, 0x42, 0x43, 0x44])
    c = b.decode("utf-8")
    

    s = "This is string"
    a = s.encode("utf-8")
    
    d = s.encode("utf-32")

    print(s + c)
    print(a + b)
    print(d)

main()
