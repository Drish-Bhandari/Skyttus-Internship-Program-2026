function UserCard({ user, toggleStatus }) {
  return (
    <div className={`card ${user.active ? "active" : "inactive"}`}>
      <h3>{user.name}</h3>
      <p>{user.email}</p>

      <p>Status: 
        <span className={user.active ? "green" : "red"}>
          {user.active ? " Active" : " Inactive"}
        </span>
      </p>

      <button onClick={() => toggleStatus(user.id)}>
        Toggle Status
      </button>
    </div>
  );
}

export default UserCard;