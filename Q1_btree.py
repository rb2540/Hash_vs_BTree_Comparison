import sys
from pathlib import Path
from BTrees.IOBTree import BTree
import time

start_time = time.time()

myindex_path = Path('./myindex.txt')

tree = BTree()
values = []

# Populate btree with (key,value) pairs from myindex.txt
with open(myindex_path) as ip:
    ip.readline()
    for idx, line in enumerate(ip):
        k, v = tuple(line.split('|'))
        k, v = int(k), int(v)
        values.append(v)
        tree[k] = idx

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
            if k in tree:
                values[tree[k]] = v
            else:
                values.append(v)
                tree[k] = idx
                idx += 1
        elif operation == 'delete':
            k = int(new_line[7:-1])
            if k in tree:
                values[tree[k]] = None
                del tree[k]
        else:
            k = int(new_line[7:-1])
            if k in tree:
                # fr.write('Key: \t{}\tValue: {}\n'.format(k, values[tree[k]]))
                print('Key: \t{}\tValue: {}'.format(k, values[tree[k]]))
            else:
                # fr.write('Key {} not present\n'.format(k))
                print('Key {} not present'.format(k))

# Write timing to file
end_time = time.time()
ft = open("1_rb2540_timing.txt", "a")
ft.write('BTree Time:\t{} seconds \n'.format(end_time - start_time))
ft.close()

# Write btree table to file
fr = open("1_rb2540_btree_resultTable.txt", "w")
fr.write("BTree Table\n\n")
for item in tree.items():
    key, idx = item
    val = values[idx]
    fr.write('Key: \t{}\tValue: {}\n'.format(key, values[idx]))
fr.close()

