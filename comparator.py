import time
import random
import os
import csv
from subprocess import call
from sys import argv


def usage():
    print("Usage: " + argv[0] + " <Binary1> <Binary2> <n elements> <#executions> <mode = (discrete, continuous)> <steps>")
    print("\tDiscrete will get times for elements of n size.")
    print("\tContinuous will get data from 1 to n vector sizes.")
    print("\t\tSteps in size incrementation (ignored in discrete mode).")

if __name__ == '__main__':
    if len(argv) != 7:
        usage()
    else:
        program1 = argv[1]
        program2 = argv[2]
        n = int(argv[3])
        executions = int(argv[4])

        if argv[5] == "discrete":
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
                    median1, median2 = median2, median1

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
        
        elif argv[5] == "continuous":

            data1 = []
            data2 = []
            steps = int(argv[6])

            z = 0
            while z < n:
                median1 = 0
                median2 = 0

                command = ['', str(n), "vector-" + str(z)]

                for x in range(0, executions):
                    # 32-bit range vector(n) random generator
                    f = open('vector-' + str(z), 'a')
                    for y in range(0, z-1):
                        f.write(str(random.randint(-2147473648, 2147473647)) + '\n');

                    if(random.choice((True, False))):
                        program1, program2 = program2, program1
                        data1, data2 = data2, data1
                        median1, median2 = median2, median1

                    # Program1
                    command[0] = './' + program1
                    pre = time.time()
                    call(command)
                    post = time.time()
                    median1 += post - pre

                    # Program2
                    command[0] = './' + program2
                    pre = time.time()
                    call(command)
                    post = time.time()
                    median2 += post - pre

                    # Remove vector data file
                    os.remove('vector-' + str(z))

                    # Increment in x steps
                    z += steps
                
                median1 /= executions
                median2 /= executions

                data1.append(median1)
                data2.append(median2)

            ofile = open('times-' + str(n) + '.csv', "wb")
            writ = csv.writer(ofile)
            writ.writerow(['#elements', program1[5:], program2[5:]]) # Header
                
            i = 0
            while (i < n/steps): # Writes each execution time for both languages
                writ.writerow([(i+1)*steps, data1[i], data2[i]])
                i += 1
              
            ofile.close()

        print("\nFinished data recollection!\n")
