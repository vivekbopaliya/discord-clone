import React from "react";
import { UseSelector, useSelector } from "react-redux";
import { Input } from "../ui/Input";
import { Button } from "../ui/Button";
const ChatBar = () => {
  const channel = useSelector((state: any) => state.channel.currentChannel);
  const user = useSelector((state: any) => state.auth.user);

  console.log(user);
  const [chats, setChat] = React.useState([]);
  const [text, setText] = React.useState("");
  const room_name = channel?.id;

  const url = `ws://${window.location.host}/ws/chat/channel/${room_name}/`;
  const chatSocket = new WebSocket(url);
  try {
    console.log(chatSocket);
    chatSocket.onmessage = function (e) {
      console.log(e);
      const data = JSON.parse(e.data);
      console.log(data);
    };
  } catch (error) {
    console.log(error);
  }

  console.log(chatSocket.readyState);
  const handleSubmit = () => {
    chatSocket.send(
      JSON.stringify({
        message: text,
        username: "asdasd",
        channel: channel.id,
      })
    );
  };
  return (
    <div>
      let's chat here {channel ? channel?.name : ""}
      <p>
        <Input
          type="text"
          placeholder="Chat..."
          value={text}
          onChange={(e) => setText(e.target.value)}
        />
        <Button onClick={handleSubmit}>Send</Button>
      </p>
    </div>
  );
};

export default ChatBar;
