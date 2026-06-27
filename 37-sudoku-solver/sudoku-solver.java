class Solution {

    public boolean isSafe(char[][]board, int row, int col,char dig){
        // check row
        for(int j=0;j<9;j++){
            if(board[row][j]==dig)
            return false;
        }
        // check column
        for(int i=0;i<9;i++){
            if(board[i][col]==dig)

            return false;
        } 

        // check 3x3 gird
        int strow=(row/3)*3;

        int stcol =(col/3)*3;
        for( int i =strow; i<=strow +2; i++){
            for(int j=stcol;j<=stcol+2;j++){
                if (board[i][j]==dig){
                    return false;
                }
            }

        }
        return true;
       

    }

    // backtracking function 
    public boolean helper(char[][] board, int row, int col) {
        if (row == 9) {
            return true;
        }

        int nextRow = row;
        int nextCol = col + 1;

        if (nextCol == 9) {
            nextRow = row + 1;
            nextCol = 0;
        }

        if (board[row][col] != '.') {
            return helper(board, nextRow, nextCol);
        }

        
        for (char dig = '1'; dig <= '9'; dig++) {
            if (isSafe(board, row, col, dig)) {
                board[row][col] = dig; 
                
                if (helper(board, nextRow, nextCol)) {
                    return true; 
                }
                
                board[row][col] = '.'; 
            }
        }

        return false;
    }

    public void solveSudoku(char[][] board) {
        
    helper(board, 0, 0);
    }
}