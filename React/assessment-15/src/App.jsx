import { Routes, Route } from "react-router-dom";
import { Suspense, lazy } from "react";
import Sidebar from "./components/Sidebar";
import Header from "./components/Header";

const Dashboard = lazy(() => import("./pages/Dashboard"));
const Users = lazy(() => import("./pages/Users"));

function App() {
  return (
    <div className="flex h-screen bg-gray-100">
      <Sidebar />
      <div className="flex-1 flex flex-col">
        <Header />
        <Suspense fallback={<div className="p-5">Loading...</div>}>
          <Routes>
            <Route path="/" element={<Dashboard />} />
            <Route path="/users" element={<Users />} />
          </Routes>
        </Suspense>
      </div>
    </div>
  );
}

export default App;