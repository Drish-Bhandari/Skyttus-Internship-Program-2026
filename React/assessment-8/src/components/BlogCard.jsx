function BlogCard({ blog, onSelect }) {
  return (
    <div className="blog-card" onClick={() => onSelect(blog)}>
      <h3>{blog.title}</h3>
      <p className="author">By {blog.author}</p>
      <p>{blog.content.substring(0, 80)}...</p>
      <button>Read More</button>
    </div>
  );
}

export default BlogCard;