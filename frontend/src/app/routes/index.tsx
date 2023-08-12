import { Route, Routes, BrowserRouter, Navigate } from "react-router-dom";
import { Home } from "../pages";

export const RoutesPaht = () => {
    return (
        <BrowserRouter>
            <Routes>
                <Route path="/" Component={Home} />
                <Route path="*" Component={() => <Navigate to="/" />}/>
            </Routes>
        </BrowserRouter>
    );
}