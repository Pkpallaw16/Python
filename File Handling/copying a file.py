with open("myfile.txt", "r") as file1:
    lines=file1.readlines()
    print(lines)
    with open("newfile.txt", "w") as file2:
        file2.writelines(lines)
