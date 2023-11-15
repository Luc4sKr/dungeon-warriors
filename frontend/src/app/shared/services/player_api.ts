import { api } from "./api";
import { PlayerRegister } from "../models/player";

export async function register(player_register: PlayerRegister) {
    try {
        const response = await api.post("/player/register", player_register);

        console.log(response)
    }
    catch (error) {
        console.error("Erro: " + error)
    }
}