from collections import defaultdict

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: list[list[int]]) -> int:
        # Map row -> bitmask of reserved seats
        # We only care about seats 2 to 9
        occupied = defaultdict(int)
        for row, col in reservedSeats:
            if 2 <= col <= 9:
                occupied[row] |= (1 << (col - 2))
                
        # Define bitmasks for the 3 structural positions
        # left: seats 2,3,4,5 -> bits 0,1,2,3 -> binary 00001111 -> 15
        # right: seats 6,7,8,9 -> bits 4,5,6,7 -> binary 11110000 -> 240
        # middle: seats 4,5,6,7 -> bits 2,3,4,5 -> binary 00111100 -> 60
        LEFT, RIGHT, MIDDLE = 15, 240, 60
        
        # Start by assuming all rows can accommodate 2 families maximum
        max_families = 2 * n
        
        for row, mask in occupied.items():
            # If a row has reservations, it can no longer hold 2 families unless 
            # BOTH left and right are perfectly open (which means mask == 0, impossible here)
            # So it will either hold 1 family or 0 families. We subtract from the max possible.
            left_free = (mask & LEFT) == 0
            right_free = (mask & RIGHT) == 0
            middle_free = (mask & MIDDLE) == 0
            
            if left_free and right_free:
                continue # Holds 2 families (no deduction)
            elif left_free or right_free or middle_free:
                max_families -= 1 # Holds 1 family (deduct 1)
            else:
                max_families -= 2 # Holds 0 families (deduct 2)
                
        return max_families
