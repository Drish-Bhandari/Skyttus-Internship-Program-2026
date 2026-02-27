import { Routes, Route, Navigate } from "react-router-dom";
import DashboardLayout from "./pages/DashboardLayout";
import Overview from "./pages/Overview";
import Products from "./pages/Products";
import Users from "./pages/Users";

function App() {
  return (
    <Routes>
      <Route path="/" element={<Navigate to="/dashboard/overview" />} />

      <Route path="/dashboard" element={<DashboardLayout />}>
        <Route path="overview" element={<Overview />} />
        <Route path="products" element={<Products />} />
        <Route path="users" element={<Users />} />
      </Route>
    </Routes>
  );
}

export default App;