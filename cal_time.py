def relu(number):
    if number >= 0:
        return number
    else:
        return 0


def cal_time(orders, efficiency):
    for i in range(len(orders)):
        # order进入五个分区的时间
        gene_time = [0] * 5
        # order在五个分区拣货所需的时间
        proc_time = [0] * 5
        # order在五个分区需要等待前一个order完成的时间
        wait_time = [0] * 5
        # order在五个分区结束的时间
        fini_time = [0] * 5

        quantity = orders[f'order_{i:03}'].section_sum()
        gene_time[0] = orders[f'order_{i:03}'].time

        if i == 0:  # order_001不需要等待
            for j in range(0, 5):
                proc_time[j] = (quantity[j]/efficiency[j])
                if j > 0:
                    gene_time[j] = fini_time[j - 1]
                fini_time[j] = gene_time[j] + wait_time[j] + proc_time[j]
        elif i >= 1:
            for j in range(0, 5):
                proc_time[j] = (quantity[j]/efficiency[j])
                if j > 0:
                    gene_time[j] = fini_time[j - 1]
                wait_time[j] = relu(orders[f'order_{i-1:03}'].fini_time[j] - gene_time[j])  # wait time大于等于0
                fini_time[j] = gene_time[j] + wait_time[j] + proc_time[j]

        orders[f'order_{i:03}'].set_alltime(gene_time, proc_time, wait_time, fini_time)   # 各个时间信息存入order对象


