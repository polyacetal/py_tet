import random
FIELD_HEIGHT = 20

class FieldDraw():

    def __init__(self):
        self.fieldList = [[0 for x in range(FIELD_WIDTH)] for y in range(FIELD_HEIGHT)]
        self.emptyBlock = "□ "
        self.filledBlock = "■ "

    def Draw(self):
        for y in range(FIELD_HEIGHT):
            print("<!", end = "")
            for x in range(FIELD_WIDTH):
                if self.fieldList[y][x] == 0:
                    print(self.emptyBlock, end = "")
                if self.fieldList[y][x] == 1:
                    print(self.filledBlock, end = "")
            print("!>")
        print("========================")

class TetriMino():
    def __init__(self):
        self.minoVector = []
        block_type = random.randint(1, 4)

        if block_type == 1:
            self.minoVector = [[-1,0],[0,0],[1,0],[2,0]]

def main():
    fd = FieldDraw()
    fd.Draw()

if __name__ == "__main__":
    main()

#https://daeudaeu.com/tetris/