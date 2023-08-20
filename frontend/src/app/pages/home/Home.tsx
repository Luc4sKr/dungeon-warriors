import { Button } from "../../shared/components/button/Button"

import "./Home.css"

export const Home = () => {
    return (
        <div>
            <div className="home-container">
                <p>Click the button and play right now</p>
                <Button>Play now</Button>
            </div>
        </div>
    )
}
