import { useState, useEffect } from "react";

function RegisterForm() {
  const [form, setForm] = useState({
    name: "",
    email: "",
    password: "",
  });

  const [errors, setErrors] = useState({});
  const [success, setSuccess] = useState("");

  // Load saved form data
  useEffect(() => {
    const savedData = JSON.parse(localStorage.getItem("formData"));
    if (savedData) {
      setForm(savedData);
    }
  }, []);

  // Save to localStorage
  useEffect(() => {
    localStorage.setItem("formData", JSON.stringify(form));
  }, [form]);

  // Validation Logic
  const validate = (fieldValues = form) => {
    let tempErrors = { ...errors };

    if ("name" in fieldValues) {
      tempErrors.name = fieldValues.name
        ? ""
        : "Name is required.";
    }

    if ("email" in fieldValues) {
      const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      tempErrors.email = emailPattern.test(fieldValues.email)
        ? ""
        : "Invalid email format.";
    }

    if ("password" in fieldValues) {
      const strongPassword =
        /^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,}$/;
      tempErrors.password = strongPassword.test(fieldValues.password)
        ? ""
        : "Password must be 8+ chars, include uppercase, lowercase & number.";
    }

    setErrors(tempErrors);

    return Object.values(tempErrors).every((x) => x === "");
  };

  const handleChange = (e) => {
    const { name, value } = e.target;

    setForm({
      ...form,
      [name]: value,
    });

    validate({ [name]: value });
  };

  const handleBlur = () => {
    validate();
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    if (validate()) {
      setSuccess("Form submitted successfully!");
      localStorage.removeItem("formData");
      setForm({ name: "", email: "", password: "" });
    } else {
      setSuccess("");
    }
  };

  return (
    <div className="form-container">
      <h2>Register</h2>

      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <input
            type="text"
            name="name"
            placeholder="Full Name"
            value={form.name}
            onChange={handleChange}
            onBlur={handleBlur}
            className={errors.name ? "error-input" : ""}
          />
          <p className="error">{errors.name}</p>
        </div>

        <div className="form-group">
          <input
            type="text"
            name="email"
            placeholder="Email Address"
            value={form.email}
            onChange={handleChange}
            onBlur={handleBlur}
            className={errors.email ? "error-input" : ""}
          />
          <p className="error">{errors.email}</p>
        </div>

        <div className="form-group">
          <input
            type="password"
            name="password"
            placeholder="Password"
            value={form.password}
            onChange={handleChange}
            onBlur={handleBlur}
            className={errors.password ? "error-input" : ""}
          />
          <p className="error">{errors.password}</p>
        </div>

        <button type="submit">Submit</button>

        {success && <p className="success">{success}</p>}
      </form>
    </div>
  );
}

export default RegisterForm;