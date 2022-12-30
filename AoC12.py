class Cell:

    def __init__(self,i,j):
        self.i, self.j = i, j
        self.walls = {'N': True, 'S': True, 'E': True, 'W': True}

class Maze:
    
    def __init__(self,ni,nj,si,sj,ei,ej):        
        self.ni, self.nj = ni, nj #ni, nj = no. of rows and columns
        self.si, self.sj = si, sj #si, sj = start cell coordinates
        self.ei, self.ej = ei, ej #ei, ej = end cell coordinates
        self.maze_map = [[Cell(i, j) for j in range(nj)] for i in range(ni)]

    def remove_wall(self, wall, i, j):
            self.maze_map[i][j].walls[wall] = False
    
    def get_height(self,value):
        if i != 0:
            if value == 'S':
                height = ord('a') - ord('a')
            elif value == 'E':
                height = ord('z') - ord('a')
            else:
                height = ord(value) - ord('a')
        return height

    def make_maze(self, topo_map):
        cell_stack = []
                
        for i in range(len(topo_map)):
            for j in range(len(topo_map[0])):
                
                current_cell = self.maze_map[i][j]
                current_height = self.get_height(topo_map[i][j])

                #north
                if i != 0:
                    north_height = self.get_height(topo_map[i-1][j])                        
                    if current_height >= north_height - 1:
                        self.remove_wall('N',i,j)

                #south
                if i < len(topo_map) - 1:
                    south_height = self.get_height(topo_map[i+1][j])        
                    if current_height >= south_height - 1:
                        self.remove_wall('S',i,j)

                #west
                if j != 0:
                    west_height = self.get_height(topo_map[i][j-1])        
                    if current_height >= west_height - 1:
                        self.remove_wall('W',i,j)

                #east
                if  j < len(topo_map[0]) - 1:
                    east_height = self.get_height(topo_map[i][j+1])    
                    if current_height >= east_height - 1:
                        self.remove_wall('E',i,j)

                cell_stack.append(current_cell)

def navigate_maze_from_S_to_E(maze, si, sj, ei, ej):
    def take_step(maze,i,j):
        #take a step from the current cell to all directions if possible
        next_steps = []
        if not maze.maze_map[i][j].walls['N']:
            next_steps = next_steps + [[i-1,j]]
        if not maze.maze_map[i][j].walls['S']:
            next_steps = next_steps + [[i+1,j]]
        if not maze.maze_map[i][j].walls['E']:
            next_steps = next_steps + [[i,j+1]]
        if not maze.maze_map[i][j].walls['W']:
            next_steps = next_steps + [[i,j-1]]
        return next_steps

    steps = 0
    visited_cells = []
    current_cells = [[si,sj]]

    while [ei,ej] not in visited_cells:
        steps = steps + 1

        # add current cells to the visited cells list if they're not there already
        for cell in current_cells:
            if cell not in visited_cells:
                visited_cells = visited_cells + [cell]

        # take a step from each current cell
        all_new_cells = []
        for current_cell in current_cells:
            new_cells = take_step(maze,current_cell[0], current_cell[1])

            # concatenate new cells and omit dublicates
            for new_cell in new_cells:
                if new_cell not in all_new_cells:
                    all_new_cells = all_new_cells + [new_cell]

        current_cells = all_new_cells

    return steps-1

def navigate_maze_from_E_to_a(maze, topo_map, ei, ej):
    def take_revese_step(maze,i,j):
        #check from which cells it is possible to take a step to the current cell
        next_steps = []
        try:
            if not maze.maze_map[i-1][j].walls['S']:
                next_steps = next_steps + [[i-1,j]]
        except:
            pass
        try:
            if not maze.maze_map[i+1][j].walls['N']:
                next_steps = next_steps + [[i+1,j]]
        except:
            pass
        try:
            if not maze.maze_map[i][j+1].walls['W']:
                next_steps = next_steps + [[i,j+1]]
        except:
            pass
        try:
            if not maze.maze_map[i][j-1].walls['E']:
                next_steps = next_steps + [[i,j-1]]
        except:
            pass
        return next_steps

    steps = 0
    visited_cells = []
    current_cells = [[ei,ej]]
    a_reached = False

    while not a_reached:
        steps = steps + 1

        # add current cells to the visited cells list if they're not there already
        for cell in current_cells:
            if cell not in visited_cells:
                visited_cells = visited_cells + [cell]
        
        # take a reverse step from neigbouring cells to the current cells
        all_new_cells = []
        for current_cell in current_cells:
            new_cells = take_revese_step(maze,current_cell[0], current_cell[1])

            # concatenate new cells and omit dublicates
            for new_cell in new_cells:
                if new_cell not in all_new_cells:
                    all_new_cells = all_new_cells + [new_cell]

        current_cells = all_new_cells

        #check if 'a' is reached
        for current_cell in current_cells:
            if topo_map[current_cell[0]][current_cell[1]] == 'a':
                a_reached = True

    return steps

input = open('.\\Desktop\\AoC\\AoC12\\input.txt','r').read().splitlines()

for i in range(len(input)):
    for j in range(len(input[0])):
        if input[i][j] == 'S':
            si, sj = i, j #start cell coordinates
        if input[i][j] == 'E':
            ei, ej = i, j #end cell coordinates

maze = Maze(len(input),len(input[0]),si,sj,ei,ej)        
maze.make_maze(input)

print('steps from S to E:',navigate_maze_from_S_to_E(maze,si,sj,ei,ej))
print('Steps from E to the nearest a:',navigate_maze_from_E_to_a(maze,input,ei,ej))