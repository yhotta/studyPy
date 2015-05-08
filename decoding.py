# -*- coding: utf-8 -*-
__author__ = 'hotta.yoshinori'

class hoge:
    def __init__(self):
        self.caesar = list("qdq-gi.q-a ziatmxxitmdqibtqi-ustbi ri.qmoqrcxi.qbubu zir -ibtqi-qp-qaai ripmymsqkir -ibtqi-qy dmxi ri.cnxuoi rruoumxakir -ibtqiqzmobyqzbkii-q.qmxi -imyqzpyqzbi rixmeaki -puzmzoqai -i-qscxmbu zaimzpir -i btq-iymbbq-a;iz -iatmxximzgi.q-a zinqiuzimzgiemgipuao-uyuzmbqpimsmuzabir -ia. za -uzsiacotiimi.qbubu zj")
        self.array = list("abcdefghijklmnopqrstuvwxyz .,-")
        self.bingo = "person"

    def getStringData(self, iShift):
        retVal = []
        i = 0
        while i < len(self.caesar):
            a = self.caesar[i]
            if a == ';':
                retVal.append(';')
            else:
                retVal.append(self._getVal(a, iShift))

            i += 1

        return retVal


    def _getVal(self, cA, iShift):
        n = self.array.index(cA)

        rep = 0
        if n + iShift < len(self.array):
            rep = n + iShift
        else:
            rep = n + iShift - len(self.array)

        return self.array[rep]

if __name__ == '__main__':
    h = hoge()
    i = 0
    while i <= 20:
        listData = h.getStringData(i)
        aStr = "".join(listData)
        print(i, " : ", aStr)
        i += 1
