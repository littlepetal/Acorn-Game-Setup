from cells import (
    Start,
    End,
    Air,
    Wall,
    Fire,
    Water,
    Teleport
)

x = Start()
y = End()
air = Air()
wall = Wall()
fire = Fire()
water = Water()


def read_lines(filename):
    """Read in a file, process them using parse(),
    and return the contents as a list of list of cells."""
    f = open(filename, "r")

    raw = f.readlines()
    grid = parse(raw)

    return grid


def parse(lines):
    """Transform the input into a grid.

    Arguments:
        lines -- list of strings representing the grid

    Returns:
        list -- contains list of lists of Cells
    """
    x_count = 0
    y_count = 0
    tele_pads = []
    
    i = 0 
    while i < len(lines):
        j = 0
        while j < len(lines[i]):
            if lines[i][j] == x.display:
                x_count += 1
            elif lines[i][j] == y.display:
                y_count += 1
            elif lines[i][j].isnumeric() and int(lines[i][j]) >= 1 and int(lines[i][j]) <= 9:
                tele_pads.append(int(lines[i][j]))
            elif lines[i][j] != air.display and lines[i][j] != wall.display and lines[i][j] != fire.display and lines[i][j] != water.display and lines[i][j] != "\n":
                raise ValueError("Bad letter in configuration file: {}.".format(lines[i][j]))
                
            j += 1
        i += 1
        
    if x_count != 1:
        raise ValueError("Expected 1 starting position, got {}.".format(x_count))
    if y_count != 1:
        raise ValueError("Expected 1 ending position, got {}.".format(y_count))
    
    deep_copy_tele_pads = tele_pads.copy()
    
    #Check if there are non matching teleport pads as recorded in tele_pads list    
    if len(tele_pads) == 1:
        raise ValueError("Teleport pad {} does not have an exclusively matching pad.".format(tele_pads[0]))
    else:
        i = 0
        while i < len(tele_pads):
            if tele_pads[i] == -1:
                i += 1
                continue
                
            pad_count = 1
            
            j = 0
            while j < len(tele_pads):
                if tele_pads[i] == tele_pads[j] and i != j:
                    pad_count += 1
                    tele_pads[j] = -1
                j += 1
            
            if pad_count%2 != 0:
                raise ValueError("Teleport pad {} does not have an exclusively matching pad.".format(tele_pads[i]))
            
            tele_pads[i] = -1
            
            i += 1

            
    ls = []
    
    i = 0
    while i < len(lines):
        
        processed = []
        j = 0
        while j < len(lines[i]):
            if lines[i][j] == x.display:
                processed.append(x)
            elif lines[i][j] == y.display:
                processed.append(y)  
            elif lines[i][j].isnumeric():
                processed.append(Teleport(int(lines[i][j])))
            elif lines[i][j] == air.display:
                processed.append(air)
            elif lines[i][j] == wall.display:
                processed.append(wall)
            elif lines[i][j] == fire.display:
                processed.append(fire)
            elif lines[i][j] == water.display:
                processed.append(water)
            elif lines[i][j] == "\n":
                j += 1
                continue
            
            j += 1
            
        ls.append(processed)
        i += 1
    
    return ls
    
    
