import { Header } from "../../shared/components/header/Header"
import { Button } from "../../shared/components/button/Button"

import "./style.css"

export const Home = () => {
    return (
        <div>
            <Header />

            <div className="home-container">
                <p>Click the button and play right now</p>
                <Button>Play now</Button>
            </div>
        </div>
    )
}
