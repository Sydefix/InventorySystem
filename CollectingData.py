
from openpyxl import load_workbook
import json

wb = load_workbook('MC-40 22C01.xlsx')
sheet = wb['sheet1']

royal_dict = {}

def getvalue(sheet, col): 
    return sheet[cell.coordinate.replace('B',col)].value

current_cell: str = ""



for anycategory in sheet.iter_cols(min_row=2, min_col=2, max_col=2, max_row=139):
    for cell in anycategory:
        inner_royal_dict = {}
        middle_royal_dict = {}

        if cell.value is not None:
            current_cell = cell.value
        
        getvalue = lambda col: sheet[cell.coordinate.replace('B',col)].value 
        print(f"processing: {current_cell} <---> {getvalue('C')}")
        
        

        inner_royal_dict["QuantityPerCTN"] = getvalue("D")
        inner_royal_dict["CTN"] = getvalue("E")
        inner_royal_dict["RMB"] = getvalue("F")
        inner_royal_dict["Douane"] = getvalue("G")
        inner_royal_dict["Transport"] = getvalue("H")
        inner_royal_dict["Total"] = getvalue("I")

        middle_royal_dict[getvalue('C')] = inner_royal_dict
        royal_dict[current_cell] = middle_royal_dict 
                    #         "QuantityPerCTN": getvalue("D"), #D
                    # "CTN": getvalue("E"), #E
                    # "RMB": getvalue("F"), #F
                    # "Douane": getvalue("G"), #G
                    # "Transport": getvalue("H"), #H 
                    # "Total": getvalue("I"), #I
        # royal_dict[current_cell] = {
        #     getvalue("C"): {
        #             "QuantityPerCTN": getvalue("D"), #D
        #             "CTN": getvalue("E"), #E
        #             "RMB": getvalue("F"), #F
        #             "Douane": getvalue("G"), #G
        #             "Transport": getvalue("H"), #H 
        #             "Total": getvalue("I"), #I
        #     }
        # }
        

          


        # royal_dict[current_cell][getvalue('C')] = {}

        # if loadimage.image_in(cell.coordinate.replace("B", "A")):
        #     #error if there is no folder
        #     tmp = loadimage.get(cell.coordinate.replace("B", "A")).save("assets/"+ cell.value + ".png")
        #     print("Got it!") 

final_result = json.dumps(royal_dict, indent=4)
print(final_result)

# Serializing json
final_result = json.dumps(royal_dict, indent=4)

# Writing to sample.json
with open("MC-40 22C01.json", "w") as outfile:
    outfile.write(final_result)

# {
#     "category": { #B
#             "subcategory": { #C
#                 "QuantityPerCTN": 0, #D
#                 "CTN": 0, #E
#                 "RMB": 0, #F
#                 "Douane": 0, #G
#                 "Transport": 0, #H 
#                 "Total": 0, #I

#         }
#     }
# }

# """
# var.category
# for row in sheet:
#     if B is None:
#         category = var.category
#         var["category"] = {"subcategory": {quantity = D, CTN= E, RMB = F, ...}}
        
# """

# {
#     "category": {"subcategory": ["QuantityPerCTN", "CTN", "RMB", "Douane", "Transport", "Total"], "subcategory": [""]},
#     "category": {"subcategory": [""], "subcategory": [""]},
# }

# {
#     "category": [["subcategory", ""], ["subcategory", ""]],
#     "category": [["subcategory", ""], ["subcategory", ""]],
# }



