import os
#statvfs
def get_size(start_path = '/home/nikola/py/week2'):
	total_size = 0
	for dirpath, dirnames, filenames in os.walk(start_path):
		for f in filenames:
			fp = os.path.join(dirpath, f)
			total_size += os.path.getsize(fp)
	print('Drictory size: {:,} bytes'.format(total_size).replace(',', ' '))
	print('Drictory size: {:,} KB'.format(int(total_size/1024)).replace(',', ' '))
	print('Drictory size: {:,} MB'.format(int(total_size/1024**2)).replace(',', ' '))
	print('Drictory size: {:,} GB'.format(int(total_size/1024**3)).replace(',', ' '))
	print('Drictory size: {:,} TB'.format(int(total_size/1024**4)).replace(',', ' '))
	return total_size

print (get_size())
