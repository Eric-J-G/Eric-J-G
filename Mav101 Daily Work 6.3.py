def plz_dont_error():
    try:
        with open("message_3.txt") as f:
            s = f.read()
            print(s)

    except:
        with open("message_3.txt", 'w') as f:
            f.write("Eric was Here\n")
            f.write("Pearl Jam Rules!")

plz_dont_error()