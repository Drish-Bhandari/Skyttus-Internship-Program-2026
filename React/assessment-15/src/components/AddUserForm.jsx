import { useForm } from "react-hook-form";

function AddUserForm({ addUser }) {
  const { register, handleSubmit, reset, formState: { errors } } = useForm();

  const onSubmit = (data) => {
    addUser(data);
    reset();
  };

  return (
    <form onSubmit={handleSubmit(onSubmit)} className="bg-white p-6 rounded shadow mb-6">
      <h3 className="text-lg font-semibold mb-4">Add User</h3>

      <input
        {...register("name", { required: "Name is required" })}
        placeholder="Name"
        className="border p-2 w-full mb-2"
      />
      {errors.name && <p className="text-red-500">{errors.name.message}</p>}

      <input
        {...register("email", { required: "Email is required" })}
        placeholder="Email"
        className="border p-2 w-full mb-2"
      />
      {errors.email && <p className="text-red-500">{errors.email.message}</p>}

      <button className="bg-indigo-600 text-white px-4 py-2 rounded">
        Add User
      </button>
    </form>
  );
}

export default AddUserForm;