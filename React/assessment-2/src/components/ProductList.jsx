import { useState, useEffect } from "react";
import { products } from "../data/products";
import ProductCard from "./ProductCard";

function ProductList({ selectedCategory, handleAddToCart }) {
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    setTimeout(() => setLoading(false), 1500);
  }, []);

  const filtered =
    selectedCategory === "All"
      ? products
      : products.filter(p => p.category === selectedCategory);

  if (loading) {
    return (
      <div className="product-section">
        {[...Array(6)].map((_, i) => (
          <div key={i} className="skeleton-card"></div>
        ))}
      </div>
    );
  }

  return (
    <div className="product-section">
      {filtered.map(product => (
        <ProductCard
          key={product.id}
          {...product}
          handleAddToCart={handleAddToCart}
        />
      ))}
    </div>
  );
}

export default ProductList;
