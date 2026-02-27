import UserCard from "./UserCard";

function UserList({ users, toggleStatus }) {
  if (users.length === 0) {
    return <h3 className="no-users">No users available</h3>;
  }

  return (
    <div className="user-grid">
      {users.map((user) => (
        <UserCard key={user.id} user={user} toggleStatus={toggleStatus} />
      ))}
    </div>
  );
}

export default UserList;