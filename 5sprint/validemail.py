import re
def valid_email(mail):
    try:
        if '@' in mail:
            mail=mail.split('@')
            if len(mail)>2:
                raise Exception("Email is not valid")
            elif re.match(r'[a-zA-Z]+\.[a-zA-Z.]+',mail[1]) == None:
                raise Exception("Email is not valid")
        else:
                raise Exception("Email is not valid")
    except Exception as e:
        return e
    else:
        return "Email is valid"
