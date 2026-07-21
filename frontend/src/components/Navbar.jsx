import { Link } from "react-router-dom";
import PaletteMark from "./icons/PaletteMark";

function Navbar() {
    return (
        <nav className="bg-navy shadow-lg">

            <div className="max-w-7xl mx-auto flex justify-between items-center px-8 py-4">

                <Link to="/" className="flex items-center gap-3">
                    <PaletteMark className="w-9 h-9" />
                    <h1 className="text-3xl text-white logo-font">
                        Palette Forecast
                    </h1>
                </Link>

                <div className="flex gap-8 text-white font-medium">

                    <Link to="/" className="hover:text-babypink-soft transition">
                        Dashboard
                    </Link>

                    <Link to="/artists" className="hover:text-babypink-soft transition">
                        Artists
                    </Link>

                    <Link to="/artworks" className="hover:text-babypink-soft transition">
                        Artworks
                    </Link>

                    <Link to="/orders" className="hover:text-babypink-soft transition">
                        Orders
                    </Link>

                    <Link to="/analytics" className="hover:text-babypink-soft transition">
                        Analytics
                    </Link>

                </div>

            </div>

        </nav>
    );
}

export default Navbar;
