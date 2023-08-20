
import { BasicTable } from "../../shared/components/basicTable/BasicTable"
import { Player } from "../../shared/models/player";
import { api } from "../../shared/services/api";
import { useEffect, useState } from "react";

export const Players = () => {
    const defaultPlayer: Player[] = []
    const [players, setPlayers] = useState(defaultPlayer);

    useEffect(() => {
        api.get<Player[]>("/players")
            .then((response) => {
                setPlayers(response.data);
            });
    }, []);

    return (
        <div>
            <BasicTable />
        </div>
    )
}