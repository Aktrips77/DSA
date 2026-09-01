import java.util.*;

class Solution {
    public int minMoves(String[] classroom, int energy) {
        int m = classroom.length;
        int n = classroom[0].length();
        
        int startR = -1, startC = -1;
        List<int[]> litterPositions = new ArrayList<>();
        
        // 1. Locate start position and index all litter locations
        for (int r = 0; r < m; r++) {
            String rowStr = classroom[r];
            for (int c = 0; c < n; c++) {
                char ch = rowStr.charAt(c);
                if (ch == 'S') {
                    startR = r;
                    startC = c;
                } else if (ch == 'L') {
                    litterPositions.add(new int[]{r, c});
                }
            }
        }
        
        int totalLitter = litterPositions.size();
        int targetMask = (1 << totalLitter) - 1;
        
        // Fast-lookup mapping for litter indices
        int[][] litterMap = new int[m][n];
        for (int r = 0; r < m; r++) {
            Arrays.fill(litterMap[r], -1);
        }
        for (int i = 0; i < totalLitter; i++) {
            int[] pos = litterPositions.get(i);
            litterMap[pos[0]][pos[1]] = i;
        }
        
        // 2. BFS State tracking: [row, col, current_energy, litter_bitmask]
        Queue<int[]> queue = new LinkedList<>();
        queue.offer(new int[]{startR, startC, energy, 0});
        
        // Visited state caching: visited[row][col][remaining_energy][litter_mask]
        boolean[][][][] visited = new boolean[m][n][energy + 1][1 << totalLitter];
        visited[startR][startC][energy][0] = true;
        
        int[][] directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        int moves = 0;
        
        // 3. Begin Layer-by-Layer Scan
        while (!queue.isEmpty()) {
            int size = queue.size();
            for (int s = 0; s < size; s++) {
                int[] curr = queue.poll();
                int r = curr[0];
                int c = curr[1];
                int e = curr[2];
                int mask = curr[3];
                
                // Winning Condition met
                if (mask == targetMask) {
                    return moves;
                }
                
                // If out of energy, no further transition can be initiated from this cell
                if (e == 0) {
                    continue;
                }
                
                for (int[] dir : directions) {
                    int nr = r + dir[0];
                    int nc = c + dir[1];
                    
                    if (nr >= 0 && nr < m && nc >= 0 && nc < n) {
                        char cellType = classroom[nr].charAt(nc);
                        if (cellType == 'X') {
                            continue; // Obstructed obstacle cell
                        }
                        
                        int nextEnergy = e - 1;
                        int nextMask = mask;
                        
                        // Collect Litter check
                        if (cellType == 'L') {
                            int litterIdx = litterMap[nr][nc];
                            if (litterIdx != -1) {
                                nextMask |= (1 << litterIdx);
                            }
                        }
                        
                        // Handle Station Recharge Capacity
                        if (cellType == 'R') {
                            nextEnergy = energy;
                        }
                        
                        // Offer state if completely unique parameter path
                        if (!visited[nr][nc][nextEnergy][nextMask]) {
                            visited[nr][nc][nextEnergy][nextMask] = true;
                            queue.offer(new int[]{nr, nc, nextEnergy, nextMask});
                        }
                    }
                }
            }
            moves++;
        }
        
        return -1;
    }
}
