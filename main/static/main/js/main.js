async function getProducts() {
    return fetch("/get-product").then((res) => res.json())
}

async function refreshProducts() {
    const products = await getProducts()
    let htmlString = ``
    products.forEach((item) => {
        htmlString += 
        `
        
        <a href="" class="product-box-a">
            <div class="product-box">
                <img src='${item.fields.photo_url}' alt="">

                <div class="product-information" >
                    <p>${item.fields.name}</p>
                    <p>Rp.${item.fields.price}</p>
                    <div class="review-container">
                        <img src="https://cdn-icons-png.flaticon.com/512/2107/2107957.png" style="max-width: 12px; max-height: 12px;margin-top: 18px;">
                        <p>${item.fields.rating} | </p>
                        <p>${item.fields.amount} stok</p>
                    </div>
                </div>

                <div class="change-amount-btn">
                    <a href="/decrease_amount/${item.pk}">
                        <i class="fa fa-minus" style="font-size:24px;color: black;"></i>
                    </a>
                    <a href="/increase_amount/${item.pk}">
                        <i class="fa fa-plus" style="font-size:24px;color: black;"></i>
                    </a>
                    <a href="/remove_item/${item.pk}">
                        <i class="fa fa-trash" style="font-size:24px;color: black;"></i>
                    </a>
                </div>
            </div>
        </a>\n
        
        `
    })
    
    document.getElementById("product_table").innerHTML = htmlString
}

refreshProducts()

function addProduct() {
    fetch("create-product-ajax/", {
        method: "POST",
        body: new FormData(document.querySelector('#form'))
    }).then(refreshProducts)

    document.getElementById("form").reset()
    return false
}
document.getElementById("button_add").onclick = addProduct