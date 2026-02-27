import { useEffect, useState } from "react";
import { productAPI, userAPI } from "../services/api";
import Card from "../components/Card";
import Loader from "../components/Loader";
import Error from "../components/Error";
import { useDashboard } from "../context/DashboardContext";

function Overview() {
  const { stats, setStats } = useDashboard();
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    Promise.all([
      productAPI.get("/products"),
      userAPI.get("/users"),
    ])
      .then(([productRes, userRes]) => {
        setStats({
          totalProducts: productRes.data.length,
          totalUsers: userRes.data.users.length,
        });
      })
      .catch(() => setError("Failed to load dashboard data"))
      .finally(() => setLoading(false));
  }, []);

  if (loading) return <Loader />;
  if (error) return <Error message={error} />;

  return (
    <div className="card-grid">
      <Card title="Total Products" value={stats.totalProducts} />
      <Card title="Total Users" value={stats.totalUsers} />
    </div>
  );
}

export default Overview;