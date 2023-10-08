"""import sys


def filedis(filename):
    a = open(file=filename, mode='rt', encoding='utf-8')
    for line in a:
        sys.stdout.write(line)

    a.close()


if __name__ == "__main__":
    filedis(sys.argv[1])"""

with open(file="app.log", mode='rt', encoding='utf-8') as log:
    maxtime = ['0', '0']
    for index, content in enumerate(log.readlines()):
        if index == 0:
            pass
        else:
            con = list(content.split()[1].split(','))
            if maxtime[0] < con[0]:
                maxtime[0], maxtime[1] = con[0], index

    print(f'Maximum time:{maxtime[0]} Line number:{maxtime[1]}')
