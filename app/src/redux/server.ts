import { createSlice } from "@reduxjs/toolkit";

export const server = createSlice({
  name: "server",
  initialState: {
    currentServer: null,
  },
  reducers: {
    setCurrentServer(state: any, action) {
      state.currentServer = action.payload;
    },
  },
});

export const { setCurrentServer } = server.actions;

export default server.reducer;
