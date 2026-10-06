
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0]*numCourses
        courseMap = [[] for i in range(numCourses)]

        for crs,pre in prerequisites:
            courseMap[pre].append(crs)
            indegree[crs]+=1
        
        q = deque()

        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)
        finish=0

        print(courseMap)
        print(indegree)
        while q:
            finish+=1
            cur = q.popleft()

            for nei in courseMap[cur]:
                indegree[nei]-=1
                if indegree[nei]==0:
                    q.append(nei)

        return finish==numCourses

        
            