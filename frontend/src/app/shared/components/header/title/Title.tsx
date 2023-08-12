import { Link } from "react-router-dom";

import "./style.css";

export const Title = () => {
    return (
        <Link to={"/"} className="link">
            <div className="title-container">
                <h1 className="title">Dungeon</h1>
                <h1 className="title">Warriors</h1>
            </div>
        </Link>
    )
}