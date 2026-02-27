import { useEffect, useState } from "react";
import ProductList from "./components/ProductList";
import SearchFilter from "./components/SearchFilter";
import { fetchProducts } from "./services/ProductServices";

function App() {
  const [products, setProducts] = useState([]);
  const [filteredProducts, setFilteredProducts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  const [searchTerm, setSearchTerm] = useState("");
  const [category, setCategory] = useState("all");

  // Fetch Products (Mount)
  useEffect(() => {
    const getProducts = async () => {
      try {
        const data = await fetchProducts();
        setProducts(data);
        setFilteredProducts(data);
      } catch (err) {
        setError("Failed to fetch products");
      } finally {
        setLoading(false);
      }
    };

    getProducts();
  }, []);

  // Filtering Logic (Triggered when search/category changes)
  useEffect(() => {
    let filtered = products;

    if (searchTerm) {
      filtered = filtered.filter((product) =>
        product.title
          .toLowerCase()
          .includes(searchTerm.toLowerCase())
      );
    }

    if (category !== "all") {
      filtered = filtered.filter(
        (product) => product.category === category
      );
    }

    setFilteredProducts(filtered);
  }, [searchTerm, category, products]);

  // Get Unique Categories
  const categories = [
    ...new Set(products.map((p) => p.category)),
  ];

  return (
    <div className="app">
      <h1>Product Store</h1>

      <SearchFilter
        searchTerm={searchTerm}
        setSearchTerm={setSearchTerm}
        category={category}
        setCategory={setCategory}
        categories={categories}
      />

      {loading && <p className="loading">Loading...</p>}
      {error && <p className="error">{error}</p>}

      {!loading && !error && (
        <ProductList products={filteredProducts} />
      )}
    </div>
  );
}

export default App;