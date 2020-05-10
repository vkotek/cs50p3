document.addEventListener('DOMContentLoaded', (event) => {
    console.log("eshop.js loaded.");

});

function addToCart(item) {
    cartview = document.getElementById("cart"); 
    console.log(item);
    const request = new XMLHttpRequest();
    request.open('GET', `/api/v1/cart/${id}`);
    request.onload = () => {
        const response = request.responseText;
        console.log(response);
    }
};


var helpers = {
    itemData: function (object) {
        var item = {
            name = object.getAttribute('data-name'),
            
        }
    }
}

function displayCart() {
    console.log("Refreshing cart..")
    var cart = localStorage.getItem('cart');
    cart = JSON.parse(cart);

    cartview = document.getElementById("cart");
    cartview.innerHTML = "";
    for ( let item in cart) {
        var newitem = document.createElement("LI");
        newitem.value = item;
        newitem.innerHTML = getProductById(item);
        cartview.appendChild(newitem);
    }
 };

 function getProductById(id) {
    const request = new XMLHttpRequest();
    request.open('GET', `/api/v1/menuitems/${id}`)
    request.onload = () => {
        const response = request.responseText;
        console.log(response);
        return response;
    }
    request.send();
 };