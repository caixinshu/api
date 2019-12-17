# -*- coding: utf-8 -*-
import win32clipboard as board
import win32con

def getText():
    board.OpenClipboard()
    d = board.GetClipboardData(win32con.CF_TEXT)
    #print d
    board.CloseClipboard()
    return d

def setText(aString):
    board.OpenClipboard()
    board.EmptyClipboard()
    board.SetClipboardData(win32con.CF_TEXT, aString)
    board.CloseClipboard()


#setText("D:\ABC")
#print getText()