import { useState } from "react";
import BlogList from "./components/BlogList";
import BlogDetail from "./components/BlogDetail";

function App() {
  const [selectedBlog, setSelectedBlog] = useState(null);

  const blogs = [
    {
      id: 1,
      title: "Getting Started with React",
      author: "Drish Bhandari",
      content:
        "React is a powerful JavaScript library used for building user interfaces. It allows developers to create reusable components and manage state efficiently. Understanding JSX, components, and props is the foundation of React development..."
    },
    {
      id: 2,
      title: "Understanding useState Hook",
      author: "Drish Bhandari",
      content:
        "The useState hook allows functional components to manage state. It returns a state variable and a function to update it. State updates trigger re-renders, making UI dynamic..."
    },
    {
      id: 3,
      title: "Why Single Page Applications?",
      author: "Drish Bhandari",
      content:
        "Single Page Applications (SPA) improve user experience by dynamically updating content without reloading the entire page. React enables this using conditional rendering..."
    }
  ];

  return (
    <div className="app">
      <h1>My Blog</h1>

      {selectedBlog ? (
        <BlogDetail blog={selectedBlog} goBack={() => setSelectedBlog(null)} />
      ) : (
        <BlogList blogs={blogs} onSelect={setSelectedBlog} />
      )}
    </div>
  );
}

export default App;