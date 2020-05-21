function reloadCart() {

    const request = new XMLHttpRequest();
    request.open('GET', `/api/v1/cart-text/`);
    request.setRequestHeader('Accept', 'application/json');
    request.setRequestHeader('Content-Type', 'application/json');
    request.onload = () => {
        if ( request.status == 200 ) {
            const response = JSON.parse(request.responseText);

            var cartTable = document.getElementById("cart-table");
            cartTable.innerHTML = "";
            var total_price = 0.0;
            for ( let item of response) {
                total_price = total_price + parseFloat(item.price);
                var tr = document.createElement("tr");
                tr.setAttribute("id", item.id);


                var td1 = document.createElement("td");
                td1.appendChild( document.createTextNode(`${item.item_category} - ${item.item_name}`));
                tr.appendChild(td1);

                var td2 = document.createElement("td");
                for ( let topping of item.toppings ) {
                    td2.appendChild( document.createTextNode(`${topping.name}, `));
                }
                tr.appendChild(td2);

                var td3 = document.createElement("td");
                td3.appendChild( document.createTextNode(`$ ${item.price}`));
                tr.appendChild(td3);

                var td4 = document.createElement("td");
                var removeButton = document.createElement("span");
                removeButton.setAttribute("value", item.id);
                removeButton.setAttribute("class", "cart-remove material-icons");
                removeButton.appendChild( document.createTextNode("remove_circle"));
                removeButton.onclick = function () {
                    removeFromCart(item.id)
                }
                td4.appendChild( removeButton);
                tr.appendChild(td4);

                cartTable.appendChild(tr);
            }
    
            var tr = document.createElement("tr");
            total_price = total_price.toFixed(2);
            tr.innerHTML = `<td></td><td>Total:</td><td>$ ${total_price}</td><td></td>`;
            cartTable.appendChild(tr);
            

        } else {
            M.toast({html: 'Could not refresh cart'});
        }
    }
    request.send();
}

function addToCart(item, toppings=false) {

    var csrftoken = getCookie('csrftoken');

    const request = new XMLHttpRequest();
    request.open('POST', `/api/v1/cart/`);
    request.setRequestHeader('X-CSRFToken', csrftoken);
    request.setRequestHeader('Accept', 'application/json');
    request.setRequestHeader('Content-Type', 'application/json');
    request.onload = () => {
        const response = request.responseText;
        if ( request.status == 202 & toppings == false ) {
            modals['toppings'].open();
            toppings = getToppings(item);
            
            console.log("202 returned!");
        } else if ( request.status == 200 ) {
            console.log("200");
            console.log(response);
            M.toast({html: 'Item added to cart!'});
        } else {
            console.log("Error");
            M.toast({html: 'Something went wrong..'});
            console.log(response);
        }
    }
    let data = JSON.stringify({'item':item, 'toppings':toppings});
    request.send(data);

    setTimeout(function(){
        reloadCart();
    }, 200);

    return false;
};

function removeFromCart(itemId) {

    var csrftoken = getCookie('csrftoken');
    
    const request = new XMLHttpRequest();
    request.open('DELETE', `/api/v1/cart/${itemId}`);
    request.setRequestHeader('X-CSRFToken', csrftoken);
    request.setRequestHeader('Accept', 'application/json');
    request.setRequestHeader('Content-Type', 'application/json');
    request.onload = () => {
        const response = request.responseText;
        if ( request.status == 200 ) {
            console.log(response);
            M.toast({html: 'Item removed from cart!'});
        } else {
            M.toast({html: 'Something went wrong..'});
        }
    }
    request.send();

    setTimeout(function(){
        reloadCart();
    }, 100);
}

function getToppings(itemId) {

    const request = new XMLHttpRequest();
    request.open('GET', `/api/v1/toppings/${itemId}`);
    request.setRequestHeader('Accept', 'application/json');
    request.setRequestHeader('Content-Type', 'application/json');
    request.onload = () => {
        const response = request.responseText;
        if ( request.status == 200 ) {
            populateToppingsToModal( JSON.parse(response) );
            document.getElementById('toppingsAdd').dataset['productid'] = itemId;

        } else {
            M.toast({html: 'Something went wrong..'});
        }
    }
    request.send();

    setTimeout(function(){
        reloadCart();
    }, 100);
}

function populateToppingsToModal(toppings) {

    option_form = document.getElementById('toppings-form');
    option_form.innerHTML = "";
    for (topping of Object.values(toppings)) {
        var option = document.createElement('p');
        option.innerHTML = `<label><input type="checkbox" class="" value="${topping.id}" /><span>${topping.name} ($${topping.price})</span></label>`;    
        option_form.appendChild(option);
    }
}

function getSelectedToppings() {
    var array = []
    var checkboxes = document.querySelectorAll('input[type=checkbox]:checked')

    for (var i = 0; i < checkboxes.length; i++) {
    array.push(checkboxes[i].value)
    }

    return array;
}

function completeOrder() {

    var csrftoken = getCookie('csrftoken');

    const request = new XMLHttpRequest();
    request.open('POST', `/api/v1/order/`);
    request.setRequestHeader('X-CSRFToken', csrftoken);
    request.setRequestHeader('Accept', 'application/json');
    request.setRequestHeader('Content-Type', 'application/json');
    request.onload = () => {
        const response = request.responseText;
        if ( request.status == 200 ) {
            M.toast({html: 'Order submitted!'});
        } else {
            M.toast({html: 'Something went wrong..'});
        }
    }
    request.send();

    setTimeout(function(){
        reloadCart();
    }, 100);
    
    reloadCart();

}

// Gets an item from the cookie, e.g. the CSRF token for submitting AJAX requests
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// Not used
function ajax(url) {
    return new Promise(function(resolve, reject) { 
        var xhr = new XMLHttpRequest();
        xhr.onload = function () {
            resolve(this.responseText);
        }
        xhr.onerror = reject;
        xhr.open('GET', url);
        xhr.send();
    })
}
