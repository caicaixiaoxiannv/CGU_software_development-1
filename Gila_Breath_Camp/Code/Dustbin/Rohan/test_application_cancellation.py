import sys
import json
import ast
sys.path.append("Python/User_Stories")
import application_cancellation
import application_status
sys.path.append("Python/Entities")
import applicant

front_end_str1 = json.dumps({"data" :[{"camp_time_slots":"2017-02-10 00:00:00.000000"}]})
front_end_str2 = json.dumps({"data" :[{"applicant_id": "2","cancel_flag":"1"},{"applicant_id": "3","cancel_flag":"1"}]})
apps = application_cancellation.Application_cancellation()
#st = apps.getApplicationCancellation(front_end_str1)
#st = apps.setCancelFlag(front_end_str2)
st = apps.setManyCancelFlag(front_end_str2)
print(st)
#re = applicant.Applicant()
#ref = re.setrefund(front_end_str2)
#print(ref)
