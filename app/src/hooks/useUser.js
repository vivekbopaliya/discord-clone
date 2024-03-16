import { setUser } from "../redux/auth"
import useAxiosPrivate from "./useAxiosPrivate"
import { useDispatch } from 'react-redux'

export default function useUser() {

    const dispatch = useDispatch()

    const axiosPrivateInstance = useAxiosPrivate()

    async function getUser() {
        try {
            const { data } = await axiosPrivateInstance.get('auth/user/')
            dispatch(setUser(data))
        } catch (error) {
            console.log(error.response)
        }
    }

    return getUser
}