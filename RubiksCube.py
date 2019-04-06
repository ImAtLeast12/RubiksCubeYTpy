class Cube:
    def __init__(self):
        self.cube = {
            'U': [1,2,3,4,5,6,7,8,9,],
            'L': [10,11,12,13,14,15,16,17,18,],
            'F': [19,20,21,22,23,24,25,26,27,],
            'D': [28,29,30,31,32,33,34,35,36,],
            'R': [37,38,39,40,41,42,43,44,45,],    
            'B': [46,47,48,59,50,51,52,53,54,], 
        }
    #   U
    #L  F   R   B
    #   D
    def printCube(self):
        a = """
                      [%s][%s][%s]
                      [%s][%s][%s]
                      [%s][%s][%s]
                   
            [%s][%s][%s] [%s][%s][%s] [%s][%s][%s] [%s][%s][%s]
            [%s][%s][%s] [%s][%s][%s] [%s][%s][%s] [%s][%s][%s]
            [%s][%s][%s] [%s][%s][%s] [%s][%s][%s] [%s][%s][%s]
            
                      [%s][%s][%s]
                      [%s][%s][%s]
                      [%s][%s][%s]
        """ % (self.tupGen())
        print(a)

    def tupGen(self):
        x = ()
        y = ()
        z = ()
        
        for i in range(9):
            x += (self.cube.get('U')[i],)
            z += (self.cube.get('D')[i],)

        for j in range(3):

            for i in range(3): 
                y += (self.cube.get('L')[j*3+i],)

            for i in range(3): 
                y += (self.cube.get('F')[j*3+i],)

            for i in range(3): 
                y += (self.cube.get('R')[j*3+i],)

            for i in range(3): 
                y += (self.cube.get('B')[j*3+i],)

            
        return x + y + z

    def moveUP(self):
        tempx = self.cube.get('U')[2]
        tempy = self.cube.get('U')[5]
        tempz = self.cube.get('U')[8]
        
        self.cube.get('U')[2] = self.cube.get('F')[2]
        self.cube.get('U')[5] = self.cube.get('F')[5]
        self.cube.get('U')[8] = self.cube.get('F')[8]

        self.cube.get('F')[2] = self.cube.get('D')[2]
        self.cube.get('F')[5] = self.cube.get('D')[5]
        self.cube.get('F')[8] = self.cube.get('D')[8]

        self.cube.get('D')[2] = self.cube.get('B')[6]
        self.cube.get('D')[5] = self.cube.get('B')[3]
        self.cube.get('D')[8] = self.cube.get('B')[0]

        self.cube.get('B')[6] = tempx
        self.cube.get('B')[3] = tempy
        self.cube.get('B')[0] = tempz
        
        
        
    
a = Cube()
a.printCube()
a.moveUP()
a.printCube()

