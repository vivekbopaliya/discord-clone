import { createSlice } from "@reduxjs/toolkit";

export const channel = createSlice({
  name: "channel",
  initialState: {
    currentChannel: null,
  },
  reducers: {
    setChannel(state: any, action) {
      state.currentChannel = action.payload;
    },
  },
});

export const { setChannel } = channel.actions;

export default channel.reducer;
