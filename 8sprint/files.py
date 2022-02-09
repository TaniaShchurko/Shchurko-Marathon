import unittest

def file_parser(file, string1, string2=None):
    if type(string1) is not str:
        raise TypeError
    with open(file,'r') as f:
        data=f.read()
    data = data.split()
    counted = 0
    if string2 is not None:
        for i in range(len(data)):
            if data[i]==string1:
                data[i]=string2
                counted+=1
        with open(file,'w') as f:
            f.truncate()
            f.write(''.join(data))
        return f"Replaced {counted} strings"
    else:
        counted=list(data).count(string1)
        return f"Found {counted} strings"

class ParserTest(unittest.TestCase):
    def test_exception(self):
        with self.assertRaises(TypeError):
            file_parser("", 3)
    def test_equal(self):
       self.assertEqual(file_parser('parser.txt', 'better'), 'Found 8 strings')
