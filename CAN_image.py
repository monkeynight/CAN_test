import numpy as np
import time
# 读取文件内容到numpy数组
data = np.loadtxt('DoS_data.txt', dtype=str)
def convert_to_binary(hex_str, length):
    return format(int(hex_str, 16), f'0{length}b')
while(1):
    start_time = time.time()
# 将每行的二进制字符串合并为一个完整的字符串
    converted_data = [
        ''.join([convert_to_binary(row[0], 12)] + [convert_to_binary(cell, 8) for cell in row[1:]])
        for row in data
    ]

    int_data = np.array([list(map(int, list(line))) for line in converted_data])
    merged_data = []
    for i in range(0, len(int_data), 35):
        block = int_data[i:i+35].flatten()
        if len(block) < 35 * int_data.shape[1]:
            block = np.pad(block, (0, 35 * int_data.shape[1] - len(block)), 'constant')
        merged_data.append(block)
    merged_data = np.array(merged_data)
    end_time = time.time()
    print("CAN image:",(end_time - start_time  )/35)