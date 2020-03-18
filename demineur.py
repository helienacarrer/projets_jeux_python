from tkinter import *
import numpy as np


fen = Tk()  # create window
fen.title('Demineur')
SIZE = 400  # width of the window

can = Canvas(fen, bg="light gray", height=SIZE, width=SIZE)
can.pack()

NB_OF_LINES = 5  # 5 lines
STEP = SIZE/NB_OF_LINES

# horizontal lines
x = 0
while (x <= NB_OF_LINES):
    can.create_line(0, STEP*x, SIZE, STEP*x, fill='blue')
    x = x+1

# vertical lines
y = 0
while (y <= NB_OF_LINES):
    can.create_line(STEP*y, 0, STEP*y, SIZE, fill='blue')
    y = y+1

# fen.mainloop()

#########################
# With rectangles instead of lines --> MIEUX POUR COORDONNEES
fen = Tk()
fen.title("Démineur")
can = Canvas(fen, height=600, width=600)
can.pack()
case = [[can.create_rectangle(i*120,j*120,(i+1)*120,(j+1)*120,fill="#FFFFFF")
                                        for i in range(5)] for j in range(5)]

def callback(event):
        """ Associe au clic de souris l'affichage des tags de l'objet graphique cliqué """
        # On récupere les tags de l'obj graphique dans tag
        items = can.find_withtag("current")
        tag = can.gettags(items)
        txtvar = tag
        print("tag obj graphique : ", txtvar)
        # On récupere les coordonnées du clic souris
        souris = can.find_closest(event.x, event.y)
        # On récupere les coordonnées de l'objet graphique le plus proche du clic souris
        print("coord clic : ", event.x, event.y, " ; coord obj graph visé : ", can.coords(souris[0]))


can.bind('<Button-1>', callback)
fen.mainloop()


##############
def exist(liste, index):
    '''
    check if an index is in a list
    '''
    if index < 0:
        return False
    if index >= len(liste):
        return False
    return True

# create a 5x5 matrix
matrix_zero_one = np.random.randint(2, size=(5,5))
print(matrix_zero_one)
# get matrix into a list
list_zero_one = []
for line in matrix_zero_one:
    for value in line:
        list_zero_one.append(value)

####################################### NOT WORKING 
# total = list_zero_one[index+1] + list_zero_one[index-1] + list_zero_one[index+5] + list_zero_one[index-5]
# le for est pour chaque valeur
for index in range(len(list_zero_one)):
    if list_zero_one[index] == 0:
        total = 0
        if exist(list_zero_one, index + 1):
            total += list_zero_one[index+1]
        if exist(list_zero_one, index - 1):
            total += list_zero_one[index-1]
        if exist(list_zero_one, index + 5):
            total += list_zero_one[index+5]
        if exist(list_zero_one, index - 5):
            total += list_zero_one[index-5]
        list_zero_one[index] = total
    # die if there is a mine
    elif list_zero_one[index] == 1:
        # break
        list_zero_one[index] = 1

# get the list into a matrix
final_matrix = np.array([list_zero_one])
shape = (5, 5)
final_matrix = final_matrix.reshape(shape)
print(final_matrix)
       

################# TO DO ###############################
# add les 4 valeurs manquantes quand == 0 (car 8 cases adjacentes, pas que 4)
# associate final_matrix with front when click
