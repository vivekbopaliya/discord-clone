import React from "react";
import { Separator } from "../ui/Seperator";
import { Hash, Lock, LockIcon, Plus } from "lucide-react";
import { Input } from "../ui/Input";
import { useDispatch, useSelector } from "react-redux";
import { axiosInstance, axiosPrivateInstance } from "../axios/axiosInstance";
import {
  Dialog,
  DialogClose,
  DialogContent,
  DialogFooter,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from "../ui/Dialog";
import { Button } from "../ui/Button";
import { useMutation } from "@tanstack/react-query";
import { AxiosError } from "axios";
import { toast, useToast } from "../ui/use-toast";
import { setChannel } from "../redux/channel";

const ChannelBar = () => {
  const server = useSelector((state: any) => state.server.currentServer);
  const user = useSelector((state: any) => state.auth.user);
  const [members, setMembers] = React.useState([]);
  const [channelName, setChannelName] = React.useState("");
  const [channels, setChannels] = React.useState([]);
  const dispatch = useDispatch();

  const { mutate: handleSubmit } = useMutation({
    mutationFn: async () => {
      const res = await axiosPrivateInstance.post(
        `channel/create/${server.id}/`,
        {
          name: channelName,
        }
      );
      console.log(res.data);
    },
    onError: (e) => {
      if (e instanceof AxiosError) {
        if (e.response?.status === 401) {
          return toast({
            title: "You need to be login to do that",
            variant: "destructive",
          });
        }
        if (e.response?.status === 40) {
          return toast({
            title: "Invalid data",
            description: "Please provid valid credentials to create channel.",
            variant: "destructive",
          });
        }
      }
      return toast({
        title: "There was an error creating channel!",
        description: "Channel could not be created, please try again.",
        variant: "destructive",
      });
    },
    onSuccess: () => {
      toast({
        title: "Channel created successfully",
      });
    },
  });

  React.useEffect(() => {
    fetchMembers();
    fetchChannels();
  }, [server, handleSubmit]);

  const fetchMembers = async () => {
    try {
      const res = await axiosInstance.get(`members/getMembers/${server.id}/`);
      setMembers(res.data.members);
      console.log(res.data);
    } catch (error) {
      console.log(error);
    }
  };

  const fetchChannels = async () => {
    try {
      const res = await axiosInstance.get(`channel/get/${server.id}/`);
      console.log(res.data.channels);
      setChannels(res.data.channels);
    } catch (error) {
      console.log(error);
    }
  };

  return (
    <div className="flex flex-col justify-center">
      <header className="py-3">
        {server ? server.name : "Click a server"}{" "}
      </header>

      <Separator className="my-1 px-2" />

      <Input placeholder="Search" />

      <Separator />

      <div className="flex justify-between hover:bg-gray-900 items-center px-3 py-3">
        <main className="gap-3 flex ">
          <p>Text Channels</p>

          <Dialog>
            <DialogTrigger>
              <Plus />
            </DialogTrigger>

            <DialogContent>
              <DialogHeader>
                <DialogTitle>Create Channel</DialogTitle>
              </DialogHeader>

              <div className="flex flex-col gap-4 ">
                <p>Enter Channel Name</p>
                <Input
                  type="text"
                  value={channelName}
                  onChange={(e) => setChannelName(e.target.value)}
                  placeholder="Channel Name..."
                />
              </div>
              <DialogFooter>
                <DialogClose>
                  {/* @ts-ignore */}
                  <Button onClick={handleSubmit}>Submit</Button>
                </DialogClose>
              </DialogFooter>
            </DialogContent>
          </Dialog>
        </main>
        <LockIcon size={20} />
      </div>

      {user !== null && (
        <div>
          {members.map((member: any) => {
            return (
              <div>
                <p>{member.username}</p>
              </div>
            );
          })}
        </div>
      )}

      {channels.map((channel: any) => {
        return (
          <div
            onClick={() => dispatch(setChannel(channel))}
            className="flex  justify-between cursor-pointer hover:bg-gray-700 bg-opacity-30 px-3 py-2 rounded-md"
          >
            <main className="flex">
              <Hash />
              <p className="ml-2">{channel.name}</p>
            </main>

            <div>
              <Lock />
            </div>
          </div>
        );
      })}
    </div>
  );
};

export default ChannelBar;
