import tkinter as tk
from Cell import Cell

ROWS = 20
COLUMNS = 20

root = tk.Tk()
root.title("Conway's Game of Life")
pixelVirtual = tk.PhotoImage(width=1, height=1)

def onclick(event):
    button = event.widget
    cell = cellMatrix[button.grid_info()["row"]][button.grid_info()["column"]]
    cell.toggleState()                     
      
def start(event):
    event.widget.unbind("<Button-1>")
    event.widget.configure(state="disabled")
    root.after(300,loop)  
             
def loop():
    for i in range(ROWS):
        for j in range(COLUMNS):
            cellMatrix[i][j].findNextState(cellMatrix)
    for i in range(ROWS):
        for j in range(COLUMNS):
            cellMatrix[i][j].changeState(cellMatrix[i][j].nextState)
    root.after(300,loop)   
      
cellMatrix = []      
for i in range(ROWS):
    cellsRow = []
    for j in range(COLUMNS):
        button = tk.Button(root,image=pixelVirtual,width=30,height=30)
        button.grid(row=i,column=j)
        button.bind("<Button-1>",onclick)
        cellsRow.append(Cell(button,i,j))
    cellMatrix.append(cellsRow)
     
startButton = tk.Button(root,text="Start")
startButton.bind("<Button-1>",start)
startButton.grid(row=ROWS,column=int(COLUMNS/2))
root.eval('tk::PlaceWindow . center')

root.mainloop()
