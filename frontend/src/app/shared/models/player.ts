export type Player = {
    id: number,
    username: string,
    email: string,
    coins: number,
    max_score: number
}

export type GetPlayerResponse = {
    data: Player[];
}

export type PlayerRegister = {
    username: string,
    email: string,
    password: string,
    profile_image_url: string
}