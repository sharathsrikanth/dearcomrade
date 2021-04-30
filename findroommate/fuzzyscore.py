from fuzzywuzzy import fuzz
from findroommate.models import ResultantTempUserTable
from viewrateusers.models import Userpreference

def findscores(users, userpreference):
    pref = userpreference.prefapartment1+userpreference.prefapartment2+userpreference.prefapartment3
    for user in users:
        tempuserpref = Userpreference.objects.get(userid=user.userid)
        temp = tempuserpref.prefapartment1+tempuserpref.prefapartment2+tempuserpref.prefapartment3
        ratio = fuzz.ratio(pref.lower(),temp.lower())
        row = ResultantTempUserTable.objects.get(userid=user.userid)
        row.compatibilityscore = ratio
        row.save(update_fields=['compatibilityscore'])

    return