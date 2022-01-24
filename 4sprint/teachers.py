class Testpaper:
    def __init__(self, subject, markscheme, pass_mark):
        self.subject=subject
        self.markscheme=markscheme
        self.pass_mark=pass_mark

class Student:
    def __init__(self):
        self.tests_taken="No tests taken"
    def take_test(self, obj, marks):
        count,result = 0,""
        for i in range(len(marks)):
            if marks[i] == obj.markscheme[i]:
                count += 1
        percent=round(100*count/len(obj.markscheme))
        result= f"Passed! ({percent}%)" if percent>=float(obj.pass_mark[:-1]) else f"Failed! ({percent}%)"
        if type(self.tests_taken)!=dict:
            self.tests_taken={obj.subject:result}
        else:
            self.tests_taken.update({obj.subject:result})