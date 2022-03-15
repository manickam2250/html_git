with open("/home/manikam/Downloads/css.txt","r")as file1:
    list=file1.read().split(".")
    no=0

    for li in list:
        li=li.replace("\n"," ")
        with open("/home/manikam/Downloads/css1.txt","a")as file2:
            file2.write(str(no)+")")
            file2.write(li+".\n")
            no+=1