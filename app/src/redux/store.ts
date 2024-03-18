import { configureStore } from "@reduxjs/toolkit";
import authReducer from "./auth";
import serverReducer from "./server";
import channelReducer from "./channel";

export default configureStore({
  reducer: {
    auth: authReducer,
    server: serverReducer,
    channel: channelReducer,
  },
});
