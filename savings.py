import locale
locale.setlocale(locale.LC_ALL,'') #this allows use of currency


# these are the savings categories
emergency = 25000
camper = 80000
wedding = 60000
condo = 200000
stuLoans = 100000
truck = 75000
horses = 10000
loanS = 12000
savings = 0

#these are the income amounts
mikeWeekly = 35.60*40*(1-.32)
rhiWeekly = 22*40*(1-.32)
mikePerdiem = 1075 * (6/7)
rent = 550*12/52
totalIncome= mikeWeekly + rhiWeekly + rent

#these are the expense amounts
housing = 2000*12/52
internet = 150*12/52
phone = 90*12/52
loan = 500*12/52
stuLoan = 200*12/52
food = 200
animals = 50
carInsurance = 12000 / 52
totalExpenses = housing + internet + phone + loan + stuLoan + food + animals + carInsurance

netIncome = totalIncome - totalExpenses

#this defines the order of adding to savings
def savingsInc():         
    global emergency
    global camper
    global wedding
    global condo
    global stuLoans
    global truck
    global horses
    global savings
    global stuLoan
    global housing
    global internet
    global phone
    global loan
    global loanS
    global animals
    global food
    global carInsurance

    if loanS > loan:
        loanS -= loan
    elif loanS > 0:
        loan -= (loan - loanS)
        loanS -= loan
    else:
        loan = 0
        totalExpenses == housing + internet + phone + loan + stuLoan + food + animals + carInsurance
    if stuLoans > stuLoan:
        stuLoans -= .75*stuLoan
    elif stuLoans > 0:
        stuLoan -= (stuLoan - stuLoans)
        stuLoans -= stuLoan
    else:
        stuLoan = 0
        totalExpenses == housing + internet + phone + loan + stuLoan + food + animals + carInsurance
    if condo > (1200 * 12 / 52):
        condo -= .75*1200*12/52
    elif condo > 0:
        housing = ((500 * 12 /52) + condo)
        condo -= (housing - (500*12/52))
    else:
        housing = 500 * 12 / 52
        totalExpenses == housing + internet + phone + loan + stuLoan + food + animals + carInsurance
    if wedding > 0:
        if wedding > netIncome:
            wedding -= netIncome
        else:
            emergency -= (netIncome - wedding)
            wedding -= wedding
    elif emergency > 0 and condo > 0:
        if emergency > .5*netIncome:
            emergency -= .5*netIncome
            condo -=.5*netIncome
        else:
            condo -= (netIncome - emergency)
            emergency -= emergency
    elif condo > 0:
        if condo > netIncome:
            condo -= netIncome
        else:
            stuLoans -= (netIncome - condo)
            condo -= condo
    elif stuLoans > 0:
        if stuLoans > netIncome:
            stuLoans -= netIncome
        else:
            truck -= (netIncome - stuLoans)
            stuLoans -= stuLoans
    elif truck > 0:
        if truck > netIncome:
            truck -= netIncome
        else:
            horses -= (netIncome - truck)
            truck -= truck
    elif horses > 0:
        if horses > netIncome:
            horses -= netIncome
        else:
            savings += (netIncome - horses)
            horses -= horses
    else:
        savings += netIncome


def weekCalc(weeks):
    global mikePerdiem
    global netIncome
    global emergency
    global camper
    global condo
    global stuLoans
    global truck
    global horses
    global savings
    numberWk = 0
    while numberWk < weeks: #this is through June 2023 number should be 30
        if camper > 0:
            if camper > mikePerdiem:
                camper -= mikePerdiem
                savingsInc()
            else:
                changeIncome = mikePerdiem - camper
                netIncome = totalIncome - totalExpenses + changeIncome
                camper -= camper
                savingsInc()
                netIncome = totalIncome - totalExpenses
        else:
            if netIncome == totalIncome - totalExpenses:
                netIncome = totalIncome - totalExpenses + mikePerdiem
            savingsInc()
        numberWk += 1
    else:
        print('AFTER ' + str(numberWk) + ' weeks, this is how much we need: ' + '\n wedding: ' + str(locale.currency(wedding,grouping=True)) + '\n emergency: ' + str(locale.currency(emergency, grouping=True)) + '\n camper: ' 
        + str(locale.currency(camper, grouping=True)) + '\n condo: ' + str(locale.currency(condo, grouping=True)) + '\n student loans: ' + str(locale.currency(stuLoans,grouping=True)) +
        '\n truck: ' + str(locale.currency(truck, grouping=True)) + '\n horses: ' + str(locale.currency(horses,grouping=True)) + '\n Extra in savings: ' + str(locale.currency(savings,grouping=True)))

weekCalc(30)

while True: #this inputs the new income information to be calculated
    print('Is new income (h)ourly or (s)alary?')
    incomeType = input()
    print('What is your new income?')
    newIncome = int(input())
    if incomeType == 'h':
        rhiWeekly = int(newIncome) * 40 * (1-.32)
        totalIncome = rhiWeekly + mikeWeekly + rent
        netIncome = totalIncome - totalExpenses
        break
    elif incomeType == 's':
        rhiWeekly = int(newIncome) / 52 * (1-.32)
        totalIncome = rhiWeekly + mikeWeekly + rent
        netIncome = totalIncome - totalExpenses
        break
    else:
        continue

while True: #this decides whether to do totals by numWeeks or until all amounts completed
    print('Do you want to input (w)eeks or see (t)otal weeks to completion after school?')
    answer = input()
    if answer == 'w': #tracks savings after specified number of weeks
       print('Input number of weeks of savings (after school)') #add loop
       weekCalc (int(input()))
       break
    elif answer == 't': #tracks when all buckets are at 0 
        numberWk = 0
        while savings == 0: 
            if camper > 0:
                if camper > mikePerdiem:
                    camper -= mikePerdiem
                    savingsInc()
                else:
                    changeIncome = mikePerdiem - camper
                    netIncome = totalIncome - totalExpenses + changeIncome
                    camper -= camper
                    savingsInc()
                    netIncome = totalIncome - totalExpenses
            else:
                if netIncome == totalIncome - totalExpenses:
                    netIncome = totalIncome - totalExpenses + mikePerdiem
                savingsInc()
            numberWk += 1
        else:
            print('AFTER ' + str(numberWk+30) + ' weeks / ' + str((numberWk+30)/52) + ' years, we will meet all our financial goals AND have an extra ' + str(locale.currency(savings,grouping=True)) + ' in savings')
        break
    else:
        continue