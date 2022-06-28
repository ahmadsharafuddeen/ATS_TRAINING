import pandas as pd

# create list of lists
# each salesperson passes in a slip for each different type of product sold
sales_persons = [
    [['S01', 'P01', 5], ['S01', 'P02', 3], ['S01', 'P01', 2], ['S01', 'P03', 9], ['S01', 'P03', 2], ['S01', 'P04', 3]],
    [['S02', 'P01', 4], ['S02', 'P02', 7], ['S02', 'P01', 9], ['S02', 'P03', 3], ['S02', 'P03', 7], ['S02', 'P04', 2]],
    [['S03', 'P01', 5], ['S03', 'P02', 8], ['S03', 'P01', 3], ['S03', 'P03', 9], ['S03', 'P03', 5], ['S03', 'P04', 5]],
    [['S04', 'P01', 8], ['S04', 'P02', 6], ['S04', 'P01', 2], ['S04', 'P03', 5], ['S04', 'P03', 1], ['S04', 'P04', 9]]
]
sales = [{}, {}, {}, {}]

# TODO: 
count = 0
for sales_person in sales_persons:
    for item in sales_person:
        sales_id = sales[count]
        sales_id.setdefault(item[0], {}) 
        sales_id[item[0]].setdefault(item[1], 0)
        sales_id[item[0]][item[1]] += item[2]
    count += 1
# print(sales)

reformat = {}
counter = 0
for item in sales:
    for id in item:
        arr = sales[counter][id]
        new = list(arr.values())
        reformat[id] = new
        counter += 1

print(reformat)


# pprint.pprint(reformat)
df  = pd.DataFrame(reformat, index=['P01', 'P02', 'P03', 'P04'])
df.loc["Sales Sum"] = [df['S01'].sum(), df['S02'].sum(), df['S03'].sum(), df['S04'].sum()]
df['P_SUM'] = df.sum(axis=1)
print(df)

# print(pd_table)
