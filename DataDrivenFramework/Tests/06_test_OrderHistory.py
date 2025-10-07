from DataDrivenFramework.pages.Base import BasePage
from DataDrivenFramework.pages.OrderHistory import OrderHistory


def test_orderHistory(logged_in_context):
    page = logged_in_context.new_page()
    page.goto("https://rahulshettyacademy.com/client/#/dashboard/dash")

    base_obj=BasePage(page)
    # click on orders
    base_obj.go_to_order()
    page.wait_for_selector("thead th")  # or a more specific selector like ".table-responsive"

    # getting table headers-columns
    obj_history=OrderHistory(page)
    text=obj_history.orderTable()
    print("columns are :", text)
# getting first row of history table
    row_text=obj_history.getFirstRow()
    print("first row values are :", row_text)
#clicking on view & getting thank you text
    text_value=obj_history.viewClick()
    print("clicking on view is success:", text_value)





