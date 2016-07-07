import re
#re-> regular 정규표현식

def validate_phone_number(number) :
    if re.match(r'^01[016789][1-9]\d{6,7}$', number):
        return True
    return False
# r'의 r은 raw

print (validate_phone_number('01028761951'))
print (validate_phone_number('010287619'))
