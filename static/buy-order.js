let btn = document.getElementById("buyBtn");
let id = window.location.pathname.replace("/order/", "");
btn.onclick = function(){
  let stripe = fetch("/config/")
    .then((result) => { return result.json(); })
    .then((data) => {
      // Initialize Stripe.js
      return Stripe(data.key);
    });
  fetch("/buy-order/" + id)
    .then((result) => {return result.json(); })
    .then((data) => {
      console.log(stripe);
      stripe.then((a) => a.redirectToCheckout({sessionId: data.id}));
    })
    .then((res) => {console.log(res); });
}
