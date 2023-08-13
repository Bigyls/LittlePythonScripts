eml = ""
try:
    with open(input("Enter the path of the file in .mct for translation in .eml : "), mode="r", encoding="utf8") as mct:
        for line in mct:
            if "+" in line[0]:
                continue
            eml += line
        new_file = open(input("Enter the new file name with .eml extension :"), "w+")
        new_file.write(eml)
except FileNotFoundError as error:
        print("Impossible d'ouvrir le fichier ! %s " % error)
