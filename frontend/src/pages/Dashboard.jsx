import { useEffect, useState } from "react";
import api from "../services/api";

function Dashboard() {
    const [dashboard, setDashboard] = useState(null);

    useEffect(() => {
        api.get("/dashboard")
            .then((response) => {
                setDashboard(response.data);
            })
            .catch((error) => {
                console.error(error);
            });
    }, []);

    if (!dashboard) {
        return (
            <h2 className="text-xl font-semibold">
                Loading dashboard...
            </h2>
        );
    }

    return (
        <div>

            <h1 className="text-3xl font-bold mb-8">
                Dashboard
            </h1>

            <div className="grid grid-cols-2 md:grid-cols-4 gap-6">

                <div className="bg-white rounded-lg shadow p-6">
                    <h3 className="text-gray-500">Revenue</h3>
                    <p className="text-3xl font-bold mt-2">
                        ₹ {dashboard.total_revenue}
                    </p>
                </div>

                <div className="bg-white rounded-lg shadow p-6">
                    <h3 className="text-gray-500">Orders</h3>
                    <p className="text-3xl font-bold mt-2">
                        {dashboard.total_orders}
                    </p>
                </div>

                <div className="bg-white rounded-lg shadow p-6">
                    <h3 className="text-gray-500">Artists</h3>
                    <p className="text-3xl font-bold mt-2">
                        {dashboard.total_artists}
                    </p>
                </div>

                <div className="bg-white rounded-lg shadow p-6">
                    <h3 className="text-gray-500">Artworks</h3>
                    <p className="text-3xl font-bold mt-2">
                        {dashboard.total_artworks}
                    </p>
                </div>

            </div>

        </div>
    );
}

export default Dashboard;