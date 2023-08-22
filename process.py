from order import Order, output_csv
from worker import WorkerAllocation
from cal_time import cal_time
import csv

# 创建分配方案实例
allocation_scheme = WorkerAllocation()

# 分配工人
allocation_scheme.assign_workers([14, 13, 9, 4], 0)  # 分配工人到区域1
allocation_scheme.assign_workers([12, 11, 8, 0], 1)  # 分配工人到区域2
allocation_scheme.assign_workers([10, 7, 3], 2)  # 分配工人到区域3
allocation_scheme.assign_workers([5], 3)  # 分配工人到区域4
allocation_scheme.assign_workers([6, 2, 1], 4)  # 分配工人到区域5

flag = 0  # 导入订单0 or 生成订单1


# 导入的订单
def csv_data(o_dir, csv_path):
    global flag
    flag = 1
    with open(csv_path, newline='', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file)
        count = 0
        for row in csv_reader:
            if count > 0:
                new_order = Order([80, 60, 30, 10, 20])
                new_order.read_sections(row)
                order_name = f"order_{(count-1):03}"
                # print(order_name)
                order_dir[order_name] = new_order
            count += 1
    return o_dir


# 自己生成的订单
def gene_data(o_dir):
    order_list = []

    all_order = []  # 订单中数量的合集
    for i in range(0, 1000):
        new_order = Order([80, 60, 30, 10, 20])

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

    return o_dir


if __name__ == '__main__':
    order_dir = {}     # 订单对象的合集
    # order_dir = gene_data(order_dir)
    order_dir = csv_data(order_dir, '第四批订单.csv')
    '''order_list = []

    all_order = []      # 订单中数量的合集
    for i in range(0, 1000):
        new_order = Order([80, 60, 30, 10, 20])

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
        order_dir[order_name] = sorted_list[i]'''

    # 显示分配情况和区域效率
    effi = allocation_scheme.display_allocation()

    # 计算时间
    cal_time(order_dir, effi, flag=flag)

    order_time_list = []
    sum_time_0 = 0
    sum_time_1 = 0
    for i in range(0, len(order_dir)):
        order_time_list.append(order_dir[f'order_{i:03}'].gene_time + order_dir[f'order_{i:03}'].fini_time)
        print(f'order_{i:03} took ', order_dir[f'order_{i:03}'].spent_time, 's')
        sum_time_0 += order_dir[f'order_{i:03}'].spent_time

        sum_time_1 = order_dir[f'order_{i:03}'].fini_time[4] - order_dir[f'order_{0:03}'].fini_time[4]
    output_csv(order_time_list, 'order_time_list.csv')
    print('sum all orders\' time : ', sum_time_0, sum_time_1)
