#
# board.py (Final project)
#
# A Board class for the Eight Puzzle
#
# name: Cheyenne Mowatt
# email: cmowatt@bu.edu
#
# If you worked with a partner, put their contact info below:
# partner's name: 
# partner's email:
#

# a 2-D list that corresponds to the tiles in the goal state
GOAL_TILES = [['0', '1', '2'],
              ['3', '4', '5'],
              ['6', '7', '8']]

class Board:
    """ A class for objects that represent an Eight Puzzle board.
    """
    def __init__(self, digitstr):
        """ a constructor for a Board object whose configuration
            is specified by the input digitstr
            input: digitstr is a permutation of the digits 0-9
        """
        # check that digitstr is 9-character string
        # containing all digits from 0-9
        assert(len(digitstr) == 9)
        for x in range(9):
            assert(str(x) in digitstr)

        self.tiles = [[''] * 3 for x in range(3)]
        self.blank_r = -1
        self.blank_c = -1

        # Put your code for the rest of __init__ below.
        # Do *NOT* remove our code above.
        
        # for r in range(len(digitstr)):
        #     self.tiles[r][c] = digitstr[0] :
        # if self.tiles[r] != 0 :
            
        p = -1   
        for row in range(3):
            for col in range(3):
                p +=1
                self.tiles[row][col] = digitstr[p]
                if self.tiles[row][col] == '0':
                    self.blank_r = row
                    self.blank_c = col
                
    ### Add your other method definitions below. ###
    def __repr__(self):
        """ 
        returns a string representation of a Board object.
        """
        
        s = ''
        for row in range(3):
            for col in range(3):
                if self.tiles[row][col] != '0':
                    s += self.tiles[row][col] + ' '
                else:
                    s+= '_ '

            s += '\n'  # newline at the end of the row
        return s
    def move_blank(self, direction):
        """
        takes as input a string direction that specifies the direction in which the blank should move, and that attempts to modify the contents of the called Board object accordingly.
        """
        if direction == 'up':
            if self.blank_r > 0 :

                x = self.tiles[self.blank_r - 1][self.blank_c] 
                y = self.tiles[self.blank_r][self.blank_c]
                self.tiles[self.blank_r][self.blank_c] = x
                self.tiles[self.blank_r - 1][self.blank_c] = y
                self.blank_r -=1
                return True
        elif direction == 'down':
            if self.blank_r < 2 :

                x = self.tiles[self.blank_r +1][self.blank_c]
                y = self.tiles[self.blank_r][self.blank_c]
                self.tiles[self.blank_r][self.blank_c] = x
                self.tiles[self.blank_r + 1][self.blank_c] = y
                self.blank_r +=1
                return True
        elif direction == 'left':
            if self.blank_c > 0 :
    
                x = self.tiles[self.blank_r][self.blank_c -1]
                y = self.tiles[self.blank_r][self.blank_c]
                self.tiles[self.blank_r][self.blank_c] = x
                self.tiles[self.blank_r][self.blank_c -1] = y
                self.blank_c -=1
                return True
        elif direction == 'right':
            if self.blank_c < 2 :

                x = self.tiles[self.blank_r][self.blank_c +1]
                y = self.tiles[self.blank_r][self.blank_c]
                self.tiles[self.blank_r][self.blank_c] = x
                self.tiles[self.blank_r][self.blank_c +1] = y
                self.blank_c +=1
                return True
        return False
        
    def digit_string(self):
        """ 
        creates and returns a string of digits that corresponds to the current contents of the called Board object’s tiles attribute.
        """
        s = ''
        for r in range(3):
            for c in range(3):
                s += self.tiles[r][c]
        
        return s
    def copy(self):
        """
        returns a newly-constructed Board object that is a deep copy of the called object
        """
        new = Board(self.digit_string())
        
        return new
    
    def num_misplaced(self):
        """
        counts and returns the number of tiles in the called Board object that are not where they should be in the goal state.
        """
        count = 0
        for row in range(3):
            for col in range(3):
                if self.tiles[row][col] != '0':
                    if self.tiles[row][col] != GOAL_TILES[row][col]:
                        count +=1
        return count
    def __eq__(self, other):
        """
        called when the == operator is used to compare two Board objects.return True if the called object (self) and the argument (other) have the same values for the tiles attribute, and False otherwise
        """
        if self.digit_string() == other.digit_string():
            return True
        return False
    
    def wrong_tiles(self):
        """
        adds the number of tiles in the wrong row and the number of tiles in the wrong column
        """
        wrong_row = 0 
        wrong_col = 0
        
        for row in range(3):
            for col in range(3):
                if self.tiles[row][col] != '0':
                    if int(self.tiles[row][col]) // 3 != row:
                        wrong_row +=1
        for row in range(3):
            for col in range(3):
                if self.tiles[row][col] != '0':
                    if int(self.tiles[row][col]) % 3 != col:
                        wrong_col +=1
                        
        return wrong_row + wrong_col
    

        
        
        