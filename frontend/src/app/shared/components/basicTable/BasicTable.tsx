import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';

import { useEffect, useState } from "react";
import { api } from "../../../shared/services/api";
import { Player } from '../../models/player';
import { Avatar } from '@mui/material';

export const BasicTable = () => {
    const defaultPlayer: Player[] = []
    const [players, setPlayers] = useState(defaultPlayer);

    useEffect(() => {
        api.get("/players")
            .then((response) => {
                setPlayers(response.data.data);
            });

    }, []);

    return (
        <TableContainer component={Paper}>
            <Table sx={{ minWidth: 650 }} aria-label="Player table">
                <TableHead>
                    <TableRow>
                        <TableCell align="center">Id</TableCell>
                        <TableCell align="center">Username</TableCell>
                        <TableCell align="center">Email</TableCell>
                        <TableCell align="center">Coins</TableCell>
                        <TableCell align="center">Max Score</TableCell>
                        <TableCell align="center">Image</TableCell>
                    </TableRow>
                </TableHead>
                <TableBody>
                    {players.map((player: Player) => (
                        <TableRow
                            key={player.id}
                            sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
                        >
                            <TableCell align="center"> {player.id} </TableCell>
                            <TableCell align="center">{player.username}</TableCell>
                            <TableCell align="center">{player.email}</TableCell>
                            <TableCell align="center">{player.coins}</TableCell>
                            <TableCell align="center">{player.max_score}</TableCell>

                            <TableCell
                                align="center"
                                style={{
                                    display: "flex",
                                    alignItems: "center",
                                    justifyContent: "center"
                                }}
                            >
                                <Avatar alt="" src={`http://localhost:5000/player/get_profile_image/${player.id}`} />
                            </TableCell>

                        </TableRow>
                    ))}
                </TableBody>
            </Table>
        </TableContainer>
    );
}