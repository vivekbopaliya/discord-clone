import { useContext, useDebugValue } from "react";
import AuthContext from "../store/AuthContext";

export default function useAuth() {
  const { user } = useContext(AuthContext);

  useDebugValue(user, (user) => (user ? "Logged In" : "Logged Out"));

  return useContext(AuthContext);
}
