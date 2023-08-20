export interface Player {
    id: number,
    username: string,
    email: string,
    coins: number,
    max_score: number
}

export type GetPlayerResponse = {
    data: Player[];
}