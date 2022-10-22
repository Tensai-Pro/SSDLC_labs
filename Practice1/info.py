import psutil

disks = psutil.disk_partitions()
for disk in disks:
    if disk[0] != 'E:\\':
        print("Disk name: ", disk[0], end='\n')
        print("File system type: ", disk[2], end='\n')
        memory = psutil.disk_usage(disk[0])
        print("Total memory: ", round(memory[0] / 1024 ** 3, 2), "GB", end='\n')
        print("Used memory: ", round(memory[1] / 1024 ** 3, 2), "GB", end='\n')
        print("Free memory: ", round(memory[2] / 1024 ** 3, 2), "GB", end='\n')
        print("Percent: ", memory[3], "%", end='\n\n')

