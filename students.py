with open("alunos.txt", "r") as file:
    file_content = file.read()

for student in file_content.split("\n"): 
    [name, note] = student.split(" ")
    if( int(note) < 6 ):
        print(name)
