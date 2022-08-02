import api, cash_on_hand,overheads,profit_loss
from pathlib import Path

forex = api.rate_function()
a = api.api_function()
b = overheads.overhead_function(forex)
c = cash_on_hand.coh_function(forex)
d = profit_loss.profitloss_function(forex)

file_path=  Path.cwd()/"Summary_report.txt"
file_path.touch()
with file_path.open(mode="w", encoding = "UTF-8") as file: 
    file.write(a)
    file.write("\n")
    file.write(b)
    file.write("\n")
    file.writelines(c)
    file.write("\n")
    file.writelines(d)

