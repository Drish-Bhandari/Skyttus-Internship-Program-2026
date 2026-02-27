function Dashboard({ users }) {
  const total = users.length;
  const active = users.filter((u) => u.active).length;
  const inactive = total - active;

  return (
    <div className="dashboard">
      <div className="box">
        <h2>{total}</h2>
        <p>Total Users</p>
      </div>
      <div className="box green-box">
        <h2>{active}</h2>
        <p>Active</p>
      </div>
      <div className="box red-box">
        <h2>{inactive}</h2>
        <p>Inactive</p>
      </div>
    </div>
  );
}

export default Dashboard;