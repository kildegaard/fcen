def filematch(lines, substr):
    for line in lines:
        if substr in line:
            yield line
