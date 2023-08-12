import { Link } from "react-router-dom";

import "./style.css";

export const Navbar = () => {
    return (
        <div className="navbar-container">
            <ul className="navbar-list">
                <li className="navbar-item">
                    <Link to={"/"} className="link">Home</Link>
                </li>
                <li className="navbar-item">
                    <Link to={"/"} className="link">Home</Link>
                </li>
                <li className="navbar-item">
                    <Link to={"/"} className="link">Home</Link>
                </li>
                <li className="navbar-item">
                    <Link to={"/"} className="link">Home</Link>
                </li>
            </ul>
        </div>
    )
}
