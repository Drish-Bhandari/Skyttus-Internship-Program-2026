import axios from "axios";

export const productAPI = axios.create({
  baseURL: import.meta.env.VITE_PRODUCT_API,
});

export const userAPI = axios.create({
  baseURL: import.meta.env.VITE_USER_API,
});