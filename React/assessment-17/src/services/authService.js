const BASE_URL = import.meta.env.VITE_API_BASE_URL;
const LOGIN_ENDPOINT = import.meta.env.VITE_LOGIN_ENDPOINT;

export async function loginApi(email, password) {
  // Simulated login (Replace with real API call)
  if (email === "admin@example.com" && password === "123456") {
    // Fake JWT with 1 hour expiry
    const fakeToken = 
      "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9." +
      btoa(JSON.stringify({
        email,
        exp: Math.floor(Date.now() / 1000) + 3600
      })) +
      ".signature";

    return { token: fakeToken };
  }

  throw new Error("Invalid credentials");
}