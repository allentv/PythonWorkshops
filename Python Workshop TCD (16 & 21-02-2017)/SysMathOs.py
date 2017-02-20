"""
Examples of using Math, Sys & OS packages
"""
import math
import sys
import os


def process_sys_args(args):
	print('Args: '				, args[1:])
	print('Python Version: '	, sys.version)
	print('Platform: '			, sys.platform)
	print('Recursion limit: '	, sys.getrecursionlimit())
	print('System PATH:\n'		, sys.path)


def process_os():
	print('\n******* ls *******\n')
	os.system('ls -lAh')
	print('\n******************\n')

	print('Current Working Directory => ', os.getcwd())
	print('OS Details => ', os.uname())

def process_math():
	print('PI 			: ', math.pi)
	print('Log 1024 (base 2)	: ', math.log(1024, 2))
	print('5!			: ', math.factorial(5))
	print('Exp(x)			: ', math.exp(1))
	print('Power			: ', math.pow(5, 2))
	print('Square Root		: ', math.sqrt(25))


if __name__ == '__main__':
	process_sys_args(sys.argv)
	print('\n')
	process_os()
	print('\n')
	process_math()
