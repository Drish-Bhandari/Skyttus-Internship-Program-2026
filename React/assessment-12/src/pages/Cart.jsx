import { useCart } from "../context/CartContext";

function Cart() {
  const {
    cart,
    removeFromCart,
    increaseQty,
    decreaseQty,
    total,
  } = useCart();

  if (cart.length === 0) {
    return <h2 className="empty">Your cart is empty 🛒</h2>;
  }

  return (
    <div className="cart-container">
      <div className="cart-items">
        {cart.map((item) => (
          <div key={item.id} className="cart-item">
            <div>
              <h3>{item.title}</h3>
              <p>${item.price}</p>

              <div className="qty-control">
                <button onClick={() => decreaseQty(item.id)}>-</button>
                <span>{item.quantity}</span>
                <button onClick={() => increaseQty(item.id)}>+</button>
              </div>
            </div>

            <button
              className="remove-btn"
              onClick={() => removeFromCart(item.id)}
            >
              Remove
            </button>
          </div>
        ))}
      </div>

      <div className="cart-summary">
        <h3>Total: ${total.toFixed(2)}</h3>
        <button className="checkout-btn">
          Proceed to Checkout
        </button>
      </div>
    </div>
  );
}

export default Cart;