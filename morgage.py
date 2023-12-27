import numpy as np
import matplotlib.pyplot as plt


# mortgage variables
YearRate = 4.15 / 100 
HousePrice = 535000 
Years = 29 #number of years in mortgage
n = 12 #number of month in a year thus number a payments in a year
MtgeAmt = HousePrice * 0.9

#MtgeAmt = 486495
FixedAddPayment = 300 #fixed additional payment per month
FirstOverPay=1 #first month to start overpay
LastOverPay=61 #month to stop overpay (not inclusive)

MonthlyRate = round(YearRate / 12, 6)
MonthlyPayment = round((MtgeAmt * MonthlyRate) / (1 - (1+ MonthlyRate)**(-abs(n*Years))), 0)
print(MonthlyPayment)

# create a list of Interest payments due in monthly payment
InterestPayments = np.zeros(n*Years)
# create a list of Mortgage due after month in 30 years
MtgeLeft = np.zeros(n*Years+1)
# create a list of Mortgage repayment part in monthly payment
MtgePaidMonthly = np.zeros(n*Years)
 
MtgeLeft[0] = MtgeAmt


LastMonth = 360

for i in range(1, n*Years+1):

    InterestPayments[i-1] = round(MtgeLeft[i-1] * MonthlyRate,0)

    MtgePaidMonthly[i-1] = round(MonthlyPayment - InterestPayments[i-1], 0)

    if i in range(FirstOverPay,LastOverPay):

        MtgePaidMonthly[i-1]  = MtgePaidMonthly[i-1]  + FixedAddPayment

        #print(i, MtgePaidMonthly[i-1])

    MtgeLeft[i] = MtgeLeft[i-1] - MtgePaidMonthly[i-1]

    if MtgeLeft[i] < 0:

        MtgeLeft[i] = 0

        MtgePaidMonthly[i-1] = 0

        if LastMonth == 360:

            LastMonth = i

    print(i, MtgeLeft[i-1], InterestPayments[i-1], MtgePaidMonthly[i-1])

 

print(MtgeLeft)
print(InterestPayments)
print(MtgePaidMonthly)


#MtgeLeftArr = MtgeLeft.reshape(Years,n)

InterestPaymentsArr = InterestPayments.reshape(Years,n)
MtgePaidMonthlyArr = MtgePaidMonthly.reshape(Years,n)

#print(InterestPaymentsArr)
#print(MtgePaidMonthlyArr)

x = np.arange(0, n*Years+1, 1)
fig = plt.figure(figsize=(9,3.8),dpi=200)
ax1 = fig.add_subplot(121)

 
ax1.plot(x, MtgeLeft, 'r') # 'r' is the color red
ax1.set_title('График погашения, срок ' f"{Years}" ' лет, мес.платеж = ' f"{MonthlyPayment}" '\n' 'последний месяц ' f"{LastMonth}")
ax1.set_xlabel('Time, month')
ax1.set_ylabel('Mtge left')

#TODO: add a plot of InterestPaymentsArr and MtgePaidMonthlyArr
#TODO: print when mortgage will be repaid in full (MtgeLeft < 0) - use position in MtgeLeft where it becomes 0
#TODO: print mortgage monthly payment
#TODO: pie chart for mortgage overview - how much to pay, what part is interest, what part is repayment
MtgePaid = sum(MtgePaidMonthly)
InterestPaid = sum(InterestPayments)
print(MtgePaid, InterestPaid)
y = np.array([MtgePaid, InterestPaid])
ax2 = fig.add_subplot(122)
ax2.set_title('Обзор ипотеки')
 
ax2.pie(y, labels=['MtgePaid' f" - {MtgePaid}", 'InterestPaid' f" - {InterestPaid}"], autopct='%1.1f%%')
#ax2.legend( bbox_to_anchor=(0.8, 1.0))
#manager = plt.get_current_fig_manager()
#manager.resize(*manager.window.maxsize())
plt.show()
#TODO: Add list for Lump sum redemption
#TODO: Implement Lump sum into Mtge payment arrays (add Lump sum to MtgePaidMonthly)
#TODO: Rework to ask params before running code
#TODO: add sliders for Mtge years and amount, so charts are interactive
#TODO: think how to divide code to functions (calc morgage, plot graphs, etc.)
#TODO: implement interactive charts via plotly