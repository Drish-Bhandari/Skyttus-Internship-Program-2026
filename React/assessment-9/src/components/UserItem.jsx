import Button from "./Button";

function UserItem({ user, deleteUser, setEditUser }) {
  return (
    <div className="item">
      <div>
        <h3>{user.name}</h3>
        <p>{user.email}</p>
        <p>{user.phone}</p>
      </div>

      <div className="actions">
        <Button text="Edit" onClick={() => setEditUser(user)} />
        <Button text="Delete" onClick={() => deleteUser(user.id)} />
      </div>
    </div>
  );
}

export default UserItem;