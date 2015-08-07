import urllib
zip_code = raw_input("What is your zip code?")

conn = urllib.urlopen('http://www.uszip.com/zip/'+zip_code)

count_array = []
for line in conn:
	count_array = count_array + [line.strip()]

place_html = ""
for i in range(len(count_array)):
	if count_array[i] == "<!-- place name / title -->":
		place_html= count_array[i+4]
		break
print place_html
print place_html[12:place_html.find(',')+1],
print place_html[place_html.find('state=')+6:place_html.find('state=')+8]