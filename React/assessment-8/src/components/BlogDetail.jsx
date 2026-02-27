function BlogDetail({ blog, goBack }) {
  return (
    <div className="blog-detail">
      <button className="back-btn" onClick={goBack}>
        ← Back to Blogs
      </button>

      <h2>{blog.title}</h2>
      <p className="author">By {blog.author}</p>
      <p className="full-content">{blog.content}</p>
    </div>
  );
}

export default BlogDetail;