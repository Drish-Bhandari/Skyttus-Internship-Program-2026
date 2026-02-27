import BlogCard from "./BlogCard";

function BlogList({ blogs, onSelect }) {
  return (
    <div className="blog-list">
      {blogs.map((blog) => (
        <BlogCard key={blog.id} blog={blog} onSelect={onSelect} />
      ))}
    </div>
  );
}

export default BlogList;