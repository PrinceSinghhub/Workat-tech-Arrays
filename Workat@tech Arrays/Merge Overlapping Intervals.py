class Solution:

    def mergeIntervals(self,intervel):

        if len(intervel) == 0:
            return intervel

        intervel.sort()

        merged = []


        start = intervel[0][0]
        end = intervel[0][1]

        for i in intervel:
            if i[0] <= end:
                end = max(end,i[1])
            else:
                merged.append([start,end])
                start = i[0]
                end = i[1]

        merged.append([start,end])
        # for i in range(len(intervel)):



        #     if len(merged) == 0 or merged[-1][1] < intervel[i][0]:
        #
        #         temp = [intervel[i][0],intervel[i][1]]
        #         merged.append(temp)
        #     else:
        #         merged[-1][1] = max(merged[-1][1],intervel[i][1])
        #
        return merged

