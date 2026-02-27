import { useState } from "react";

function Header({ cartCount, setShowCart, setShowLogin }) {
  const [mega, setMega] = useState(false);

  return (
    <header className="header">
      <div
        className="logo"
        onMouseEnter={() => setMega(true)}
        onMouseLeave={() => setMega(false)}
      >
        amazon

        {mega && (
          <div className="mega-menu">
            <div>
              <h4>Electronics</h4>
              <p>Mobiles</p>
              <p>Laptops</p>
              <p>Headphones</p>
            </div>
            <div>
              <h4>Fashion</h4>
              <p>Men</p>
              <p>Women</p>
              <p>Shoes</p>
            </div>
            <div>
              <h4>Home</h4>
              <p>Furniture</p>
              <p>Decor</p>
            </div>
          </div>
        )}
      </div>

      <div className="search-bar">
        <input placeholder="Search Amazon" />
        <button>Search</button>
      </div>

      <div className="nav-links">
        <p onClick={() => setShowLogin(true)}>Hello, Sign in</p>
        <p onClick={() => setShowCart(true)}>
          Cart 🛒 <span className="cart-count">{cartCount}</span>
        </p>
      </div>
    </header>
  );
}

export default Header;
