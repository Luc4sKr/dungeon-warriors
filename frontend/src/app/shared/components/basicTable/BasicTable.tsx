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

export const BasicTable = () => {
    const defaultPlayer: Player[] = []
    const [players, setPlayers] = useState(defaultPlayer);

    useEffect(() => {
        api.get("/players")
            .then((response) => {
                setPlayers(response.data.data);
            })
    })

    return (
        <TableContainer component={Paper}>
            <Table sx={{ minWidth: 650 }} aria-label="Player table">
                <TableHead>
                    <TableRow>
                        <TableCell>Id</TableCell>
                        <TableCell align="right">Username</TableCell>
                        <TableCell align="right">Email</TableCell>
                        <TableCell align="right">Coins(g)</TableCell>
                        <TableCell align="right">Max Score</TableCell>
                    </TableRow>
                </TableHead>
                <TableBody>
                    {players.map((player) => (
                        <TableRow
                            key={player.id}
                            sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
                        >
                            <TableCell component="th" scope="row">
                                {player.id}
                            </TableCell>
                            <TableCell align="right">{player.username}</TableCell>
                            <TableCell align="right">{player.email}</TableCell>
                            <TableCell align="right">{player.coins}</TableCell>
                            <TableCell align="right">{player.max_score}</TableCell>
                        </TableRow>
                    ))}
                </TableBody>
            </Table>
        </TableContainer>
    );
}