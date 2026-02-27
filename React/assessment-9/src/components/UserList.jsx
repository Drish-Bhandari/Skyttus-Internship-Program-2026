import UserItem from "./UserItem";

function UserList({ users, deleteUser, setEditUser }) {
  if (users.length === 0) {
    return <p className="empty">No Users Found</p>;
  }

  return (
    <div className="list">
      {users.map((user) => (
        <UserItem
          key={user.id}
          user={user}
          deleteUser={deleteUser}
          setEditUser={setEditUser}
        />
      ))}
    </div>
  );
}

export default UserList;