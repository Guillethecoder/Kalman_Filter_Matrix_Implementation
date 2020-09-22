import math
from math import sqrt
import numbers

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I
    
def dot_product(vector_one, vector_two):
    result = 0
    
    for i in range(len(vector_one)):
        result += vector_one[i] * vector_two[i]

    return result    

class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################
 
    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
        elif self.h == 1:
            determinant = 1/self.g[0][0]
            return determinant
        else:
            determinant = self.g[0][0]*self.g[1][1] - self.g[0][1]*self.g[1][0]
            return determinant
        
        

    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        sum = 0
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")
        
        else:
            for i in range(self.h):
                for j in range(self.w):
                    if j == i:
                        sum += self.g[i][j]
        return sum

        # TODO - your code here

    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")
        elif self.h == 1:
            inverse = [[1/self.g[0][0]]]
            return Matrix(inverse)
            
        else:
            inv_det = 1/self.determinant()
            inverse = [[inv_det*self.g[1][1], -inv_det*self.g[0][1]], [-inv_det*self.g[1][0], inv_det*self.g[0][0]]]
        # TODO - your code here
            return Matrix(inverse)

    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        # TODO - your code here
        t =[]
        for j in range(self.w):
            row = []
            for i in range(self.h):
                row.append(self.g[i][j])
            t.append(row)
        return Matrix(t)
           
                
            

    def is_square(self):
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]
    
    def get_column(self, column_number):
        column = []
        for r in range(self.h):
            column.append(self.g[r][column_number])

        return column


    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 
        # initialize matrix to hold the results
        matrixSum = []

        # matrix to hold a row for appending sums of each element
        row = []

        # For loop within a for loop to iterate over the matrices
        for r in range(self.h):
            row = [] # reset the list
            for c in range(self.w):
                row.append(self.g[r][c] + other.g[r][c]) # add the matrices
            matrixSum.append(row)

        return Matrix(matrixSum)
        

    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        neg = []
        for i in range(self.h):
            row = []
            for j in range(self.w):
                row.append(-self.g[i][j])
            neg.append(row)
         
        return Matrix(neg)
                

    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be substracted if the dimensions are the same") 
        subs = []
        print(self.g)
        print(other)
        for i in range(self.h):
            subs_row = []
            for j in range(self.w):
                subs_row.append(self.g[i][j] - other.g[i][j])
            subs.append(subs_row)
        print(subs)
        return Matrix(subs)
    

        return column

    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        if self.w != other.h:
            raise RunTimeError("Cannot do this multiplication")
        result = []
        for r in range(self.h):
        
            row_result = []
        # Grab current A row
            rowA = self.g[r]
        
            for c in range(other.w):
                # Grab current B column
                colB = other.get_column(c)
                # Calculate the dot product of the A row and the B column
                dot_prod = dot_product(rowA, colB)
                # And append to row_result
                row_result.append(dot_prod)

            # Add the row_result to the result matrix
            result.append(row_result)

        return Matrix(result)
        
                
        
        

    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        if isinstance(other, numbers.Number):
            res = []
            for i in range(self.h):
                row = []
                for j in range(self.w):
                    row.append(other*self.g[i][j])
                res.append(row)
         
            return Matrix(res)
            #   
            # TODO - your code here
            #
            