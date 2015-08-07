import os

dir_path = raw_input("\nThis program checks for duplicate files.\nWhat is the directory path you want to check?\n(Eg. /Users/my_username/Downloads)\n> ")

# Performs DSU sort
def sort_by_length(words_list):
	# Creates temp attribute to sort by
	temp = []
	for word in words_list:
		temp.append((len(word), word))
	temp.sort()

	#recreate list after sorting
	res = []
	for length, word in temp:
		res.append(word)
	return res

# Returns md5sum of a file given the file path
def md5_file(file_path):
	cmd = 'md5 '+file_path
	fp_open = os.popen(cmd)
	md5_hash = fp_open.read()[-33:].strip()
	fp_open.close()
	return md5_hash

# Returns a dictionary of hashes with files that has the same hash
def search_duplicate(dir_path):
	cmd = 'cd '+dir_path+ ' && '+'ls'
	dp_open = os.popen(cmd)
	dp_in_dir = dp_open.read().split('\n')
	
	dict_all_md5 = {}

	for filee in dp_in_dir:
		file_path = "'"+dir_path + '/' + filee+"'"

		if os.path.isdir(file_path.replace("'","")):
			pass
			# new_dict = search_duplicate(file_path.replace("'",""))
			# for keys in new_dict:
			# 	dict_all_md5[keys] = dict_all_md5.get(keys,[])+[new_dict[keys]]
		else:
			dict_all_md5[md5_file(file_path)] = dict_all_md5.get(md5_file(file_path),[])+[filee]
	dp_open.close()
	return dict_all_md5

result = search_duplicate(dir_path)

set_to_delete = []

for i in result:
	if len(result[i])>1:
		set_to_delete = set_to_delete + [result[i]]

if set_to_delete == []:
	print "\nNo duplicate files found in " + dir_path + ". Woohoo!\n"
else:
	original_filee = []
	delete_filees = []
	for i in set_to_delete:
		set_sorted = sort_by_length(i)
		original_filee = original_filee + [set_sorted[0]]
		delete_filees = delete_filees + [set_sorted[1:]]
	print "\n"*50
	print "%-50s | %s" %("Keep Original","Delete Duplicates")
	print "-"*100
	for original,delete in zip(original_filee,delete_filees):
		print "%-50s | %s" %(original,delete)
	print