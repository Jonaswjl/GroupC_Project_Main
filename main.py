import api, cash_on_hand,overheads,profit_loss
from pathlib import Path

a = api.api_function()
b = overheads.overhead_function()
c = cash_on_hand.coh_function()
d = profit_loss.profitloss_function()

file_path=  Path.cwd()/"Summary_report.txt"
file_path.touch()
with file_path.open(mode="w", encoding = "UTF-8",newline="\n") as file: 
    file.write(a)
    file.write("\n")
    file.write(b)
    file.write("\n")
    file.writelines(c)
    file.write("\n")
    file.writelines(d)

