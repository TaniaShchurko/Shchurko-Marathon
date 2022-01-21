import re
def create_account(user_name, password, secret_words):
    if len(password) >= 6 and len(re.findall(r'[A-Z]', password)) > 0 and len(re.findall(r'[a-z]', password)) > 0 \
            and len(re.findall(r'\d', password)) > 0 and len(re.findall(r'[_!@#$%^&*()+]', password)) > 0:
        def check(password1, secret_words1):
            if password1 == password and len(secret_words)==len(secret_words1):
                misspells=[]
                for i in range(len(secret_words)):
                    if secret_words[i] not in secret_words1:
                        misspells.append(1)
                misspells1 = []
                for i in range(len(secret_words1)):
                    if secret_words1[i] not in secret_words:
                        misspells1.append(1)
                if len(password1)>=6 and len(re.findall(r'[A-Z]', password1))>0 and len(re.findall(r'[a-z]', password1))>0\
                        and len(re.findall(r'\d', password1))>0 and len(re.findall(r'[_!@#$%^&*()+]', password1))>0 and len(misspells)<=1 and len(misspells1)<=1:
                    return True
                else:
                    return False
            else:
                return False
    else:
        raise ValueError
    return check
