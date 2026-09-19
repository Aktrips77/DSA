class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        # Find the closest X coordinate on the rectangle to the circle's center
        closest_x = max(x1, min(x2, xCenter))
        
        # Find the closest Y coordinate on the rectangle to the circle's center
        closest_y = max(y1, min(y2, yCenter))
        
        # Calculate the distance components between the circle's center and the closest point
        dist_x = xCenter - closest_x
        dist_y = yCenter - closest_y
        
        # Check if the squared distance is less than or equal to the squared radius
        return (dist_x * dist_x + dist_y * dist_y) <= (radius * radius)
