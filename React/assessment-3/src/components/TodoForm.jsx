import { useState } from "react";

function TodoForm({ addTodo }) {
  const [input, setInput] = useState("");
  const [error, setError] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();

    if (input.trim() === "") {
      setError("Task cannot be empty!");
      return;
    }

    setError("");
    addTodo(input);
    setInput("");
  };

  return (
    <>
      <form onSubmit={handleSubmit}>
        <input
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Enter task..."
        />
        <button>Add</button>
      </form>
      <p className="error">{error}</p>
    </>
  );
}

export default TodoForm;