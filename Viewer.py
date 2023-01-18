class Viewer:
        
    def PrintBlock(self):
        for y in range(20):
            print("<!", end ="")
            for x in range(10):
                if self.field[y][x] == 0:
                    print("□ ", end ="")
            print("!>")
        print("========================")

    def setField(self, field):
        self.field = field