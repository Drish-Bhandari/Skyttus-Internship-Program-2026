import React from "react";

function DashboardCards() {
  const data = [
    { title: "Users", value: 120 },
    { title: "Revenue", value: "$5,000" },
    { title: "Orders", value: 80 },
  ];

  return (
    <div className="grid grid-cols-3 gap-6">
      {data.map((item, index) => (
        <div key={index} className="bg-white p-6 rounded shadow">
          <h3 className="text-gray-500">{item.title}</h3>
          <p className="text-2xl font-bold">{item.value}</p>
        </div>
      ))}
    </div>
  );
}

export default React.memo(DashboardCards);