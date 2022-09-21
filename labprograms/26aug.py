from logging import raiseExceptions

dob = input("Enter you Date of Birth: ")
if any dob==' ':
    raise Exception("Your Date of birth cannot be empty")
if any dob=='?':
    raise Exception("Please enter the date in the any format but using the slash('/')")
        
