import { createContext, useContext, useState } from "react";

const DashboardContext = createContext();

export function DashboardProvider({ children }) {
  const [stats, setStats] = useState({
    totalProducts: 0,
    totalUsers: 0,
  });

  return (
    <DashboardContext.Provider value={{ stats, setStats }}>
      {children}
    </DashboardContext.Provider>
  );
}

export const useDashboard = () => useContext(DashboardContext);