
class Cell:
    DEAD_CELL_COLOR = "#000000"
    ALIVE_CELL_COLOR = "#ffffff"
    def __init__(self,button,x,y):
        self.button = button
        self.state = "D"
        self.x = x
        self.y = y
        self.nextState = "L"
        button.configure(bg=Cell.DEAD_CELL_COLOR)

    def toggleState(self):
        if self.state == "D":
            self.state = "L"
            self.button.configure(bg=Cell.ALIVE_CELL_COLOR)
        else:
            self.state = "D"
            self.button.configure(bg=Cell.DEAD_CELL_COLOR)
    def changeState(self,state):
        if self.state==state:
            return
        self.state = state
        if(state == "D"):
            self.button.configure(bg=Cell.DEAD_CELL_COLOR)
            return
        self.button.configure(bg=Cell.ALIVE_CELL_COLOR)
        
    def findNextState(self,cellMatrix):
        count = self.countLiveCells(self.x,self.y,cellMatrix)
        if((count>3 or count<2) and self.state == "L"):
            self.nextState = "D"
            return
        if(count == 3 and self.state=="D"):
            self.nextState = "L"
            return
        self.nextState = self.state
        
    def countLiveCells(self,x,y,cellMatrix):
        rows = len(cellMatrix)
        columns = len(cellMatrix[0])
        count = 0
        if x>0 and y>0 and cellMatrix[x-1][y-1].state == "L":
            count+=1
        if x>0 and cellMatrix[x-1][y].state == "L":
            count+=1
        if x>0 and y<(columns-1) and cellMatrix[x-1][y+1].state == "L":
            count+=1
        if y>0 and cellMatrix[x][y-1].state == "L":
            count+=1
        if y<(columns-1) and cellMatrix[x][y+1].state == "L":
            count+=1
        if x<(rows-1) and y>0 and cellMatrix[x+1][y-1].state == "L":
            count+=1
        if x<(rows-1) and cellMatrix[x+1][y].state == "L":
            count+=1
        if  x<(rows-1) and y<(columns-1) and cellMatrix[x+1][y+1].state == "L":
            count+=1
        return count