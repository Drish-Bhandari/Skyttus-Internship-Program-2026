import { useState } from "react";
import UserList from "./components/UserList";
import AddUser from "./components/AddUser";
import Dashboard from "./components/Dashboard";
import "./App.css";

function App() {
  const [users, setUsers] = useState([
    { id: 1, name: "Rahul Sharma", email: "rahul@gmail.com", active: true },
    { id: 2, name: "Priya Patel", email: "priya@gmail.com", active: false },
  ]);

  const [search, setSearch] = useState("");

  const addUser = (user) => {
    setUsers([...users, { ...user, id: Date.now(), active: true }]);
  };

  const toggleStatus = (id) => {
    setUsers(
      users.map((user) =>
        user.id === id ? { ...user, active: !user.active } : user
      )
    );
  };

  const filteredUsers = users.filter((user) =>
    user.name.toLowerCase().includes(search.toLowerCase())
  );

  return (
    <div className="container">
      <h1> User Management</h1>

      <Dashboard users={users} />

      <AddUser addUser={addUser} />

      <input
        type="text"
        placeholder="🔍 Search user..."
        value={search}
        onChange={(e) => setSearch(e.target.value)}
        className="search"
      />

      <UserList users={filteredUsers} toggleStatus={toggleStatus} />
    </div>
  );
}

export default App;