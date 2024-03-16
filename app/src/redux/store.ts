import { configureStore } from "@reduxjs/toolkit";
import authReducer from "./auth";
import serverReducer from "./server";

export default configureStore({
  reducer: {
    auth: authReducer,
    server: serverReducer,
  },
});
