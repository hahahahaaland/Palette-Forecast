import { useEffect, useState } from "react";
import { ResponsiveContainer, PieChart, Pie, Cell, Tooltip, Legend } from "recharts";
import api from "../services/api";
import BrushDivider from "../components/BrushDivider";
import PaletteMark from "../components/icons/PaletteMark";
import { NAVY, PINK_DEEP } from "../utils/chartTheme";

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
            <h2 className="text-xl font-semibold text-navy">
                Loading dashboard...
            </h2>
        );
    }

    const statusBreakdown = [
        { name: "Available", value: dashboard.available_artworks || 0 },
        { name: "Sold", value: dashboard.sold_artworks || 0 },
    ];
    const hasStatusData = statusBreakdown.some((s) => s.value > 0);

    return (
        <div>
            <div className="flex items-center gap-3 mb-2">
                <PaletteMark className="w-9 h-9 hidden sm:block" />
                <h1 className="text-3xl font-bold text-navy">Dashboard</h1>
            </div>
            <BrushDivider className="w-48 mb-8" />

            <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">

                <div className="lg:col-span-2 grid grid-cols-2 gap-6 content-start">

                    <div className="bg-white rounded-lg shadow border border-babypink p-6">
                        <h3 className="hand-font text-navy/70">Revenue</h3>
                        <p className="text-3xl font-bold text-navy mt-2">
                            ₹ {dashboard.total_revenue}
                        </p>
                    </div>

                    <div className="bg-white rounded-lg shadow border border-babypink p-6">
                        <h3 className="hand-font text-navy/70">Orders</h3>
                        <p className="text-3xl font-bold text-navy mt-2">
                            {dashboard.total_orders}
                        </p>
                    </div>

                    <div className="bg-white rounded-lg shadow border border-babypink p-6">
                        <h3 className="hand-font text-navy/70">Artists</h3>
                        <p className="text-3xl font-bold text-navy mt-2">
                            {dashboard.total_artists}
                        </p>
                    </div>

                    <div className="bg-white rounded-lg shadow border border-babypink p-6">
                        <h3 className="hand-font text-navy/70">Artworks</h3>
                        <p className="text-3xl font-bold text-navy mt-2">
                            {dashboard.total_artworks}
                        </p>
                    </div>

                </div>

                <div className="bg-white rounded-lg shadow border border-babypink p-6">
                    <h3 className="hand-font text-navy/70 mb-2">Available vs sold</h3>
                    {hasStatusData ? (
                        <ResponsiveContainer width="100%" height={200}>
                            <PieChart>
                                <Pie
                                    data={statusBreakdown}
                                    dataKey="value"
                                    nameKey="name"
                                    innerRadius={40}
                                    outerRadius={75}
                                    paddingAngle={3}
                                >
                                    <Cell fill={PINK_DEEP} />
                                    <Cell fill={NAVY} />
                                </Pie>
                                <Tooltip contentStyle={{ backgroundColor: "#fff", border: "1px solid " + NAVY, borderRadius: "0.5rem", fontSize: "13px" }} />
                                <Legend wrapperStyle={{ fontSize: "12px" }} />
                            </PieChart>
                        </ResponsiveContainer>
                    ) : (
                        <p className="text-navy/50 text-sm">No artworks yet.</p>
                    )}
                </div>

            </div>

        </div>
    );
}

export default Dashboard;
