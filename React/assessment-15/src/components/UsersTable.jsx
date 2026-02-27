import React from "react";

function UsersTable({ users }) {
  return (
    <div className="bg-white p-6 rounded shadow">
      <h3 className="text-lg font-semibold mb-4">Users List</h3>
      {users.length === 0 ? (
        <p>No Users Added</p>
      ) : (
        <table className="w-full border">
          <thead>
            <tr className="bg-gray-200">
              <th className="p-2">Name</th>
              <th className="p-2">Email</th>
            </tr>
          </thead>
          <tbody>
            {users.map((user, index) => (
              <tr key={index} className="text-center border-t">
                <td className="p-2">{user.name}</td>
                <td className="p-2">{user.email}</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
}

export default React.memo(UsersTable);