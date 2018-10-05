import re
import argparse
import sys


def output(line):
    print(line)

def print_context(left_position, right_position, params, strings_all, strings_selected):
	while (left_position<=right_position):
		if (params.line_number==True):
			flag=1
			for  key in strings_selected.keys():
				if left_position==key:
					s=str(left_position)+":"+strings_all[left_position]
					flag=0
				else:
					s=str(left_position)+"-"+strings_all[left_position]
				if flag==0:
					break
			output(s)
		else:
			output(strings_all[left_position])
		left_position+=1

def check_right_position (key, context_after, strings_all):
	if (key + context_after <= len(strings_all)):
		right_position = key + context_after
	else:
		right_position = len(strings_all)
	return right_position

def check_left_position (key, context_before):
	if (key - context_before > 0):
		left_position = key - context_before
	else:
		left_position = 1
	return left_position

def grep(lines, params):
	a = []
	context=[]
	i = 1
	strings_selected = {}
	strings_all = {}
	regexp = params.pattern
	regexp = regexp.replace('?', '.')
	regexp = regexp.replace('*', '.*')
	for line in lines:
		line = line.rstrip()
		strings_selected[i] = line
		i+= 1
	strings_all=dict(strings_selected)
	for key, value in strings_selected.items():
		if (bool(re.search(regexp, value, re.I if params.ignore_case else 0))!=(params.invert == False)):
			a.append(key)
	for i in range(len(a)):
		del strings_selected[a[i]]
	if params.count == True:
	       	output(str(len(strings_selected)))
	elif (params.line_number==True and  params.before_context==0 and params.context==0 and params.after_context==0):
		for key, value in strings_selected.items():
			s=str(key)+":"+value
			output(s)
	elif (params.before_context!=0 or params.context!=0 or params.after_context!=0):
		context_before=max(params.before_context,params.context)
		context_after=max(params.after_context,params.context)
		left_position=1
		right_position=1
		n=0
		for key, value in strings_selected.items():
			previous_right_position=right_position
			previous_left_position=left_position
			if (key<=right_position+1 and left_position !=0 and right_position!=0):
				right_position = check_right_position(key, context_after, strings_all)
				n+=1
			else:
				left_position=check_left_position(key, context_before)
				right_position=check_right_position(key, context_after, strings_all)
				n+=1
			if (n>1):
				if (left_position!=previous_left_position):
					print_context(previous_left_position, previous_right_position, params, strings_all, strings_selected)
		print_context(left_position, right_position, params, strings_all, strings_selected)
	else:
		for value in strings_selected.values():
			output(value)

def parse_args(args):
    parser = argparse.ArgumentParser(description='This is a simple grep on python')
    parser.add_argument(
        '-v', action="store_true", dest="invert", default=False, help='Selected lines are those not matching pattern.')
    parser.add_argument(
        '-i', action="store_true", dest="ignore_case", default=False, help='Perform case insensitive matching.')
    parser.add_argument(
        '-c',
        action="store_true",
        dest="count",
        default=False,
        help='Only a count of selected lines is written to standard output.')
    parser.add_argument(
        '-n',
        action="store_true",
        dest="line_number",
        default=False,
        help='Each output line is preceded by its relative line number in the file, starting at line 1.')
    parser.add_argument(
        '-C',
        action="store",
        dest="context",
        type=int,
        default=0,
        help='Print num lines of leading and trailing context surrounding each match.')
    parser.add_argument(
        '-B',
        action="store",
        dest="before_context",
        type=int,
        default=0,
        help='Print num lines of trailing context after each match')
    parser.add_argument(
        '-A',
        action="store",
        dest="after_context",
        type=int,
        default=0,
        help='Print num lines of leading context before each match.')
    parser.add_argument('pattern', action="store", help='Search pattern. Can contain magic symbols: ?*')
    return parser.parse_args(args)


def main():
    params = parse_args(sys.argv[1:])
    grep(sys.stdin.readlines(), params)


if __name__ == '__main__':
    main()
