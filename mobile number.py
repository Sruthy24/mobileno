''' AUTHOR= SRUTHY S
DESCRIPTION = Input two lists from the user. Merge these lists into a third list such that in the merged list, all even numbers occur first followed by odd numbers. Both the even numbers and odd numbers should be in sorted order.'''
def mobile_number(number):
    if len(number)== 10 and number[0] in ["9","8","7"]:

        return True
    return False
mobile= input("enter a mobile number:")
if mobile_number(mobile):
    print("valid")
else:
    print("not valid")




