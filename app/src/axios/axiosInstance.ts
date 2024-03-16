import axios from "axios";
import { UseSelector, useSelector } from "react-redux";

const API_URL = "http://127.0.0.1:8000/api/";

const accessToken = localStorage.getItem("accessToken");

export const axiosInstance = axios.create({
  baseURL: API_URL,
  withCredentials: true,
  headers: {
    "Content-Type": "application/json",
  },
});

export const axiosPrivateInstance = axios.create({
  baseURL: API_URL,
  withCredentials: true,
  headers: {
    "Content-Type": "application/json",
    Authorization: `Bearer ${accessToken}`,
  },
});
