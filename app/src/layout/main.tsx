import React from "react";
import ServerBar from "../components/ServerBar";
import ChannelBar from "../components/ChannelBar";

const main = ({ children }: { children: React.ReactNode }) => {
  return (
    <div className=" grid grid-cols-12 w-screen h-screen gap-2">
      <div className=" col-span-1 ">
        <ServerBar />
      </div>
      <div className="col-span-3 ">
        <ChannelBar />
      </div>

      <div className="col-span-8">{children}</div>
    </div>
  );
};

export default main;
