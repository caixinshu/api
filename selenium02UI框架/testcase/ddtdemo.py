# coding=utf-8
import unittest
from ddt import ddt,data,unpack


@ddt
class PrintNum(unittest.TestCase):
    '''输出一些信息'''
    sample_list = ['a','b','1']
    sample_list1 = ['c','d','2']


    # @data(1,0,-1)
    # def testprintvalue(self,value):
    #     print value

    # @data(sample_list,sample_list1)
    # def testprintvalue001(self,value):
    #     a1,b1,c1=value
    #     print a1
    #     print b1
    #     print c1

    # @data((1,2),(3,4),(5,6))
    # @unpack
    # def testprintvalue002(self,value,value1):
    #    # a1,b1,c1=value
    #     print value+value1

    @data({'first': 1, 'second': 3, 'third': 2},
          {'first': 4, 'second': 6, 'third': 5})
    @unpack
    def testprintvalue002(self,first,second,third):
       # a1,b1,c1=value
        print first


if __name__=='__main__':
    unittest.main(verbosity=2)