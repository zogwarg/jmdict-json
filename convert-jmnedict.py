import xml.etree.ElementTree as ET
import xmltodict
from json import dumps

# Making compact dumps
tos = lambda e: dumps(e, separators=(',', ':'), ensure_ascii=False)

root = ET.parse('JMnedict.xml').getroot()

with open('jmnedict.json', 'w') as file:
	for ele in root:
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
