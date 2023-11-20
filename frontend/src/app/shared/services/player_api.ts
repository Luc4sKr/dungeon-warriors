import { api } from "./api";
import { PlayerRegister } from "../models/player";

export async function save_profile_image(profile_image: File) {
    try {
        const formData = new FormData();
        formData.append("profile_image", profile_image)

        const headers = { 'Content-Type': 'multipart/form-data' }
        const response = await api.post("/player/save_profile_image", formData, { headers: headers });
    
        return response.data;
    }
    catch {

    }
}

export async function register(player_register: PlayerRegister) {
    try {
        const response = await api.post("/player/register", player_register);
        return response.data;
    }
    catch (error) {
        console.error("Erro: " + error);
    }
}

export async function get_profile_image(id: number) {
    try {
        const response = await api.post(`/player/get_profile_image/${id}`)

        return response.data;
    }
    catch (error) {
        console.log(error);
    }
}