import { useState } from "react";
import Header from "./components/Header";
import CategoryBar from "./components/CategoryBar";
import Banner from "./components/Banner";
import ProductList from "./components/ProductList";
import Footer from "./components/Footer";

function App() {
  const [cartCount, setCartCount] = useState(0);
  const [selectedCategory, setSelectedCategory] = useState("All");
  const [showCart, setShowCart] = useState(false);
  const [showLogin, setShowLogin] = useState(false);
  const [toast, setToast] = useState(false);

  const handleAddToCart = () => {
    setCartCount(prev => prev + 1);
    setToast(true);
    setTimeout(() => setToast(false), 2000);
  };

  return (
    <>
      <Header
        cartCount={cartCount}
        setShowCart={setShowCart}
        setShowLogin={setShowLogin}
      />

      <CategoryBar setSelectedCategory={setSelectedCategory} />
      <Banner />

      <ProductList
        selectedCategory={selectedCategory}
        handleAddToCart={handleAddToCart}
      />

      <Footer />

      {toast && <div className="toast">Added to Cart!</div>}

      {showCart && (
        <div className="cart-drawer">
          <h3>Your Cart</h3>
          <p>{cartCount} items added</p>
          <button onClick={() => setShowCart(false)}>Close</button>
        </div>
      )}

      {showLogin && (
        <div className="modal">
          <div className="modal-content">
            <h3>Login</h3>
            <input placeholder="Email" />
            <input placeholder="Password" type="password" />
            <button>Login</button>
            <button onClick={() => setShowLogin(false)}>Close</button>
          </div>
        </div>
      )}
    </>
  );
}

export default App;
