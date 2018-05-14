
import csv
import time
import datetime
from matplotlib import pyplot 

batch_number = 7
global_cpu_usage_file_pattern = 'somewhere/global/batch{0}/log_global_cpu_usage'

with open(global_cpu_usage_file_pattern.format(batch_number)) as csvfile:
    reader = csv.reader(csvfile, delimiter='\t')
    first_time = None

    times = []
    cpus = []

    for row in reader:
        time_str = row[0]
        cpu = row[1]

        time_time = datetime.datetime.strptime(time_str, "%H:%M:%S")

        if not first_time:
            first_time = time_time

        time_from_beginning = (time_time-first_time).total_seconds()

        times.append(time_from_beginning)
        cpus.append(cpu)

    pyplot.title("Batch #{0}".format(batch_number))
    pyplot.xlabel("Time (s)")
    pyplot.ylabel("CPU (%)")
    pyplot.plot(times, cpus)
    pyplot.show()
