console.log("sanity check!!")

//new
//get publishable key
fetch("/config")
.then((result) => { return result.json(); })
.then((data) => {
    //init stripe .js
    const stripe = Stripe(data.publicKey);

    //new event handler
    let submitBtn = document.querySelector('#submitBtn');
    if (submitBtn != null) {
        submitBtn.addEventListener("click", () => {
            //get the checkout session id
            fetch("/create-checkout-session/")
            .then((result) => { return result.json(); })
            .then((data) => {
                console.log(data);
                //redirect to stripe checkout
                return stripe.redirectToCheckout({sessionId: data.sessionId})
            })
            .then((res) => {
                console.log(res);
            });
        });
    }
});