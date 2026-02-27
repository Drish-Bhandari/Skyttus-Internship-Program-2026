import { useEffect, useState } from "react";
import { productAPI } from "../services/api";
import Loader from "../components/Loader";
import Error from "../components/Error";

function Products() {
  const [products, setProducts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    productAPI.get("/products")
      .then(res => setProducts(res.data))
      .catch(() => setError("Failed to fetch products"))
      .finally(() => setLoading(false));
  }, []);

  if (loading) return <Loader />;
  if (error) return <Error message={error} />;

  return (
    <div className="list">
      {products.slice(0, 5).map(product => (
        <div key={product.id} className="list-item">
          {product.title}
        </div>
      ))}
    </div>
  );
}

export default Products;