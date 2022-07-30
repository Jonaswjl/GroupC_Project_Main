import api, cash_on_hand,overheads,profit_loss
from pathlib import Path
def main(): 
    api.api_function()
    overheads.overhead_function()
    cash_on_hand.coh_function()
    profit_loss.profitloss_function()

i = api.api_function()
file_path=  Path.cwd()/"Summary_report.txt"
file_path.touch()
with file_path.open(mode="w", encoding = "UTF-8") as file: 
    file.writelines(i)
