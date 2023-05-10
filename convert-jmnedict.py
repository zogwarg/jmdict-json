import xml.etree.ElementTree as ET
import xmltodict
from json import dumps

# Making compact dumps
tos = lambda e: dumps(e, separators=(',', ':'), ensure_ascii=False)

print('parsing JMnedict.xml')
root = ET.parse('JMnedict.xml').getroot()
num_ele = len(root)

with open('jmnedict.json', 'w') as file:
	for i, ele in enumerate(root):
		if i % 1000 == 0:
			print('jmnedict.json %i/%i' % (i+1,num_ele))
		# Forcing certain fields to be list, even if only one element
		entry = xmltodict.parse(ET.tostring(ele), force_list={
			'k_ele',
			'r_ele',
			'trans',
			'ke_inf',
			'ke_pri',
			're_restr',
			're_inf',
			're_pri',
			'name_type',
			'xref',
			'trans_det',
		})
		file.write(tos(entry)+'\n')
	print('jmnedict.json %i/%i' % (num_ele,num_ele))
