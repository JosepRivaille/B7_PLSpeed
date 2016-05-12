import time
import random
import os
import csv
from subprocess import call
from sys import argv


def usage():
    print("Usage: " + argv[0] + " <Binary1> <Binary2> <n elements> <#executions>")

if __name__ == '__main__':
    if len(argv) != 5:
        usage()
    else:
        program1 = argv[1]
        program2 = argv[2]
        n = int(argv[3])
        executions = int(argv[4])

        data1 = []
        data2 = []
        median1 = 0
        median2 = 0

        command = ['', str(n), "vector-" + str(n)]

        for x in range(0, executions):
            # 32-bit range vector(n) random generator
            f = open('vector-' + str(n), 'a')
            for y in range(0, n-1):
                f.write(str(random.randint(-2147473648, 2147473647)) + '\n');

            if(random.choice((True, False))):
                program1, program2 = program2, program1
                data1, data2 = data2, data1

            # Program1
            command[0] = './' + program1
            pre = time.time()
            call(command)
            post = time.time()
            data1.append(post - pre)
            median1 += post - pre

            # Program2
            command[0] = './' + program2
            pre = time.time()
            call(command)
            post = time.time()
            data2.append(post - pre)
            median2 += post - pre

            # Remove vector data file
            os.remove('vector-' + str(n))
        
        ofile = open('times-' + str(n) + '.csv', "wb")
        writ = csv.writer(ofile)
        writ.writerow(['#execution', program1, program2]) # Header
		
        i = 0
        while (i < executions): # Writes each execution time for both languages
			writ.writerow([i+1, data1[i], data2[i]])
			i += 1
		
        median1 /= executions
        median2 /= executions
        writ.writerow([]) # Empty line
        writ.writerow(['median:', median1, median2])
		
        ofile.close()
