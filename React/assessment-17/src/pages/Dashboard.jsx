import { useAuth } from "../context/AuthContext";

function Dashboard() {
  const { logout, user } = useAuth();

  return (
    <div style={{ padding: "40px" }}>
      <h2>Dashboard</h2>
      <p>Welcome {user?.email}</p>
      <button onClick={logout}>Logout</button>
    </div>
  );
}

export default Dashboard;