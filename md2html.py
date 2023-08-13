import markdown

text = ""

try:
    with open(input("Enter the path of the file to translate in html : "), mode="r", encoding="utf8") as md:
        for line in md:
            text += line
    html = markdown.markdown(text)
    new_file = open(input("Enter the new file name with .html extension :"), "w+")
    new_file.write(html)

except FileNotFoundError as error:
        print("Impossible d'ouvrir le fichier ! %s " % error)
