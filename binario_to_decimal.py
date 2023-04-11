import unittest

def decimal2binario(decimal):
   
    if decimal <= 0:
        return 0
    
    binario = ''
    while decimal > 0:
        resto = decimal % 2
        binario = str(resto) + binario
        decimal = decimal // 2
        
    return binario + 0





class TestNumeracion(unittest.TestCase):
    # def test_binario2decimal(self):
    #     self.assertEqual(binario2decimal('01011100'),92)
    def test_decimal2binario(self):
        self.assertEqual(decimal2binario(97),'01100001')
    

if __name__ == '__main__':
    unittest.main()