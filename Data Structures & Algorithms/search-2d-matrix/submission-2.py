class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        l = len(matrix)
        h = len(matrix[0])

        left,top =0,0
        right,bottom = h-1,l-1

        while top <= bottom:
            midH = top + (bottom-top)//2

            if target >= matrix[midH][0] and target <= matrix[midH][right]:
                while left<=right:
                    midL = left+(right-left)//2

                    if matrix[midH][midL]==target:
                        return True
                    elif matrix[midH][midL]>target:
                        right = midL-1
                    else:
                        left = midL+1
            elif target < matrix[midH][0]:
                bottom = midH-1
            else:
                top = midH+1
        return False
