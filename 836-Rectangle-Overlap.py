class Solution:
    def isRectangleOverlap(self, rec1: list[int], rec2: list[int]) -> bool:
        return not (
            rec1[2] <= rec2[0] or  # rec1 is to the left of rec2
            rec1[0] >= rec2[2] or  # rec1 is to the right of rec2
            rec1[3] <= rec2[1] or  # rec1 is below rec2
            rec1[1] >= rec2[3]     # rec1 is above rec2
        )