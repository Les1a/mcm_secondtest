from order import Order, output_csv
from worker import WorkerAllocation
from cal_time import cal_time

# 创建分配方案实例
allocation_scheme = WorkerAllocation()

# 分配工人
allocation_scheme.assign_workers([14, 13, 12, 6], 0)  # 分配工人到区域1
allocation_scheme.assign_workers([7, 9, 10], 1)  # 分配工人到区域2
allocation_scheme.assign_workers([0, 1, 2, 3, 4, 8], 2)  # 分配工人到区域3
allocation_scheme.assign_workers([5], 3)  # 分配工人到区域4
allocation_scheme.assign_workers([11], 4)  # 分配工人到区域5


if __name__ == '__main__':
    order_dir = {}     # 订单对象的合集
    order_list = []

    all_order = []      # 订单中数量的合集
    for i in range(0, 1000):
        # order_name = f"order_{i:03}"
        # print(order_name)
        new_order = Order([80, 60, 30, 10, 20])
        # order_dir[order_name] = new_order
        order_list.append(new_order)
        all_order.append(new_order.get_order())

    # 根据最后一项的大小顺序排列all_order
    sorted_orders = sorted(all_order, key=lambda order: order[-1])
    output_csv(sorted_orders, 'present_orders.csv')

    # 根据self.time的大小顺序排列order_list 并按时间顺序命名存入字典库
    sorted_list = sorted(order_list, key=lambda order: order.time)
    for i in range(len(sorted_list)):
        order_name = f"order_{i:03}"
        # print(order_name)
        order_dir[order_name] = sorted_list[i]

    # 显示分配情况和区域效率
    effi = allocation_scheme.display_allocation()

    # 计算时间
    cal_time(order_dir, effi)

    order_time_list = []
    for i in range(0, 1000):
        order_time_list.append(order_dir[f'order_{i:03}'].gene_time + order_dir[f'order_{i:03}'].fini_time)
        print(f'order_{i:03} took ', order_dir[f'order_{i:03}'].spent_time, 's')
    output_csv(order_time_list, 'order_time_list.csv')
