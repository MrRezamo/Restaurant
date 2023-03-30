from collections import OrderedDict

number = int(input("Please Enter your Number : "))
final_list = OrderedDict()
count = 0
while count <= number:
    item_name = input("Please Enter item name : ")
    net_price = float(input("Please Enter net price : "))
    # final_list[item_name] = net_price

    if item_name in final_list:
        final_list[item_name].append(net_price)
        sum_all = sum([sum(values) for values in final_list.values()])
        count += 1
    else:
        final_list[item_name] = [net_price]
    count += 1


print(final_list)
print(sum_all)
