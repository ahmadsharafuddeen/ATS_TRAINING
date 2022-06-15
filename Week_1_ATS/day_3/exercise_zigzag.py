import sys, time

indent = 0
increase_indenting = True

try:
    while True:
        print(' ' * indent, end='')
        print('********')
        time.sleep(0.1)

        if increase_indenting: 
            indent = indent + 1
            if indent == 20:
                increase_indenting = False
        else:
            indent = indent - 1 
            if indent == 0:
                increase_indenting = True
except KeyboardInterrupt:
    sys.exit()