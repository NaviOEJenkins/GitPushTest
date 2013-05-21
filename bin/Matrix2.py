class Matrix(object):
    """
    A simple matrix
    This matrix is a list of lists
    Column and row numbers start with 1
    """

    def __init__(self, rows, cols):
        """
        Initialize a Matrix object with a number of Columns and rows
        set by the args.

        Zero fill the rows.

        >>> a = Matrix(4,4)
        >>> print a
        Row 1 = [0, 0, 0, 0]
        Row 2 = [0, 0, 0, 0]
        Row 3 = [0, 0, 0, 0]
        Row 4 = [0, 0, 0, 0]
        <BLANKLINE>
        """
        cols = cols
        self.rows = rows
        # initialize matrix and fill with zeroes
        self.matrix = []
        for i in range(rows):
            ea_row = []
            for j in range(cols):
                ea_row.append(0)
            self.matrix.append(ea_row)


    def setitem(self, row, col, v):
        """
        Set the value of the cell at (row, col) to v.

        >>> a = Matrix(4,4)
        >>> print a
        Row 1 = [0, 0, 0, 0]
        Row 2 = [0, 0, 0, 0]
        Row 3 = [0, 0, 0, 0]
        Row 4 = [0, 0, 0, 0]
        <BLANKLINE>

        >>> a.setitem(3,4,'55.75')
        >>> print a
        Row 1 = [0, 0, 0, 0]
        Row 2 = [0, 0, 0, 0]
        Row 3 = [0, 0, 0, '55.75']
        Row 4 = [0, 0, 0, 0]
        <BLANKLINE>
        """
        self.matrix[row-1][col-1] = v


    def getitem(self, row, col):
        """
        Return the value of the cell at (row, col).

        >>> a = Matrix(4,4)
        >>> print a
        Row 1 = [0, 0, 0, 0]
        Row 2 = [0, 0, 0, 0]
        Row 3 = [0, 0, 0, 0]
        Row 4 = [0, 0, 0, 0]
        <BLANKLINE>

        >>> a.setitem(3,4,'55.75')
        >>> print a
        Row 1 = [0, 0, 0, 0]
        Row 2 = [0, 0, 0, 0]
        Row 3 = [0, 0, 0, '55.75']
        Row 4 = [0, 0, 0, 0]
        <BLANKLINE>

        >>> print a.getitem(3,4)
        55.75
        """
        return self.matrix[row-1][col-1]


    def getcolumn(self, row):
        return [self.matrix[row-1][i] for i in range(self.cols)]

    def getcolumn2(self, row):
        return [self.matrix[row-1][i] for i in range(self.cols)]


    def __repr__(self):
        outStr = ""
        for i in range(self.rows):
            outStr += 'Row %s = %s\n' % (i+1, self.matrix[i])
        return outStr


    def __iter__(self):
        for row in range(self.rows):
            for col in range(self.cols):
                yield (self.matrix, row, col)

