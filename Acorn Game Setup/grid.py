def grid_to_string(grid, player):
    """Turns a grid and player into a string

    Arguments:
        grid -- list of list of Cells
        player -- a Player with water buckets

    Returns:
        string: A string representation of the grid and player.
    """
    
    grid_str = ""
    i = 0
    while i < len(grid):
        j = 0
        while j < len(grid[i]):
            if i == player.row and j == player.col:
                grid_str += player.display
            else:
                grid_str += grid[i][j].display
                
            if j == (len(grid[i]) - 1):
                grid_str += "\n"
                
            j += 1
        i += 1
        
        
    if player.num_water_buckets == 1:
        water_str = "You have {} water bucket.".format(player.num_water_buckets)
    else:
        water_str = "You have {} water buckets.".format(player.num_water_buckets)
    
    
    final_str = grid_str + "\n" + water_str
    
    return final_str
