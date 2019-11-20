import sys
from pathlib import Path
import time
import collections

start_time = time.time()

myindex_path = Path('./myindex.txt')

hash_dict = {}
values = []

# Populate hash with (key,value) pairs from myindex.txt
with open(myindex_path) as ip:
    ip.readline()
    for idx, line in enumerate(ip):
        k, v = tuple(line.split('|'))
        k, v = int(k), int(v)
        values.append(v)
        hash_dict[k] = idx

# Get file path from command line
file_path = Path(sys.argv[1])
idx += 1

# Main loop for insert, delete, and search
with open(file_path) as fp:
    for line in fp:
        new_line = line.strip()
        operation = new_line[:6]
        if operation == 'insert':
            k, v = new_line[7:-1].split(',')
            k, v = int(k), int(v)
            if k in hash_dict:
                values[hash_dict[k]] = v
            else:
                values.append(v)
                hash_dict[k] = idx
                idx += 1
        elif operation == 'delete':
            k = new_line[7:-1]
            k = int(k)
            if k in hash_dict:
                values[hash_dict[k]] = None
                del hash_dict[k]
        elif operation == 'search':
            k = new_line[7:-1]
            k = int(k)
            if k in hash_dict:
                # fr.write('Key: \t{}\tValue: {}\n'.format(k,values[hash_dict[k]]))
                print('Key: \t{}\tValue: {}'.format(k,values[hash_dict[k]]))
            else:
                # fr.write('Key {} not present\n'.format(k))
                print('Key {} not present'.format(k))

# Write timing to file
end_time = time.time()
ft = open("1_rb2540_timing.txt", "w")
ft.write('Hash Time:\t{} seconds\n'.format(end_time - start_time))
ft.close()

# Write hash table to file
fr = open("1_rb2540_hash_resultTable.txt", "w")
fr.write("Hash Table\n\n")
# for item in hash_dict.items():
#     key, idx = item
#     val = values[idx]
#     fr.write('Key: \t{}\tValue: {}\n'.format(key, values[idx]))
for key in sorted(hash_dict.keys()):
    fr.write('Key: \t{}\tValue: {}\n'.format(key, values[hash_dict[key]]))
fr.close()


