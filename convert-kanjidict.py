import xml.etree.ElementTree as ET
import xmltodict
from json import dumps

# Making compact dumps, with proper handling of re_nokanji
# tos = lambda e: dumps(e, separators=(',', ':'), ensure_ascii=False).replace('"re_nokanji":null','"re_nokanji":true')

print('parsing kanjidic2.xml')
root = ET.parse('kanjidic2.xml').getroot()
num_ele = len(root)

with open('kanjidict.json', 'w') as file:
	for i, ele in enumerate(root):
		if i == 0:
			continue
		if i % 1000 == 0:
			print('kanjidict.json %i/%i' % (i+1,num_ele))
		# Forcing certain fields to be list, even if only one element
		entry = xmltodict.parse(ET.tostring(ele), force_list={
			'cp_value',
			'dic_ref',
			'rad_name',
			'stroke_count',
			'variant',
			'q_code',
			'rad_value',
			'nanori',
			'meaning',
			'reading'
		})
		file.write(dumps(entry)+'\n')
	print('kanjidict.json %i/%i' % (num_ele,num_ele))
