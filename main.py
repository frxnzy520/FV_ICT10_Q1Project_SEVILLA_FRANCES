from pyscript import display, document


def generate_sku(e):

    document.getElementById("result").innerHTML = " "

    category = document.getElementById("category").value
    product_name = document.getElementById("product").value
    stock_qty = document.getElementById("quantity").value

    SKU = category[:3].upper() + "-" + product_name[:4].upper() + "-" + str(stock_qty)

    display("SKU: " + SKU, target="result")