import { useState, useEffect, useRef } from "react";
import Button from "./Button";
import Input from "./Input";

function UserForm({ addUser, updateUser, editUser }) {
  const [form, setForm] = useState({ name: "", email: "" });

  const phoneRef = useRef(); // Uncontrolled input

  useEffect(() => {
    if (editUser) {
      setForm(editUser);
    }
  }, [editUser]);

  useEffect(() => {
    phoneRef.current.focus(); // useRef focus example
  }, []);

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    const phone = phoneRef.current.value;

    if (!form.name || !form.email) return;

    if (editUser) {
      updateUser({ ...form, phone });
    } else {
      addUser({ ...form, phone });
    }

    setForm({ name: "", email: "" });
    phoneRef.current.value = "";
  };

  return (
    <form className="form" onSubmit={handleSubmit}>
      <Input
        type="text"
        name="name"
        placeholder="Enter Name"
        value={form.name}
        onChange={handleChange}
      />

      <Input
        type="email"
        name="email"
        placeholder="Enter Email"
        value={form.email}
        onChange={handleChange}
      />

      {/* Uncontrolled Input */}
      <input
        type="text"
        placeholder="Enter Phone"
        ref={phoneRef}
        className="input"
      />

      <Button text={editUser ? "Update User" : "Add User"} />
    </form>
  );
}

export default UserForm;