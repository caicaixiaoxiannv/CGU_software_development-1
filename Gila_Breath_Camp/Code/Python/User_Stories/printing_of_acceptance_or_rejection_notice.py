# ===============================================================================
#                             GILA BREATH CAMP
#
# ===============================================================================
# ===============================================================================
# FILE NAME      : printing_of_acceptance_or_rejection_notice.py
# PURPOSE        : printing of notice
# AUTHOR         : Jemin Gohil
# CREATION DATE  : 1-Nov-2016
# PENDING 		 : 
# -------------------------------------------------------------------------------
# CHANGE HISTORY :
# VER	|	DATE       	|	MODIFIED BY  		|  	CHANGE DESCRIPTION
# -------------------------------------------------------------------------------
# 1.0   	1-Nov-2016  	Jemin Gohil    		    Started coding
# 2.0       3-Nov-2016      Jemin Gohil              Logic for printing rejection notice
# ================================================================================

import sys
import ast
import json
import os.path
sys.path.append("Python")
import common_functions
sys.path.append("Python/Entities")
import applicant
sys.path.append("Python/User_Stories")
import application_status

front_end_str = json.dumps({"data" :[{"applicant_id":"1"}]}) #Need to remove

class Notice(object):
	"""docstring for AcceptanceNotice"""
	def __init__(self):
		pass
		
	def acceptance(self,front_end_str):
		
		front_end_dict = ast.literal_eval(front_end_str)
		front_end_data = front_end_dict['data'][0]
		print('front_end_data :',front_end_data)

		cf = common_functions.Common_functions() 
		data = cf.getFromCsv('applicant.csv',front_end_data)
		#print(data)

		app = application_status.Application_status(front_end_str)
		data1 = app.getApplicationStatus(front_end_str)

		data[0]["violations"] = data1[0]["violations"]
		data[0]["application_status"] = data1[0]["application_status"]
		
		with open("Dustbin/Jemin/r_template.txt", "r") as myfile:
			template = myfile.readlines()
			temp = '\n'.join(template)

		print(temp)
		#print(data[0].keys()[0])
		for j in range(0,len(data)):
			t = temp
			for i in data[j].keys():
				#print(i)
				if('*'+i+'*' in temp):
					t = t.replace('*'+i+'*',"abc")
					print ("yes")
			#print(t)
				save_path = 'Dustbin/Jemin/'
				name_of_file = data[0]["applicant_first_name"]+"_"+data[0]["applicant_last_name"]+"_"+data[0]["applicant_id"]+"_rejection_letter"
				completeName = os.path.join(save_path, name_of_file + ".txt")
				text_file = open(completeName,"w")
				text_file.write(t)
				text_file.close()
			print(t)

ap = Notice()
ap.acceptance(front_end_str)
