class WorkerAllocation:
    def __init__(self, num_workers=15, num_areas=5):
        self.num_workers = num_workers
        self.num_areas = num_areas
        self.worker_efficiencies = [num for num in range(1, num_workers + 1)]  # 定义效率
        self.worker_locations = [0] * num_workers
        self.area_efficiencies = [0] * num_areas  # 初始区域效率为0

    def assign_workers(self, worker_indices, area_index):
        if len(worker_indices) <= self.num_workers:
            for idx in worker_indices:
                self.worker_locations[idx] = area_index + 1
        else:
            print("Not enough available workers for this assignment.")

    def display_allocation(self):
        for num in range(len(self.worker_locations)):
            if self.worker_locations[num] >= 1:
                self.area_efficiencies[self.worker_locations[num] - 1] += num + 1

        print("Worker Locations:", self.worker_locations)
        print("Area Efficiencies:", self.area_efficiencies)

        return self.area_efficiencies
