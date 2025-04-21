def tally_scores(file):
    # open the file
    infile = open(file, 'r')

    # read the lines until the end of the file
    lines = []
    while True:
        line = infile.readline()
        line = line.strip('\n')
        if not line:
            break
        lines.append(line)

    # close the file
    infile.close()

    for line in lines:
        line = line.split()
        name = line[0]
        sum_scores = 0
        for score in line[1:]:
            sum_scores += int(score)
        average = sum_scores / (len(line) - 1)
        print(f"{name}: {' '.join(line[1:])}")
        print(f"average: {average}")
