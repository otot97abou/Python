#-------------------------------------------------------------------------------
# Name:        chrono
# Purpose:
#
# Author:      othmane abouelaecha
#
# Created:     14/03/2015
# Copyright:   (c) othmane abouelaecha 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import tkinter

class Chrono(tkinter.Label) :
    def __init__(self,root,startTime=70):
        tkinter.Label.__init__(self,root,text='starting ...')
        self.value = startTime
        self.font = ('Helvetica', 25, 'normal')
        self.__setitem__('font', self.font)
        self.after(1000, self.count)

    def formatTime(self):
        return str(self.value//60)+' : ' + str(self.value%60)

    def count(self):
        if self.value > 0 : self.value = self.value - 1
        else : self.value = 0

        self.__setitem__('text', self.formatTime())
        self.after(1000,self.count)

if __name__ == "__main__" :
    root = tkinter.Tk()
    root.title('Chtit Chrono')
    label = Chrono(root,130)
    label.pack()
    root.mainloop()
