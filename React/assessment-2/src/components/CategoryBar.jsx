function CategoryBar({ setSelectedCategory }) {
  const categories = ["All", "Electronics", "Fashion"];

  return (
    <div className="category-bar">
      {categories.map((cat, index) => (
        <button key={index} onClick={() => setSelectedCategory(cat)}>
          {cat}
        </button>
      ))}
    </div>
  );
}

export default CategoryBar;
