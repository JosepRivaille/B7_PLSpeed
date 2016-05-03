import time
import random
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

        for x in range(0, executions):
            command = ['']
            # 32-bit range vector(n) random generator
            for y in range(0, n-1):
                command.append(str(random.randint(-2147473648, 2147473647)))

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

        # Write median program1
        f = open(program1 + '-' + str(n), 'a')
        f.write("\nMedian: " + str(med_pro1/executions)+ "\n")
        # Write median program2
        f = open(program2 + '-' + str(n), 'a')
        f.write("\nMedian: " + str(med_pro2/executions)+ "\n")
