# -*- coding: utf-8 -*
'''
Created on 2015-5-26

@author: 胡晓燕
'''
from __future__ import division
# 费率计算方法
# 计算当前本金和当期利息和月还款额，和剩余本金
#参数说明
# contractMoney,合同金额
#irrate，月利率
#period,分期
#surplusPrincipal,剩余本金
#amortizedInterest，当期利息
#amortizedPrincipal，当前本金
#periodMoney ，月还款额

# 等本等息的剩余本金，当期还款利息，当期还款本金，月还款额
def periodSchedulebycontract(contractMoney,irrate,period):
    surplusPrincipal=contractMoney
    surplusPrincipallist=[]
    amortizedPrincipal=round(float(contractMoney)/period,2)
    amortizedInterest=round(contractMoney*irrate,2)
    periodMoney=round(amortizedPrincipal+amortizedInterest,2)#等本等息月还款额
    for i in range(period):
        surplusPrincipal=round(surplusPrincipal-float(contractMoney)/period,2)
        surplusPrincipallist.append(surplusPrincipal)
    return periodMoney,surplusPrincipallist,amortizedInterest,amortizedPrincipal
#等额本息的剩余本金，当期还款利息，当期还款本金，月还款额
def periodSchedulebycontract1(contractMoney,irrate,period):
    periodMoney=contractMoney*irrate*pow(1+irrate,period)/(pow(1+irrate,period)-1)
    surplusPrincipal=contractMoney
    surplusPrincipallist=[]
    amortizedInterestlist=[]
    amortizedPrincipallist=[]
    for i in range(period):
        amortizedInterest=round(surplusPrincipal*irrate,2)
        amortizedPrincipal=round(periodMoney-amortizedInterest,2)
        surplusPrincipal=round(surplusPrincipal-amortizedPrincipal,2)
        surplusPrincipallist.append(surplusPrincipal)
        amortizedInterestlist.append(amortizedInterest)
        amortizedPrincipallist.append(amortizedPrincipal)
    return round(periodMoney,2),surplusPrincipallist,amortizedInterestlist,amortizedPrincipallist
#等额本金的剩余本金，当期还款本金，当期还款利息，月还款额
def periodSchedulebycontract2(contractMoney,irrate,period):
    surplusPrincipal=contractMoney
    surplusPrincipallist=[]
    amortizedInterestlist=[]
    amortizedPrincipallist=[]
    periodmoneylist=[]
    for i in range(period):
        amortizedInterest=round(surplusPrincipal*irrate,2)
        amortizedPrincipal=round(float(contractMoney/period),2)
        surplusPrincipal=round(surplusPrincipal-amortizedPrincipal,2)
        periodmoney=round(amortizedPrincipal+amortizedInterest,2)
        if i==period-1:
           surplusPrincipal=0.0
        surplusPrincipallist.append(surplusPrincipal)
        amortizedInterestlist.append(amortizedInterest)
        amortizedPrincipallist.append(amortizedPrincipal)
        periodmoneylist.append(periodmoney)

    return periodmoneylist,surplusPrincipallist,amortizedInterestlist,amortizedPrincipallist
# print x[0][1],x[1][1],x[2][1]
# 付息通的剩余本金，当期还款本金，当期还款利息，月还款额
def periodSchedulebycontract3(contractMoney,irrate,period):
    surplusPrincipal=contractMoney
    surplusPrincipallist=[]
    amortizedInterestlist=[]
    amortizedPrincipallist=[]
    periodmoneylist=[]
    for i in range(period):
        # 最后一个月
        if i==period-1:
          amortizedInterest=round(contractMoney*irrate,2)
          amortizedPrincipal=round(contractMoney,2)
          surplusPrincipal=round(0,2)
          periodmoney=amortizedInterest+amortizedPrincipal
        else:
          amortizedInterest=round(contractMoney*irrate,2)
          amortizedPrincipal=round(0,2)
          surplusPrincipal=round(contractMoney,2)
          periodmoney=amortizedInterest
        surplusPrincipallist.append(surplusPrincipal)
        amortizedInterestlist.append(amortizedInterest)
        amortizedPrincipallist.append(amortizedPrincipal)
        periodmoneylist.append(periodmoney)
    return periodmoneylist,surplusPrincipallist,amortizedInterestlist,amortizedPrincipallist

#助农贷

#月利息：contract*irr
#最后一期还款额contract*irr+contract

# print periodSchedulebycontract3(20000,0.0097942594806015,12)






