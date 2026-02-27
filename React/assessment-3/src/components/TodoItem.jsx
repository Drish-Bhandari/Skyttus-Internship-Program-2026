function TodoItem({ todo, index, deleteTodo, toggleComplete, editTodo }) {
  const handleEdit = () => {
    const newText = prompt("Edit task:", todo.text);
    if (newText && newText.trim() !== "") {
      editTodo(index, newText);
    }
  };

  return (
    <li className={todo.completed ? "completed" : ""}>
      <span onClick={() => toggleComplete(index)}>{todo.text}</span>

      <div>
        <button onClick={handleEdit}>Edit</button>
        <button onClick={() => deleteTodo(index)}>Delete</button>
      </div>
    </li>
  );
}

export default TodoItem;