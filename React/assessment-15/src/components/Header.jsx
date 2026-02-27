function Header() {
  return (
    <div className="bg-white shadow p-4 flex justify-between">
      <h2 className="text-xl font-semibold">Admin Dashboard</h2>
      <button className="bg-indigo-600 text-white px-4 py-1 rounded">
        Logout
      </button>
    </div>
  );
}

export default Header;