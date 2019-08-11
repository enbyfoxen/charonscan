from uuid import UUID

def validate_uuid4(uuid_string):

    
    #Validate that a UUID string is in
    #fact a valid uuid
    #Happily, the uuid module does the actual
    #checking for us.

    try:
        val = UUID(uuid_string)
    except ValueError:
        # If it's a value error, then the string 
        # is not a valid hex code for a UUID.
        return False

    # return the UUID string if it correct
    return val
