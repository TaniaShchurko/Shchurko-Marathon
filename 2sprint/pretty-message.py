data = "Another input data string"
import re
def pretty_message(data_prev):
    data_next=re.sub(r'([a-z]*)\1+', r'\1', data_prev)
    while data_prev!=data_next:
        data_prev = data_next
        data_next = re.sub(r'([a-z]*)\1+', r'\1', data_prev)
    return data_next
print(pretty_message(data))