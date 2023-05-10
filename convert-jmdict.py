import xml.etree.ElementTree as ET
import xmltodict
from json import dumps

# Making compact dumps, with proper handling of re_nokanji
tos = lambda e: dumps(e, separators=(',', ':'), ensure_ascii=False).replace('"re_nokanji":null','"re_nokanji":true')

print('parsing JMdict.xml')
root = ET.parse('JMdict.xml').getroot()
num_ele = len(root)

with open('jmdict.json', 'w') as file:
	for i, ele in enumerate(root):
		if i % 1000 == 0:
			print('jmdict.json %i/%i' % (i+1,num_ele))
		# Forcing certain fields to be list, even if only one element
		entry = xmltodict.parse(ET.tostring(ele), force_list={
			'k_ele',
			'r_ele',
			'sense',
			'ke_inf',
			'ke_pri',
			're_restr',
			're_inf',
			're_pri',
			'stagk',
			'stagr',
			'pos',
			'xref',
			'ant',
			'field',
			'misc',
			's_inf',
			'lsource',
			'dial',
			'gloss'
		})
		file.write(tos(entry)+'\n')
	print('jmdict.json %i/%i' % (num_ele,num_ele))
