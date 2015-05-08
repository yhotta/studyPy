# -*- coding: utf-8 -*-
__author__ = 'hotta.yoshinori'

import datetime

class primeNumber():
    def __init__(self, iMax):
        self.max = iMax
        self.array = []
#        self.array = range(self.max+1) # 1～maxまでの配列  ※素数以外は、array[n] = False にする
#        self.array = [0,1,2,3,4,5,6,7,8,9,10] # 1～maxまでの配列  ※素数以外は、array[n] = False にする
        for i in range(self.max+1):
            self.array.append(i)



    def mkEratosthenesArray(self):

        # 面倒なので、2と3の倍数は素数以外を設定する(高速化するには、5と7と11...も）
        i = 4                                 # 高速ポイント
        while i <= self.max:
            if i % 2 == 0 or i % 3 == 0:     # 高速化ポイント
                # print(self.array)
                # print(list(self.array))
                # print(len(self.array))
                self.array[i] = False
            i += 1

        i = 4                               # 高速ポイント
        while i <= self.max:
            if i == 1:
                continue

            if self.array[i] != False:
                self._falseArray(i)
            i += 1


    def _falseArray(self, iVal):   # 約数つぶし（素数の倍数は素数でないので配列内をFalseに倒す）
        i = iVal*2
        while i <= self.max:
            if i%iVal == 0:
                self.array[i] = False
            i += iVal



    def _time(self):
        self.jpTime = datetime.datetime.utcnow()+datetime.timedelta(hours=9)
        print(self.jpTime.strftime('%M:%S.%f'))

    def run(self):
        for i in self.array:
            if self.array[i] != False:
                print(i)


if __name__ == '__main__':
    pn = primeNumber(10000)
    pn.mkEratosthenesArray()
    pn.run()





