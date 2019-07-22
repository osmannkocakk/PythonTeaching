zoo = ['lion', "tiger", 'puma']

if __name__ == "__main__":
    f = open("input.txt", "a")  #"w" for the create or first delete(if file exists) then create file

    for i in zoo:
        f.write(i)

    f.close()
