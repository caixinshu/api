# -*- coding: utf-8 -*
import os
for dirpath,filenames in os.walk('e:/'):
	for filename in filenames:
		print os.path.join(dirpath,filename)


