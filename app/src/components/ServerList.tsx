import React from "react";
import { axiosPrivateInstance } from "../axios/axiosInstance";
import { UseDispatch, useDispatch } from "react-redux";
import { setCurrentServer } from "../redux/server";

const ServerList = () => {
  const [servers, setServers] = React.useState<any | null>([]);
  const dispatch = useDispatch();

  React.useEffect(() => {
    getServers();
  }, []);

  const getServers = async () => {
    try {
      const res = await axiosPrivateInstance.get("server/getServers/");
      setServers(res.data.servers);
      console.log(res.data.servers);
    } catch (error) {
      console.log(error);
    }
  };
  return (
    <div>
      {servers.map((server: any) => {
        return (
          <p
            className="cursor-pointer"
            onClick={() => dispatch(setCurrentServer(server))}
          >
            {" "}
            {server.name}
          </p>
        );
      })}
    </div>
  );
};

export default ServerList;
