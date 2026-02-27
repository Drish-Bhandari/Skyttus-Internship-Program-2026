import { useState, useCallback } from "react";
import UsersTable from "../components/UsersTable";
import AddUserForm from "../components/AddUserForm";

function Users() {
  const [users, setUsers] = useState([]);

  const addUser = useCallback((data) => {
    setUsers((prev) => [...prev, data]);
  }, []);

  return (
    <div className="p-6">
      <AddUserForm addUser={addUser} />
      <UsersTable users={users} />
    </div>
  );
}

export default Users;