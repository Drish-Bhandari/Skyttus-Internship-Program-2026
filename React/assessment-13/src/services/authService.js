export const loginUser = (credentials) => {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      const demoUser = import.meta.env.VITE_DEMO_USERNAME;
      const demoPass = import.meta.env.VITE_DEMO_PASSWORD;

      if (
        credentials.username === demoUser &&
        credentials.password === demoPass
      ) {
        resolve({
          username: credentials.username,
          token: "fake-jwt-token-12345"
        });
      } else {
        reject(new Error("Invalid credentials"));
      }
    }, 1000); // simulate API delay
  });
};