import { useAuth } from "../context/AuthContext";

function Profile() {
  const { user } = useAuth();

  return (
      <div className="page-wrapper">
    <div className="profile-card">
      <h2>Profile</h2>
      <p><strong>Username:</strong> {user?.username}</p>
    </div>
    </div>
  );
}
export default Profile;