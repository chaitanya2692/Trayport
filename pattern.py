import sys

def parse_by_line(file_name):
    f = open(file_name, 'r')
    f1 = f.readlines()
    all_lines = []
    for x in f1:
        one_line = list(x)                
        all_lines.append(one_line)
    return all_lines

def match_pattern(bug, char_index,line_index,lines):
    for i,bug_line in enumerate(bug):
        if lines[line_index+i][char_index:char_index+len(bug_line)] == bug_line:
            continue
        else:
            return False
    return True

def check_pattern(bug, lines,line_index):
    count = 0
    for char_index, char in enumerate(lines[line_index]):
        if char == bug[0][0]:
            if match_pattern(bug, char_index,line_index,lines):
                count = count + 1
    return count
        
if __name__ == "__main__":
    bug = parse_by_line(str(sys.argv[1]))
    lines = parse_by_line(str(sys.argv[2]))
    # bug = parse_by_line('bug.txt')
    [x.remove('\n') for x in bug]
    # lines = parse_by_line('landscape_1.txt')
    total_count = 0
    for i in range(len(lines)-len(bug)+1):
        count = check_pattern(bug,lines,i)
        total_count = total_count + count
    print("Total number of bugs =", total_count)