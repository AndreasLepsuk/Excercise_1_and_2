import unittest

def count_to_ten_for():
    '''
    paranda koodi nii, et tagastatav väärtus oleks järgmine: [1,2,3,4,5,6,7,8,9,10] 
    '''
    #Todo 
    result = []
    for i in range (1, 11):
        result.append(i)
    return result

def count_from_ten_to_zero_while():
    '''
    paranda koodi nii, et tagastatav väärtus oleks järgmine: [10,9,8,7,6,5,4,3,2,1,0] 
    '''
    #Todo
    result = []
    i = 10
    while i >= 0:
        result.append(i)
        i = i - 1
    return result

def reverse_tuple(mytuple):
    '''
    Teosta meetod, mis tagastab tuple tüüpi andmehulga tagurpidi järjestuses
    '''
    #Todo
    reversetuple = mytuple[::-1]
    return reversetuple

def reverse_string(mystring):
    '''
    tee mooteod, mis pöörab string tüüpi muutuja tagurpidi ja tagastab selle
    '''
    #Todo
    revstring = mystring[::-1]
    return revstring

def remove_first_two_and_last_two_symbols(mystring1):
    '''
    tee meetod, mis eemaldab string tüüpi muutujalt 2 tähemärki algusest ja 2 lõpust ning tagastab selle
    '''
    #Todo
    SlicedString = mystring1[2:4]
    return SlicedString



class KoodiTest(unittest.TestCase):
    def test_count_to_ten_for(self):
        expectation = [1,2,3,4,5,6,7,8,9,10]
        self.assertEqual(expectation, count_to_ten_for(),"Kümneni lugemine ja listi lisamine for tsükkliga ebaõnnestus")

    def test_count_from_ten_to_zero_while(self):
        expectation = [10,9,8,7,6,5,4,3,2,1,0]
        self.assertEqual(expectation, count_from_ten_to_zero_while(),"Kümnest nullini lugemine ja listi lisamine while tsükkliga ebaõnnestus")
    
    def test_reverse_tuple(self):
        expectation = (10,9,8,7,6,5,4,3,2,1,0)
        mytuple = (0,1,2,3,4,5,6,7,8,9,10)
        self.assertEqual(expectation, reverse_tuple(mytuple),"annab tuplei tagurpidi")

    def test_reverse_string(self):
        expectation = "python"
        mystring = 'nohtyp'
        self.assertEqual(expectation, reverse_string(mystring),"annab string muutuja tagurpidi tagasi")

    def test_remove_first_two_and_last_two_symbols(self):
        expectation = "th"
        mystring1 = "python"
        self.assertEqual(expectation, mystring1, "eemaldab esimesed 2 ja viimased 2 sümbolit")

if __name__ == '__main__':
    unittest.main()