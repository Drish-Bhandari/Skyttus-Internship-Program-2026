import { useRef, useEffect } from "react";

function SearchFilter({
  searchTerm,
  setSearchTerm,
  category,
  setCategory,
  categories
}) {
  const searchRef = useRef();

  // Auto-focus using useRef
  useEffect(() => {
    searchRef.current.focus();
  }, []);

  return (
    <div className="search-filter">
      <input
        ref={searchRef}
        type="text"
        placeholder="Search products..."
        value={searchTerm}
        onChange={(e) => setSearchTerm(e.target.value)}
      />

      <select
        value={category}
        onChange={(e) => setCategory(e.target.value)}
      >
        <option value="all">All Categories</option>
        {categories.map((cat, index) => (
          <option key={index} value={cat}>
            {cat}
          </option>
        ))}
      </select>
    </div>
  );
}

export default SearchFilter;