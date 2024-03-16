import { createSlice } from "@reduxjs/toolkit";

export const auth = createSlice({
  name: "auth",
  initialState: {
    accessToken: localStorage.getItem("accessToken") || null,
    user: {
      id: null,
      name: null,
      image: null,
    },
  },
  reducers: {
    setAccessToken(state: any, action) {
      state.accessToken = action.payload;
    },
    setUser(state: any, action) {
      state.user = action.payload;
    },
  },
});

export const { setAccessToken, setUser } = auth.actions;

export default auth.reducer;
