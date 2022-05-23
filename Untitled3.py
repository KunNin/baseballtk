#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pymongo
client=pymongo.MongoClient("mongodb+srv://KunNing:WAYI9988@cluster0.gxcoz.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db1=client.Monkey
db2=client.FB
db3=client.ChunShin
db4=client.Way
db5=client.Seven
import tkinter as tk
import PIL.Image
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
from tkinter import *
import tkinter.ttk as ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
#------------------------------------(樂天)
collection6=db1.Monkey2021
result25=collection6.find_one({"年度":"2021(上)"})
result26=collection6.find_one({"年度":"2021(下)"})
result27=collection6.find_one({"防禦率":"4.15"})
result28=collection6.find_one({"盜壘成功":"95"})
result29=collection6.find_one({"捕逸":"7"})
collection7=db1.Monkey2020
result30=collection7.find_one({"年度":"2020(上)"})
result31=collection7.find_one({"年度":"2020(下)"})
result32=collection7.find_one({"防禦率":"5.82"})
result33=collection7.find_one({"盜壘成功":"100"})
result34=collection7.find_one({"捕逸":"10"})
collection8=db1.Monkey2019
result35=collection8.find_one({"年度":"2019(上)"})
result36=collection8.find_one({"年度":"2019(下)"})
result37=collection8.find_one({"防禦率":"5.11"})
result38=collection8.find_one({"盜壘成功":"55"})
result39=collection8.find_one({"捕逸":"5"})
collection9=db1.Monkey2018
result40=collection9.find_one({"年度":"2018(上)"})
result41=collection9.find_one({"年度":"2018(下)"})
result42=collection9.find_one({"防禦率":"4.39"})
result43=collection9.find_one({"盜壘成功":"47"})
result44=collection9.find_one({"捕逸":"7"})
collection10=db1.Monkey2017
result45=collection10.find_one({"年度":"2017(上)"})
result46=collection10.find_one({"年度":"2017(下)"})
result47=collection10.find_one({"防禦率":"4.29"})
result48=collection10.find_one({"盜壘成功":"83"})
result49=collection10.find_one({"捕逸":"4"})
#------------------------------------(富邦)
collection11=db2.FB2021
result50=collection11.find_one({"年度":"2021(上)"})
result51=collection11.find_one({"年度":"2021(下)"})
result52=collection11.find_one({"防禦率":"3.53"})
result53=collection11.find_one({"盜壘成功":"67"})
result54=collection11.find_one({"捕逸":"7"})
collection12=db2.FB2020
result55=collection12.find_one({"年度":"2020(上)"})
result56=collection12.find_one({"年度":"2020(下)"})
result57=collection12.find_one({"防禦率":"5.23"})
result58=collection12.find_one({"盜壘成功":"79"})
result59=collection12.find_one({"捕逸":"6"})
collection13=db2.FB2019
result60=collection13.find_one({"年度":"2019(上)"})
result61=collection13.find_one({"年度":"2019(下)"})
result62=collection13.find_one({"防禦率":"4.23"})
result63=collection13.find_one({"盜壘成功":"78"})
result64=collection13.find_one({"捕逸":"8"})
collection14=db2.FB2018
result65=collection14.find_one({"年度":"2018(上)"})
result66=collection14.find_one({"年度":"2018(下)"})
result67=collection14.find_one({"防禦率":"4.72"})
result68=collection14.find_one({"盜壘成功":"89"})
result69=collection14.find_one({"捕逸":"4"})
collection15=db2.FB2017
result70=collection15.find_one({"年度":"2017(上)"})
result71=collection15.find_one({"年度":"2017(下)"})
result72=collection15.find_one({"防禦率":"5.03"})
result73=collection15.find_one({"盜壘成功":"51"})
result74=collection15.find_one({"捕逸":"5"})
#------------------------------------(統一)
collection16=db5.Seven2021
result75=collection6.find_one({"年度":"2021(上)"})
result76=collection6.find_one({"年度":"2021(下)"})
result77=collection6.find_one({"防禦率":"4.15"})
result78=collection6.find_one({"盜壘成功":"95"})
result79=collection6.find_one({"捕逸":"7"})
collection17=db5.Seven2020
result80=collection7.find_one({"年度":"2020(上)"})
result81=collection7.find_one({"年度":"2020(下)"})
result82=collection7.find_one({"防禦率":"5.82"})
result83=collection7.find_one({"盜壘成功":"100"})
result84=collection7.find_one({"捕逸":"10"})
collection18=db5.Seven2019
result85=collection8.find_one({"年度":"2019(上)"})
result86=collection8.find_one({"年度":"2019(下)"})
result87=collection8.find_one({"防禦率":"5.11"})
result88=collection8.find_one({"盜壘成功":"55"})
result89=collection8.find_one({"捕逸":"5"})
collection19=db5.Seven2018
result90=collection9.find_one({"年度":"2018(上)"})
result91=collection9.find_one({"年度":"2018(下)"})
result92=collection9.find_one({"防禦率":"4.39"})
result93=collection9.find_one({"盜壘成功":"47"})
result94=collection9.find_one({"捕逸":"7"})
collection20=db5.Seven2017
result95=collection10.find_one({"年度":"2017(上)"})
result96=collection10.find_one({"年度":"2017(下)"})
result97=collection10.find_one({"防禦率":"4.29"})
result98=collection10.find_one({"盜壘成功":"83"})
result99=collection10.find_one({"捕逸":"4"})
#------------------------------------(味全)
collection21=db4.Way2021
result100=collection21.find_one({"年度":"2021(上)"})
result101=collection21.find_one({"年度":"2021(下)"})
result102=collection21.find_one({"防禦率":"3.93"})
result103=collection21.find_one({"盜壘成功":"86"})
result104=collection21.find_one({"捕逸":"9"})
#------------------------------------(中信)
collection=db3.ChunShin2021
result=collection.find_one({"年度":"2021(上)"})
result1=collection.find_one({"年度":"2021(下)"})
result2=collection.find_one({"防禦率":"3.66"})
result3=collection.find_one({"盜壘成功":"83"})
result4=collection.find_one({"捕逸":"8"})
collection2=db3.ChunShin2020
result5=collection2.find_one({"年度":"2020(上)"})
result6=collection2.find_one({"年度":"2020(下)"})
result7=collection2.find_one({"防禦率":"4.2"})
result8=collection2.find_one({"盜壘成功":"75"})
result9=collection2.find_one({"捕逸":"4"})
collection3=db3.ChunShin2019
result10=collection3.find_one({"年度":"2019(上)"})
result11=collection3.find_one({"年度":"2019(下)"})
result12=collection3.find_one({"防禦率":"4.58"})
result13=collection3.find_one({"盜壘成功":"84"})
result14=collection3.find_one({"捕逸":"6"})
collection4=db3.ChunShin2018
result15=collection4.find_one({"年度":"2018(上)"})
result16=collection4.find_one({"年度":"2018(下)"})
result17=collection4.find_one({"防禦率":"5.09"})
result18=collection4.find_one({"盜壘成功":"81"})
result19=collection4.find_one({"捕逸":"10"})
collection5=db3.ChunShin2017
result20=collection5.find_one({"年度":"2017(上)"})
result21=collection5.find_one({"年度":"2017(下)"})
result22=collection5.find_one({"防禦率":"5.16"})
result23=collection5.find_one({"盜壘成功":"109"})
result24=collection5.find_one({"捕逸":"11"})
#------------------------------------(樂天)
del result25["_id"]
MK1=(str(result25).replace("{","").replace("}", "").replace("'",""))
del result26["_id"]
MK2=(str(result26).replace("{","").replace("}", "").replace("'",""))
del result27["_id"]
MK3=(str(result27).replace("{","").replace("}", "").replace("'",""))
del result28["_id"]
MK4=(str(result28).replace("{","").replace("}", "").replace("'",""))
del result29["_id"]
MK5=(str(result29).replace("{","").replace("}", "").replace("'",""))
del result30["_id"]
MK6=(str(result30).replace("{","").replace("}", "").replace("'",""))
del result31["_id"]
MK7=(str(result31).replace("{","").replace("}", "").replace("'",""))
del result32["_id"]
MK8=(str(result32).replace("{","").replace("}", "").replace("'",""))
del result33["_id"]
MK9=(str(result33).replace("{","").replace("}", "").replace("'",""))
del result34["_id"]
MK10=(str(result34).replace("{","").replace("}", "").replace("'",""))
del result35["_id"]
MK11=(str(result35).replace("{","").replace("}", "").replace("'",""))
del result36["_id"]
MK12=(str(result36).replace("{","").replace("}", "").replace("'",""))
del result37["_id"]
MK13=(str(result37).replace("{","").replace("}", "").replace("'",""))
del result38["_id"]
MK14=(str(result38).replace("{","").replace("}", "").replace("'",""))
del result39["_id"]
MK15=(str(result39).replace("{","").replace("}", "").replace("'",""))
del result40["_id"]
MK16=(str(result40).replace("{","").replace("}", "").replace("'",""))
del result41["_id"]
MK17=(str(result41).replace("{","").replace("}", "").replace("'",""))
del result42["_id"]
MK18=(str(result42).replace("{","").replace("}", "").replace("'",""))
del result43["_id"]
MK19=(str(result43).replace("{","").replace("}", "").replace("'",""))
del result44["_id"]
MK20=(str(result44).replace("{","").replace("}", "").replace("'",""))
del result45["_id"]
MK21=(str(result45).replace("{","").replace("}", "").replace("'",""))
del result46["_id"]
MK22=(str(result46).replace("{","").replace("}", "").replace("'",""))
del result47["_id"]
MK23=(str(result47).replace("{","").replace("}", "").replace("'",""))
del result48["_id"]
MK24=(str(result48).replace("{","").replace("}", "").replace("'",""))
del result49["_id"]
MK25=(str(result49).replace("{","").replace("}", "").replace("'",""))
#------------------------------------(富邦)
del result50["_id"]
FB1=(str(result50).replace("{","").replace("}", "").replace("'",""))
del result51["_id"]
FB2=(str(result51).replace("{","").replace("}", "").replace("'",""))
del result52["_id"]
FB3=(str(result52).replace("{","").replace("}", "").replace("'",""))
del result53["_id"]
FB4=(str(result53).replace("{","").replace("}", "").replace("'",""))
del result54["_id"]
FB5=(str(result54).replace("{","").replace("}", "").replace("'",""))
del result55["_id"]
FB6=(str(result55).replace("{","").replace("}", "").replace("'",""))
del result56["_id"]
FB7=(str(result56).replace("{","").replace("}", "").replace("'",""))
del result57["_id"]
FB8=(str(result57).replace("{","").replace("}", "").replace("'",""))
del result58["_id"]
FB9=(str(result58).replace("{","").replace("}", "").replace("'",""))
del result59["_id"]
FB10=(str(result59).replace("{","").replace("}", "").replace("'",""))
del result60["_id"]
FB11=(str(result60).replace("{","").replace("}", "").replace("'",""))
del result61["_id"]
FB12=(str(result61).replace("{","").replace("}", "").replace("'",""))
del result62["_id"]
FB13=(str(result62).replace("{","").replace("}", "").replace("'",""))
del result63["_id"]
FB14=(str(result63).replace("{","").replace("}", "").replace("'",""))
del result64["_id"]
FB15=(str(result64).replace("{","").replace("}", "").replace("'",""))
del result65["_id"]
FB16=(str(result65).replace("{","").replace("}", "").replace("'",""))
del result66["_id"]
FB17=(str(result66).replace("{","").replace("}", "").replace("'",""))
del result67["_id"]
FB18=(str(result67).replace("{","").replace("}", "").replace("'",""))
del result68["_id"]
FB19=(str(result68).replace("{","").replace("}", "").replace("'",""))
del result69["_id"]
FB20=(str(result69).replace("{","").replace("}", "").replace("'",""))
del result70["_id"]
FB21=(str(result70).replace("{","").replace("}", "").replace("'",""))
del result71["_id"]
FB22=(str(result71).replace("{","").replace("}", "").replace("'",""))
del result72["_id"]
FB23=(str(result72).replace("{","").replace("}", "").replace("'",""))
del result73["_id"]
FB24=(str(result73).replace("{","").replace("}", "").replace("'",""))
del result74["_id"]
FB25=(str(result74).replace("{","").replace("}", "").replace("'",""))
#------------------------------------(統一)
del result75["_id"]
SE1=(str(result75).replace("{","").replace("}", "").replace("'",""))
del result76["_id"]
SE2=(str(result76).replace("{","").replace("}", "").replace("'",""))
del result77["_id"]
SE3=(str(result77).replace("{","").replace("}", "").replace("'",""))
del result78["_id"]
SE4=(str(result78).replace("{","").replace("}", "").replace("'",""))
del result79["_id"]
SE5=(str(result79).replace("{","").replace("}", "").replace("'",""))
del result80["_id"]
SE6=(str(result80).replace("{","").replace("}", "").replace("'",""))
del result81["_id"]
SE7=(str(result81).replace("{","").replace("}", "").replace("'",""))
del result82["_id"]
SE8=(str(result82).replace("{","").replace("}", "").replace("'",""))
del result83["_id"]
SE9=(str(result83).replace("{","").replace("}", "").replace("'",""))
del result84["_id"]
SE10=(str(result84).replace("{","").replace("}", "").replace("'",""))
del result85["_id"]
SE11=(str(result85).replace("{","").replace("}", "").replace("'",""))
del result86["_id"]
SE12=(str(result86).replace("{","").replace("}", "").replace("'",""))
del result87["_id"]
SE13=(str(result87).replace("{","").replace("}", "").replace("'",""))
del result88["_id"]
SE14=(str(result88).replace("{","").replace("}", "").replace("'",""))
del result89["_id"]
SE15=(str(result89).replace("{","").replace("}", "").replace("'",""))
del result90["_id"]
SE16=(str(result90).replace("{","").replace("}", "").replace("'",""))
del result91["_id"]
SE17=(str(result91).replace("{","").replace("}", "").replace("'",""))
del result92["_id"]
SE18=(str(result92).replace("{","").replace("}", "").replace("'",""))
del result93["_id"]
SE19=(str(result93).replace("{","").replace("}", "").replace("'",""))
del result94["_id"]
SE20=(str(result94).replace("{","").replace("}", "").replace("'",""))
del result95["_id"]
SE21=(str(result95).replace("{","").replace("}", "").replace("'",""))
del result96["_id"]
SE22=(str(result96).replace("{","").replace("}", "").replace("'",""))
del result97["_id"]
SE23=(str(result97).replace("{","").replace("}", "").replace("'",""))
del result98["_id"]
SE24=(str(result98).replace("{","").replace("}", "").replace("'",""))
del result99["_id"]
SE25=(str(result99).replace("{","").replace("}", "").replace("'",""))
#------------------------------------(味全)
del result100["_id"]
WA1=(str(result100).replace("{","").replace("}", "").replace("'",""))
del result101["_id"]
WA2=(str(result101).replace("{","").replace("}", "").replace("'",""))
del result102["_id"]
WA3=(str(result102).replace("{","").replace("}", "").replace("'",""))
del result103["_id"]
WA4=(str(result103).replace("{","").replace("}", "").replace("'",""))
del result104["_id"]
WA5=(str(result104).replace("{","").replace("}", "").replace("'",""))
#------------------------------------(中信)
del result["_id"]
CH1=(str(result).replace("{","").replace("}", "").replace("'",""))
del result1["_id"]
CH2=(str(result1).replace("{","").replace("}", "").replace("'",""))
del result2["_id"]
CH3=(str(result2).replace("{","").replace("}", "").replace("'",""))
del result3["_id"]
CH4=(str(result3).replace("{","").replace("}", "").replace("'",""))
del result4["_id"]
CH5=(str(result4).replace("{","").replace("}", "").replace("'",""))
del result5["_id"]
CH6=(str(result5).replace("{","").replace("}", "").replace("'",""))
del result6["_id"]
CH7=(str(result6).replace("{","").replace("}", "").replace("'",""))
del result7["_id"]
CH8=(str(result7).replace("{","").replace("}", "").replace("'",""))
del result8["_id"]
CH9=(str(result8).replace("{","").replace("}", "").replace("'",""))
del result9["_id"]
CH10=(str(result9).replace("{","").replace("}", "").replace("'",""))
del result10["_id"]
CH11=(str(result10).replace("{","").replace("}", "").replace("'",""))
del result11["_id"]
CH12=(str(result11).replace("{","").replace("}", "").replace("'",""))
del result12["_id"]
CH13=(str(result12).replace("{","").replace("}", "").replace("'",""))
del result13["_id"]
CH14=(str(result13).replace("{","").replace("}", "").replace("'",""))
del result14["_id"]
CH15=(str(result14).replace("{","").replace("}", "").replace("'",""))
del result15["_id"]
CH16=(str(result15).replace("{","").replace("}", "").replace("'",""))
del result16["_id"]
CH17=(str(result16).replace("{","").replace("}", "").replace("'",""))
del result17["_id"]
CH18=(str(result17).replace("{","").replace("}", "").replace("'",""))
del result18["_id"]
CH19=(str(result18).replace("{","").replace("}", "").replace("'",""))
del result19["_id"]
CH20=(str(result19).replace("{","").replace("}", "").replace("'",""))
del result20["_id"]
CH21=(str(result20).replace("{","").replace("}", "").replace("'",""))
del result21["_id"]
CH22=(str(result21).replace("{","").replace("}", "").replace("'",""))
del result22["_id"]
CH23=(str(result22).replace("{","").replace("}", "").replace("'",""))
del result23["_id"]
CH24=(str(result23).replace("{","").replace("}", "").replace("'",""))
del result24["_id"]
CH25=(str(result24).replace("{","").replace("}", "").replace("'",""))
win=Tk()
#視窗屬性設定區
win.title("職棒成績查詢系統")
win.geometry("1290x900")
win_main=ttk.Notebook()
win_main.place(relx=0,rely=0,relwidth=1,relheight=1)
win1=Frame(win_main)

win1.place(x=0,y=30)
win_main.add(win1,text="page1")
tab2=Frame(win_main)
tab2.place(x=100,y=30)
win_main.add(tab2,text="page2")
fig=plt.figure(figsize=(7,4),dpi=100)

canvas=tk.Canvas(win1,width=1290,height=900,bd=0, highlightthickness=0)
imgpath = 'base.gif'
img = PIL.Image.open(imgpath)
photo9 = ImageTk.PhotoImage(img)
canvas.create_image(645,482, image=photo9)
canvas.pack()
win.resizable(False,False)#鎖定視窗大小是否可更動
win.iconbitmap("Baseball.ico")#更改ICON

#------------------------------------(桃猿)
def Monkey2021():
    lb1.config(text=MK1,font=("微軟正黑體", 14,"bold"))
    lb2.config(text=MK2,font=("微軟正黑體", 14,"bold"))
    lb3.config(text=MK3,font=("微軟正黑體", 12,"bold"))
    lb4.config(text=MK4,font=("微軟正黑體", 11,"bold"))
    lb5.config(text=MK5,font=("微軟正黑體", 14,"bold"))
def Monkey2020():
    lb1.config(text=MK6,font=("微軟正黑體", 14,"bold"))
    lb2.config(text=MK7,font=("微軟正黑體", 14,"bold"))
    lb3.config(text=MK8,font=("微軟正黑體", 12,"bold"))
    lb4.config(text=MK9,font=("微軟正黑體", 11,"bold"))
    lb5.config(text=MK10,font=("微軟正黑體", 14,"bold"))
def Monkey2019():
    lb1.config(text=MK11,font=("微軟正黑體", 14,"bold"))
    lb2.config(text=MK12,font=("微軟正黑體", 14,"bold"))
    lb3.config(text=MK13,font=("微軟正黑體", 12,"bold"))
    lb4.config(text=MK14,font=("微軟正黑體", 11,"bold"))
    lb5.config(text=MK15,font=("微軟正黑體", 14,"bold"))
def Monkey2018():
    lb1.config(text=MK16,font=("微軟正黑體", 14,"bold"))
    lb2.config(text=MK17,font=("微軟正黑體", 14,"bold"))
    lb3.config(text=MK18,font=("微軟正黑體", 12,"bold"))
    lb4.config(text=MK19,font=("微軟正黑體", 11,"bold"))
    lb5.config(text=MK20,font=("微軟正黑體", 14,"bold"))
def Monkey2017():
    lb1.config(text=MK21,font=("微軟正黑體", 14,"bold"))
    lb2.config(text=MK22,font=("微軟正黑體", 14,"bold"))
    lb3.config(text=MK23,font=("微軟正黑體", 12,"bold"))
    lb4.config(text=MK24,font=("微軟正黑體", 11,"bold"))
    lb5.config(text=MK25,font=("微軟正黑體", 14,"bold"))
#------------------------------------(富邦)
def FB2021():
    lb1.config(text=FB1,font=("微軟正黑體", 14,"bold"))
    lb2.config(text=FB2,font=("微軟正黑體", 14,"bold"))
    lb3.config(text=FB3,font=("微軟正黑體", 12,"bold"))
    lb4.config(text=FB4,font=("微軟正黑體", 11,"bold"))
    lb5.config(text=FB5,font=("微軟正黑體", 14,"bold"))
def FB2020():
    lb1.config(text=FB6,font=("微軟正黑體", 14,"bold"))
    lb2.config(text=FB7,font=("微軟正黑體", 14,"bold"))
    lb3.config(text=FB8,font=("微軟正黑體", 12,"bold"))
    lb4.config(text=FB9,font=("微軟正黑體", 11,"bold"))
    lb5.config(text=FB10,font=("微軟正黑體", 14,"bold"))
def FB2019():
    lb1.config(text=FB11,font=("微軟正黑體", 14,"bold"))
    lb2.config(text=FB12,font=("微軟正黑體", 14,"bold"))
    lb3.config(text=FB13,font=("微軟正黑體", 12,"bold"))
    lb4.config(text=FB14,font=("微軟正黑體", 11,"bold"))
    lb5.config(text=FB15,font=("微軟正黑體", 14,"bold"))
def FB2018():
    lb1.config(text=FB16,font=("微軟正黑體", 14,"bold"))
    lb2.config(text=FB17,font=("微軟正黑體", 14,"bold"))
    lb3.config(text=FB18,font=("微軟正黑體", 12,"bold"))
    lb4.config(text=FB19,font=("微軟正黑體", 11,"bold"))
    lb5.config(text=FB20,font=("微軟正黑體", 14,"bold"))
def FB2017():
    lb1.config(text=FB21,font=("微軟正黑體", 14,"bold"))
    lb2.config(text=FB22,font=("微軟正黑體", 14,"bold"))
    lb3.config(text=FB23,font=("微軟正黑體", 12,"bold"))
    lb4.config(text=FB24,font=("微軟正黑體", 11,"bold"))
    lb5.config(text=FB25,font=("微軟正黑體", 14,"bold"))
#------------------------------------(統一)
def Seven2021():
    lb1.config(text=SE1,font=("微軟正黑體", 14,"bold"))
    lb2.config(text=SE2,font=("微軟正黑體", 14,"bold"))
    lb3.config(text=SE3,font=("微軟正黑體", 12,"bold"))
    lb4.config(text=SE4,font=("微軟正黑體", 11,"bold"))
    lb5.config(text=SE5,font=("微軟正黑體", 14,"bold"))
def Seven2020():
    lb1.config(text=SE6,font=("微軟正黑體", 14,"bold"))
    lb2.config(text=SE7,font=("微軟正黑體", 14,"bold"))
    lb3.config(text=SE8,font=("微軟正黑體", 12,"bold"))
    lb4.config(text=SE9,font=("微軟正黑體", 11,"bold"))
    lb5.config(text=SE10,font=("微軟正黑體", 14,"bold"))
def Seven2019():
    lb1.config(text=SE11,font=("微軟正黑體", 14,"bold"))
    lb2.config(text=SE12,font=("微軟正黑體", 14,"bold"))
    lb3.config(text=SE13,font=("微軟正黑體", 12,"bold"))
    lb4.config(text=SE14,font=("微軟正黑體", 11,"bold"))
    lb5.config(text=SE15,font=("微軟正黑體", 14,"bold"))
def Seven2018():
    lb1.config(text=SE16,font=("微軟正黑體", 14,"bold"))
    lb2.config(text=SE17,font=("微軟正黑體", 14,"bold"))
    lb3.config(text=SE18,font=("微軟正黑體", 12,"bold"))
    lb4.config(text=SE19,font=("微軟正黑體", 11,"bold"))
    lb5.config(text=SE20,font=("微軟正黑體", 14,"bold"))
def Seven2017():
    lb1.config(text=SE21,font=("微軟正黑體", 14,"bold"))
    lb2.config(text=SE22,font=("微軟正黑體", 14,"bold"))
    lb3.config(text=SE23,font=("微軟正黑體", 12,"bold"))
    lb4.config(text=SE24,font=("微軟正黑體", 11,"bold"))
    lb5.config(text=SE25,font=("微軟正黑體", 14,"bold"))
#------------------------------------(味全)
def Way2021():
    lb1.config(text=WA1,font=("微軟正黑體", 14,"bold"))
    lb2.config(text=WA2,font=("微軟正黑體", 14,"bold"))
    lb3.config(text=WA3,font=("微軟正黑體", 12,"bold"))
    lb4.config(text=WA4,font=("微軟正黑體", 11,"bold"))
    lb5.config(text=WA5,font=("微軟正黑體", 14,"bold"))
#------------------------------------(中信)
def ChunShin2021():
    lb1.config(text=CH1,font=("微軟正黑體", 14,"bold"))
    lb2.config(text=CH2,font=("微軟正黑體", 14,"bold"))
    lb3.config(text=CH3,font=("微軟正黑體", 12,"bold"))
    lb4.config(text=CH4,font=("微軟正黑體", 11,"bold"))
    lb5.config(text=CH5,font=("微軟正黑體", 14,"bold"))
def ChunShin2020():
    lb1.config(text=CH6,font=("微軟正黑體", 14,"bold"))
    lb2.config(text=CH7,font=("微軟正黑體", 14,"bold"))
    lb3.config(text=CH8,font=("微軟正黑體", 12,"bold"))
    lb4.config(text=CH9,font=("微軟正黑體", 11,"bold"))
    lb5.config(text=CH10,font=("微軟正黑體", 14,"bold"))
def ChunShin2019():
    lb1.config(text=CH11,font=("微軟正黑體", 14,"bold"))
    lb2.config(text=CH12,font=("微軟正黑體", 14,"bold"))
    lb3.config(text=CH13,font=("微軟正黑體", 12,"bold"))
    lb4.config(text=CH14,font=("微軟正黑體", 11,"bold"))
    lb5.config(text=CH15,font=("微軟正黑體", 14,"bold"))
def ChunShin2018():
    lb1.config(text=CH16,font=("微軟正黑體", 14,"bold"))
    lb2.config(text=CH17,font=("微軟正黑體", 14,"bold"))
    lb3.config(text=CH18,font=("微軟正黑體", 12,"bold"))
    lb4.config(text=CH19,font=("微軟正黑體", 11,"bold"))
    lb5.config(text=CH20,font=("微軟正黑體", 14,"bold"))
def ChunShin2017():
    lb1.config(text=CH21,font=("微軟正黑體", 14,"bold"))
    lb2.config(text=CH22,font=("微軟正黑體", 14,"bold"))
    lb3.config(text=CH23,font=("微軟正黑體", 12,"bold"))
    lb4.config(text=CH24,font=("微軟正黑體", 11,"bold"))
    lb5.config(text=CH25,font=("微軟正黑體", 14,"bold"))
lb=tk.Label(win1,text="請點選想搜尋的球隊")
lb.config(bg="#14FF3C",fg="#FF6929",font=("微軟正黑體", 15,"bold"))
lb.place(relx=0,rely=0)

lb1=tk.Label(win1,text="")
lb1.config(bg="#ECF5FF",fg="#FF6929")
lb1.place(relx=0.07,rely=0.4)
lb6=tk.Label(win1,text="球隊成績:")
lb6.config(bg="#ECF5FF",fg="#FF6929",font=("微軟正黑體", 14,"bold"))
lb6.place(relx=0,rely=0.4)
lb2=tk.Label(win1,text="")
lb2.config(bg="#ECF5FF",fg="#FF6929")
lb2.place(relx=0.07,rely=0.5)
lb7=tk.Label(win1,text="球隊成績:")
lb7.config(bg="#ECF5FF",fg="#FF6929",font=("微軟正黑體", 14,"bold"))
lb7.place(relx=0,rely=0.5)
lb3=tk.Label(win1,text="")
lb3.config(bg="#ECF5FF",fg="#FF6929")
lb3.place(relx=0.07,rely=0.6)
lb8=tk.Label(win1,text="投手成績:")
lb8.config(bg="#ECF5FF",fg="#FF6929",font=("微軟正黑體", 14,"bold"))
lb8.place(relx=0,rely=0.6)
lb4=tk.Label(win1,text="")
lb4.config(bg="#ECF5FF",fg="#FF6929")
lb4.place(relx=0.07,rely=0.7)
lb9=tk.Label(win1,text="打擊成績:")
lb9.config(bg="#ECF5FF",fg="#FF6929",font=("微軟正黑體", 14,"bold"))
lb9.place(relx=0,rely=0.7)
lb5=tk.Label(win1,text="")
lb5.config(bg="#ECF5FF",fg="#FF6929")
lb5.place(relx=0.07,rely=0.8)
lb10=tk.Label(win1,text="守備成績:")
lb10.config(bg="#ECF5FF",fg="#FF6929",font=("微軟正黑體", 14,"bold"))
lb10.place(relx=0,rely=0.8)
img1=tk.PhotoImage(file="桃猿1.png")
img2= PIL.Image.open('富邦1.png')
photo = ImageTk.PhotoImage(img2)
img3=tk.PhotoImage(file="統一1.png")
img4= PIL.Image.open('中信1.png') 
photo2 = ImageTk.PhotoImage(img4)
img5= PIL.Image.open('味全1.png')
photo3 = ImageTk.PhotoImage(img5)
btn1=tk.Button(win1,text="click",command=Monkey2021)
btn2=tk.Button(win1,text="click",command=FB2021)
btn3=tk.Button(win1,text="click",command=Seven2021)
btn4=tk.Button(win1,text="click",command=ChunShin2021)
btn5=tk.Button(win1,text="click",command=Way2021)
btn1.place(relx=0.18,rely=0)
btn2.place(relx=0.32,rely=0)
btn3.place(relx=0.48,rely=0)
btn4.place(relx=0.64,rely=0)
btn5.place(relx=0.80,rely=0)
btn1.config(image=img1)
btn2.config(image=photo)
btn3.config(image=img3)
btn4.config(image=photo2)
btn5.config(image=photo3)

#------------------------------------(樂天桃猿)
btn6=tk.Button(win1,text="2021年",command=Monkey2021)
btn7=tk.Button(win1,text="2020年",command=Monkey2020)
btn8=tk.Button(win1,text="2019年",command=Monkey2019)
btn9=tk.Button(win1,text="2018年",command=Monkey2018)
btn10=tk.Button(win1,text="2017年",command=Monkey2017)
btn6.place(relx=0.18,rely=0.185)
btn7.place(relx=0.22,rely=0.185)
btn8.place(relx=0.26,rely=0.185)
btn9.place(relx=0.195,rely=0.215)
btn10.place(relx=0.235,rely=0.215)
#------------------------------------(富邦悍將)
btn11=tk.Button(win1,text="2021年",command=FB2021)
btn12=tk.Button(win1,text="2020年",command=FB2020)
btn13=tk.Button(win1,text="2019年",command=FB2019)
btn14=tk.Button(win1,text="2018年",command=FB2018)
btn15=tk.Button(win1,text="2017年",command=FB2017)
btn11.place(relx=0.32,rely=0.25)
btn12.place(relx=0.36,rely=0.25)
btn13.place(relx=0.4,rely=0.25)
btn14.place(relx=0.34,rely=0.279)
btn15.place(relx=0.38,rely=0.279)
#------------------------------------(統一獅)
btn16=tk.Button(win1,text="2021年",command=Seven2021)
btn17=tk.Button(win1,text="2020年",command=Seven2020)
btn18=tk.Button(win1,text="2019年",command=Seven2019)
btn19=tk.Button(win1,text="2018年",command=Seven2018)
btn20=tk.Button(win1,text="2017年",command=Seven2017)
btn16.place(relx=0.48,rely=0.201)
btn17.place(relx=0.52,rely=0.201)
btn18.place(relx=0.56,rely=0.201)
btn19.place(relx=0.5,rely=0.232)
btn20.place(relx=0.54,rely=0.232)
#------------------------------------(中信兄弟)
btn21=tk.Button(win1,text="2021年",command=ChunShin2021)
btn22=tk.Button(win1,text="2020年",command=ChunShin2020)
btn23=tk.Button(win1,text="2019年",command=ChunShin2019)
btn24=tk.Button(win1,text="2018年",command=ChunShin2018)
btn25=tk.Button(win1,text="2017年",command=ChunShin2017)
btn21.place(relx=0.64,rely=0.202)
btn22.place(relx=0.68,rely=0.202)
btn23.place(relx=0.72,rely=0.202)
btn24.place(relx=0.66,rely=0.232)
btn25.place(relx=0.699,rely=0.232)
#------------------------------------(味全龍)
btn26=tk.Button(win1,text="2021年",command=Way2021)
btn26.place(relx=0.833,rely=0.145)

#------------------------------------以上為第一頁編輯內容
#------------------------------------第二頁
canvas2=tk.Canvas(tab2,width=1290,height=900,bd=0, highlightthickness=0)
imgpath2 = 'base.gif'
img_tab = PIL.Image.open(imgpath2)
photo_9 = ImageTk.PhotoImage(img_tab)
canvas2.create_image(645,482, image=photo_9)
canvas2.pack()
lb_=tk.Label(tab2,text="請輸入想搜尋的球員")
lb_.config(bg="#14FF3C",fg="#FF6929",font=("微軟正黑體", 15,"bold"))
lb_.place(relx=0,rely=0)
en=tk.Entry(tab2)
en.place(relx=0.15,rely=0)
win.mainloop()

