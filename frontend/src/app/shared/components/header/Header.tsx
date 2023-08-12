import { Title } from "./title/Title.jsx";
import { Navbar } from "./navbar/Navbar.jsx";
import "./style.css";

export const Header = () => {
    return (
        <header className="header-top">
            <Title />
            <Navbar />
        </header>
    );
}