import { Link } from "react-router-dom";

function Navbar() {
    return (
        <nav className="bg-blue-950 shadow-lg">

            <div className="max-w-7xl mx-auto flex justify-between items-center px-8 py-4">

                <h1 className="text-3xl text-white logo-font">
                    Palette Forecast
                </h1>

                <div className="flex gap-8 text-white font-medium">

                    <Link to="/" className="hover:text-blue-400 transition">
                        Dashboard
                    </Link>

                    <Link to="/artists" className="hover:text-blue-400 transition">
                        Artists
                    </Link>

                    <Link to="/artworks" className="hover:text-blue-400 transition">
                        Artworks
                    </Link>

                    <Link to="/orders" className="hover:text-blue-400 transition">
                        Orders
                    </Link>

                    <Link to="/analytics" className="hover:text-blue-400 transition">
                        Analytics
                    </Link>

                </div>

            </div>

        </nav>
    );
}

export default Navbar;