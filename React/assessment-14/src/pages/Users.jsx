import { useEffect, useState } from "react";
import { userAPI } from "../services/api";
import Loader from "../components/Loader";
import Error from "../components/Error";

function Users() {
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    userAPI.get("/users")
      .then(res => setUsers(res.data.users))
      .catch(() => setError("Failed to fetch users"))
      .finally(() => setLoading(false));
  }, []);

  if (loading) return <Loader />;
  if (error) return <Error message={error} />;

  return (
    <div className="list">
      {users.slice(0, 5).map(user => (
        <div key={user.id} className="list-item">
          {user.firstName} {user.lastName}
        </div>
      ))}
    </div>
  );
}

export default Users;