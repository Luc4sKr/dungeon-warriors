import { HomeContainer } from "./Home.style"
import { Button } from "../../shared/components/button/Button"

export const Home = () => {

    const playNow = (e: any) => {
        e.preventDefault();
        window.open("https://github.com/Luc4sKr/dungeon-warriors");
    }


    return (
        <HomeContainer>
            <p>Click the button and play right now</p>
            <Button onClick={playNow}>Play now</Button>
        </HomeContainer>
    )
}
