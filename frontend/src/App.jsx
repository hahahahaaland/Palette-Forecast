import Navbar from "./components/Navbar";

import Dashboard from "./pages/Dashboard";
import Artists from "./pages/Artists";
import Artworks from "./pages/Artworks";
import Orders from "./pages/Orders";
import Analytics from "./pages/Analytics";

import { Routes, Route } from "react-router-dom";

function App() {
    return (
        <div className="min-h-screen bg-rose-100">

            <Navbar />

            <div className="p-8">

                <Routes>

                    <Route path="/" element={<Dashboard />} />

                    <Route path="/artists" element={<Artists />} />

                    <Route path="/artworks" element={<Artworks />} />

                    <Route path="/orders" element={<Orders />} />

                    <Route path="/analytics" element={<Analytics />} />

                </Routes>

            </div>

        </div>
    );
}

export default App;