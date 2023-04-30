sales_data = [(10000, "January"), (15000, "February"), (12000, "March"), (18000, "April"),
              (20000, "May"), (14000, "June"), (16000,
                                                "July"), (17000, "August"), (13000, "September"),
              (11000, "October"), (19000, "November"), (22000, "December")]

month_with_highest_revenue = sales_data[0]
month_with_lowest_revenue = sales_data[0]
average_revenue_per_month = 0
total_annual_revenue = 0


def update_month_with_highest_revenue(revenue, month):
    global month_with_highest_revenue
    highest_revenue, highest_month = month_with_highest_revenue
    if highest_revenue >= revenue:
        return
    else:
        month_with_highest_revenue = (revenue, month)


def update_month_with_lowest_revenue(revenue, month):
    global month_with_lowest_revenue
    lowest_revenue, lowest_month = month_with_lowest_revenue
    if lowest_revenue <= revenue:
        return
    else:
        month_with_lowest_revenue = (revenue, month)


def update_total_annual_revenue(revenue):
    global total_annual_revenue
    total_annual_revenue += revenue


def average_revenue(total_revenue):
    return round(total_revenue / len(sales_data))


def analyze(sales_data):
    global average_revenue_per_month
    for revenue, month in sales_data:
        update_month_with_lowest_revenue(revenue, month)
        update_month_with_highest_revenue(revenue, month)
        update_total_annual_revenue(revenue)

    average_revenue_per_month = average_revenue(total_annual_revenue)


# analyze sales data
analyze(sales_data)
print("Total revenue for the year: $", total_annual_revenue)
print("Average revenue per month: $", average_revenue_per_month)
print("Month with the highest revenue:", month_with_highest_revenue[1])
print("Month with the lowest revenue:", month_with_lowest_revenue[1])
