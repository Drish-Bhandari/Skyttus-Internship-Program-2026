import { Link } from "react-router-dom";

function ProductCard({ product }) {
  return (
    <div className="card">
      <img src={product.image} alt={product.title} />
      <h3>{product.title.substring(0, 30)}...</h3>
      <p>${product.price}</p>
      <Link to={`/product/${product.id}`}>
        <button>View Details</button>
      </Link>
    </div>
  );
}

export default ProductCard;