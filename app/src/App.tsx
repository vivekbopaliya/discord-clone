import ChannelBar from "./components/ChannelBar";
import ChatBar from "./components/ChatBar";
import ServerBar from "./components/ServerBar";

function App() {
  return (
    <div className=" grid grid-cols-12 w-screen h-screen gap-2">
      <div className=" col-span-1 ">
        <ServerBar />
      </div>
      <div className="col-span-3 ">
        <ChannelBar />
      </div>

      <div className="col-span-8">
        <ChatBar />
      </div>
    </div>
  );
}

export default App;
