import { Routes, Route, Link } from "react-router-dom";
import Home from "./pages/Home";
import ProductDetails from "./pages/ProductDetails";
import Cart from "./pages/Cart";
import { useCart } from "./context/CartContext";

function App() {
  const { cart, message } = useCart();

  return (
    <>
      <nav className="navbar">
        <Link to="/">Home</Link>
        <Link to="/cart" className="cart-link">
          Cart <span className="cart-badge">{cart.length}</span>
        </Link>
      </nav>

      {message && <div className="toast">{message}</div>}

      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/product/:id" element={<ProductDetails />} />
        <Route path="/cart" element={<Cart />} />
      </Routes>
    </>
  );
}

export default App;