
from unicodedata import category

from openpyxl import load_workbook

wb = load_workbook('MC-40 22C01.xlsx')
sheet = wb['sheet1']



current_cell: str = ""
for anycategory in sheet.iter_cols(min_row=2, min_col=2, max_col=2, max_row=139):
    for cell in anycategory:
        if cell.value is not None:
            current_cell = cell.value
        print(f"processing: {current_cell} <---> {sheet[cell.coordinate.replace('B','C')].value}") 
        # if loadimage.image_in(cell.coordinate.replace("B", "A")):
        #     #error if there is no folder
        #     tmp = loadimage.get(cell.coordinate.replace("B", "A")).save("assets/"+ cell.value + ".png")
        #     print("Got it!")


{
    "category": { #B
            "subcategory": { #C
                "QuantityPerCTN": 0, #D
                "CTN": 0, #E
                "RMB": 0, #F
                "Douane": 0, #G
                "Transport": 0, #H 
                "Total": 0, #I

        }
    }
}
"""
var.category
for row in sheet:
    if B is None:
        category = var.category
        var["category"] = {"subcategory": {quantity = D, CTN= E, RMB = F, ...}}
        
"""

{
    "category": {"subcategory": ["QuantityPerCTN", "CTN", "RMB", "Douane", "Transport", "Total"], "subcategory": [""]},
    "category": {"subcategory": [""], "subcategory": [""]},
}

{
    "category": [["subcategory", ""], ["subcategory", ""]],
    "category": [["subcategory", ""], ["subcategory", ""]],
}



