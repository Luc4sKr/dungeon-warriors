import { Route, Routes, BrowserRouter, Navigate } from "react-router-dom";
import { Header } from "../shared/components/header/Header";
import { Home, Players, Register } from "../pages";

export const RoutesPath = () => {
    return (
        <BrowserRouter>
            <Header />
            <Routes>
                <Route path="/" Component={Home} />
                <Route path="/players" Component={Players}/>
                <Route path="/register" Component={Register}/>
                <Route path="*" Component={() => <Navigate to="/" />}/>
            </Routes>
        </BrowserRouter>
    );
}