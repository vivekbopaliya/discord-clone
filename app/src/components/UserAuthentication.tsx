import React, { useContext } from "react";
import {
  Dialog,
  DialogClose,
  DialogContent,
  DialogDescription,
  DialogFooter,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from "../ui/Dialog";
import { Button } from "../ui/Button";
import { Input } from "../ui/Input";
import axios, { AxiosError } from "axios";
import { useMutation } from "@tanstack/react-query";
import { toast } from "../ui/use-toast";
import { axiosInstance } from "../axios/axiosInstance";
import { useDispatch } from "react-redux";
import { setAccessToken, setUser } from "../redux/auth";
import { jwtDecode } from "jwt-decode";

type AuthType = "REGISTER" | "LOGIN";

const UserAuthentication = () => {
  const [auth, setAuth] = React.useState<AuthType>("REGISTER");
  const [name, setName] = React.useState("");
  const [email, setEmail] = React.useState("");
  const [password, setPassword] = React.useState("");
  const [password2, setPassword2] = React.useState("");

  const dispatch = useDispatch();

  async function handleLogin(event: any) {
    event.preventDefault();
    try {
      const response = await axiosInstance.post(
        "auth/login/",
        JSON.stringify({
          email,
          password,
        })
      );
      console.log(response.data);
      localStorage.setItem("accessToken", response?.data?.access_token || null);
      dispatch(setAccessToken(response?.data?.access_token || null));
    } catch (error) {
      console.log(error);
    }
  }
  console.log(localStorage.getItem("accessToken"));

  const { mutate: handleRegister, isPending: isLoading } = useMutation({
    mutationFn: async () => {
      const payload = {
        username: name,
        email: email,
        password: password,
        password2: password2,
      };

      await axiosInstance.post(
        "http://127.0.0.1:8000/api/auth/register/",
        payload
      );
    },
    onError: (err) => {
      if (err instanceof AxiosError) {
        if (err.response?.status === 401) {
          return toast({
            title: "Password doesn't match",
            description: "Please enter same password",
            variant: "destructive",
          });
        }
      }
      return toast({
        title: "There was an error",
        description: "You did not register, please try again!",
        variant: "destructive",
      });
    },
    onSuccess: () => {
      setAuth("LOGIN");
      return toast({
        title: "You are successfully registerd!",
        description: "Now please login with registerd credentials.",
      });
    },
  });

  return (
    <div>
      <Dialog>
        <DialogTrigger>
          <Button>{auth === "REGISTER" ? "Register" : "Login"}</Button>

          <DialogContent color="white" className="max-w-lg min-h-64 ">
            <DialogHeader>
              <DialogTitle>
                {auth === "REGISTER" ? "Sign in" : "Create your user"}
              </DialogTitle>

              <DialogDescription>
                Give yourself a personality with a name and an icon. You can
                always change it later.
              </DialogDescription>
            </DialogHeader>
            {auth === "REGISTER" && (
              <div className="mt-2 gap-2 flex flex-col ">
                <p>YOUR NAME</p>
                <Input value={name} onChange={(e) => setName(e.target.value)} />
              </div>
            )}

            <div className="mt-2 gap-2 flex flex-col ">
              <p>YOUR EMAIL</p>
              <Input value={email} onChange={(e) => setEmail(e.target.value)} />
            </div>

            <div className="mt-2 gap-2 flex flex-col ">
              <p>YOUR PASSWORD</p>
              <Input
                value={password}
                onChange={(e) => setPassword(e.target.value)}
              />
            </div>

            {auth === "REGISTER" && (
              <div className="mt-2 gap-2 flex flex-col ">
                <p>Confirm your password</p>
                <Input
                  value={password2}
                  onChange={(e) => setPassword2(e.target.value)}
                />
              </div>
            )}
            {auth === "REGISTER" && (
              <p className="text-gray-600">
                Already have an account?{" "}
                <span
                  className="text-blue-600 cursor-pointer underline"
                  onClick={() => setAuth("LOGIN")}
                >
                  Login
                </span>
              </p>
            )}
            {auth === "LOGIN" && (
              <p className="text-gray-600">
                Doesn't have an account?{" "}
                <span
                  className="text-blue-600 cursor-pointer underline"
                  onClick={() => setAuth("REGISTER")}
                >
                  Register
                </span>
              </p>
            )}

            <DialogFooter className="flex flex-col gap-2 justify-between items-center w-full">
              {auth === "REGISTER" && (
                <Button
                  // @ts-ignore
                  onClick={handleRegister}
                  className="bg-blue-500"
                ></Button>
              )}
              {auth === "LOGIN" && (
                // @ts-ignore
                <Button onClick={handleLogin} className="bg-blue-500"></Button>
              )}
            </DialogFooter>
          </DialogContent>
        </DialogTrigger>
      </Dialog>
    </div>
  );
};

export default UserAuthentication;
