import xml.etree.ElementTree as ET
import xmltodict
from json import dumps

# Making compact dumps, with proper handling of re_nokanji
tos = lambda e: dumps(e, separators=(',', ':'), ensure_ascii=False).replace('"re_nokanji":null','"re_nokanji":true')

root = ET.parse('JMdict.xml').getroot()

with open('jmdict.json', 'w') as file:
	for ele in root:
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
