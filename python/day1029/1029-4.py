# 하노이탑 알고리즘
def move(disk, src, tar, tmp):
    if disk == 1:
        print('Move Disk:', disk, 'from', src, 'to', tar)
    else:
        move(disk-1, src, tmp, tar)
        print('Move Disk:', disk, 'from', src, 'to', tar)
        move(disk-1, tmp, tar, src)

print(move(3,'A','B','C'))

