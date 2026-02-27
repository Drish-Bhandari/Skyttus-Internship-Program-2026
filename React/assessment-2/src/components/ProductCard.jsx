import { FaStar } from "react-icons/fa";

function ProductCard({ title, price, image, handleAddToCart }) {
  return (
    <div className="product-card">
      <div className="image-container">
        <img src={image} alt={title} />
      </div>

      <h3>{title}</h3>

      <div className="rating">
        <FaStar /><FaStar /><FaStar /><FaStar />
      </div>

      <p className="price">₹{price}</p>

      <span className="prime-badge">Prime</span>

      <button onClick={handleAddToCart}>Add to Cart</button>
    </div>
  );
}

export default ProductCard;
