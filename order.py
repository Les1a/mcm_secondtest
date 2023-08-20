import numpy as np
from prettytable import PrettyTable
import random
import csv


class Order:
    def __init__(self, lam_list, flag=1):
        # 初始化订单类
        self.sections = {
            "食品区": [],      # 不同分区的商品将存储在这个字典中，每个分区对应一个空列表
            "饮料区": [],
            "日用品区": [],
            "电器区": [],
            "礼品区": []
        }

        if flag == 0:
            self.init_sections()  # 在初始化时自动填充商品信息
        elif flag == 1:
            self.poisson_sections(lam_list)

        self.time = random.randint(0, 3600*9)

        self.gene_time = [0] * 5
        self.proc_time = [0] * 5
        self.wait_time = [0] * 5
        self.fini_time = [0] * 5

        self.spent_time = 0

    def set_alltime(self, gene_time, proc_time, wait_time, fini_time):
        self.gene_time = gene_time
        self.proc_time = proc_time
        self.wait_time = wait_time
        self.fini_time = fini_time

        self.spent_time = sum(proc_time) + sum(wait_time)

    def section_sum(self):
        sum_list = []
        for _, products in self.sections.items():
            total = 0
            for _, quantity in products:
                total += quantity
            sum_list.append(total)
        return sum_list

    # 随机
    def init_sections(self):
        # 用于填充每个分区的商品信息
        for section in self.sections.keys():
            for shelf in range(0, 10):  # 每个分区有10个货架
                product_name = f"{section} - 货架{shelf}"
                quantity = random.randint(0, 100)  # 随机初始化数量为0-100
                self.sections[section].append((product_name, quantity))

    # 泊松
    def poisson_sections(self, lam_list):
        # 用于填充每个分区的商品信息
        for section in self.sections.keys():
            if section == "食品区":
                lam = lam_list[0]
            elif section == "饮料区":
                lam = lam_list[1]
            elif section == "日用品区":
                lam = lam_list[2]
            elif section == "电器区":
                lam = lam_list[3]
            elif section == "礼品区":
                lam = lam_list[4]
            for shelf in range(0, 10):  # 每个分区有10个货架
                product_name = f"{section} - 货架{shelf}"
                quantity = int(np.random.poisson(lam, 1))
                quantity = int(np.clip(quantity, 0, 100))  # 依据泊松分布初始化数量为0-100
                self.sections[section].append((product_name, quantity))

    def get_order(self):
        order_array = []
        # 打印订单中的商品信息
        s = 0
        for section, products in self.sections.items():
            # print(section)  # 打印分区名称
            s += 1
            n = 0
            for product_name, quantity in products:
                # print(f"{product_name}: {quantity}")  # 打印商品名称和数量
                n += 1
                order_array.append(quantity)

        # 最后一项为订单生成时间
        order_array.append(self.time)
        return order_array

    def print_order_table(self):
        table = PrettyTable()
        table.field_names = ["分区", "商品名称", "数量"]

        for section, products in self.sections.items():
            for product_name, quantity in products:
                table.add_row([section, product_name, quantity])

        table.align = "c"
        print(table)


def output_csv(orders, csv_file_path="historical_orders.csv"):
    print('======> csv starts <======')
    # 将二维列表的每行写入CSV文件
    with open(csv_file_path, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        for row in orders:
            csv_writer.writerow(row)
    print(f'======> {csv_file_path} done! <======')


if __name__ == '__main__':
    '''# 创建一个订单示例
    order = Order()
    print(order.get_order())
    order.print_order_table()  # 打印订单中的商品信息'''
    all_order = []
    for i in range(0, 1000):
        order = Order([80, 60, 40, 10, 20])

        all_order.append(order.get_order())
        print('======>', i, '<======', order.time)

    # 根据order.time的大小顺序排列all_order
    sorted_orders = sorted(all_order, key=lambda order: order[-1])

    output_csv(sorted_orders)
