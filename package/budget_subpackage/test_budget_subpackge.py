from freemembership import FreeMemberShip
from basicmembership import BasicMembership
from premiummembership import PremiumMembership

def testing_budget():
    #Free membership
    free_mem1=FreeMemberShip(25000)
    free_mem1.add_amount(1500)

    #Basic membership
    basic_mem1=BasicMembership()
    annual=basic_mem1.analysis_and_suggestion()
    free_mem2 =FreeMemberShip(annual)
    free_mem2.add_amount(30)

    #Premium membership
    premium_mem1=PremiumMembership()
    premium_mem1.expenditure_chart()
    annual=premium_mem1.analysis_and_suggestion()
    free_mem3=FreeMemberShip(annual)
    free_mem3.add_amount(500)
    
testing_budget()

