import { Link } from "react-router-dom";

import "./style.css";
import { Typography } from "@mui/material";

export const Navbar = () => {
    return (
        <div className="navbar-container">
            <ul className="navbar-list">
                <li className="navbar-item">
                    <Typography variant="h4">
                        <Link to={"/"} className="link">Home</Link>
                    </Typography>
                </li>
                <li className="navbar-item">
                    <Typography variant="h4">
                        <Link to={"/players"} className="link">Players</Link>
                    </Typography>
                </li>
                <li className="navbar-item">
                    <Typography variant="h4">
                        <Link to={"/register"} className="link">Register</Link>
                    </Typography>
                </li>
                <li className="navbar-item">
                    <Typography variant="h4">
                        <Link to={"/login"} className="link">Login</Link>
                    </Typography>
                </li>
            </ul>
        </div>
    )
}
