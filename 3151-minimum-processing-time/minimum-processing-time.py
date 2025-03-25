class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime = sorted(processorTime,reverse = True)
        tasks = sorted(tasks)
        time_pointer = 0
        arr = []
        for i in range(len(tasks)):
            if i != 0 and (i+1) % 4 == 0:
                arr.append(tasks[i] + processorTime[time_pointer])
                time_pointer += 1
        return max(arr)