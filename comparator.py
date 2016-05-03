import time
import random
import os
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

        med_pro1 = 0;
        med_pro2 = 0;

        command = ['', str(n), "vector-" + str(n)]

        for x in range(0, executions):
            # 32-bit range vector(n) random generator
            f = open('vector-' + str(n), 'a')
            for y in range(0, n-1):
                f.write(str(random.randint(-2147473648, 2147473647)) + '\n');

            if(random.choice((True, False))):
                program1, program2 = program2, program1
                med_pro1, med_pro2 = med_pro2, med_pro1

            # Program1
            command[0] = './' + program1
            pre = time.time()
            call(command)
            post = time.time()
            med_pro1 = med_pro1 + (post - pre);
            f = open(program1 + '-' + str(n), 'a')
            f.write(str(post-pre) + "s\n")
            f.close

            # Program2
            command[0] = './' + program2
            pre = time.time()
            call(command)
            post = time.time()
            med_pro2 = med_pro2 + (post - pre);
            f = open(program2 + '-' + str(n), 'a')
            f.write(str(post-pre) + "s\n")
            f.close

            # Remove vector data file
            os.remove('vector-' + str(n))

        # Write total and median program1
        f = open(program1 + '-' + str(n), 'a')
        f.write("\nTotal: " + str(med_pro1) + "s")
        f.write("\nMedian: " + str(med_pro1/executions) + "s\n")
        # Write total and median program2
        f = open(program2 + '-' + str(n), 'a')
        f.write("\nTotal: " + str(med_pro2) + "s")
        f.write("\nMedian: " + str(med_pro2/executions) + "s\n")
