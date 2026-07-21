import { useEffect, useState } from "react";
import {
    ResponsiveContainer,
    AreaChart,
    Area,
    XAxis,
    YAxis,
    CartesianGrid,
    Tooltip,
    PieChart,
    Pie,
    Cell,
    BarChart,
    Bar,
    Legend,
} from "recharts";
import api from "../services/api";
import BrushDivider from "../components/BrushDivider";
import PaletteMark from "../components/icons/PaletteMark";
import { NAVY, PINK_DEEP, PINK_SOFT, NAVY_SOFT, CHART_COLORS, AXIS_STYLE } from "../utils/chartTheme";

function Analytics() {
    const [revenue, setRevenue] = useState({});
    const [topArtist, setTopArtist] = useState({});
    const [topStyle, setTopStyle] = useState({});
    const [topMedium, setTopMedium] = useState({});
    const [giftWrap, setGiftWrap] = useState({});
    const [commissions, setCommissions] = useState({});
    const [status, setStatus] = useState({});
    const [artworks, setArtworks] = useState([]);
    const [orders, setOrders] = useState([]);
    const [loaded, setLoaded] = useState(false);

    useEffect(() => {
        Promise.all([
            api.get("/analytics/revenue"),
            api.get("/analytics/top-artist"),
            api.get("/analytics/top-style"),
            api.get("/analytics/top-medium"),
            api.get("/analytics/gift-wrap"),
            api.get("/analytics/commissions"),
            api.get("/analytics/status"),
            api.get("/artworks"),
            api.get("/orders"),
        ])
            .then(
                ([
                    revenueRes,
                    topArtistRes,
                    topStyleRes,
                    topMediumRes,
                    giftWrapRes,
                    commissionsRes,
                    statusRes,
                    artworksRes,
                    ordersRes,
                ]) => {
                    setRevenue(revenueRes.data);
                    setTopArtist(topArtistRes.data);
                    setTopStyle(topStyleRes.data);
                    setTopMedium(topMediumRes.data);
                    setGiftWrap(giftWrapRes.data);
                    setCommissions(commissionsRes.data);
                    setStatus(statusRes.data);
                    setArtworks(artworksRes.data);
                    setOrders(ordersRes.data);
                    setLoaded(true);
                }
            )
            .catch((error) => console.error(error));
    }, []);

    // --- client-side aggregation, no backend changes needed ---

    const statusData = Object.entries(status).map(([name, value]) => ({
        name,
        value,
    }));

    const styleData = Object.values(
        artworks.reduce((acc, a) => {
            const key = a.style_name || "Unknown";
            acc[key] = acc[key] || { name: key, count: 0 };
            acc[key].count += 1;
            return acc;
        }, {})
    ).sort((a, b) => b.count - a.count);

    const mediumData = Object.values(
        artworks.reduce((acc, a) => {
            const key = a.medium_name || "Unknown";
            acc[key] = acc[key] || { name: key, count: 0 };
            acc[key].count += 1;
            return acc;
        }, {})
    ).sort((a, b) => b.count - a.count);

    const revenueTrend = Object.entries(
        orders.reduce((acc, o) => {
            const date = o.order_date || "Unknown";
            acc[date] = (acc[date] || 0) + Number(o.final_price || 0);
            return acc;
        }, {})
    )
        .map(([date, total]) => ({ date, total }))
        .sort((a, b) => a.date.localeCompare(b.date));

    const giftWrapData = [
        { name: "Gift wrapped", value: giftWrap["1"] ?? giftWrap[1] ?? 0 },
        { name: "Standard", value: giftWrap["0"] ?? giftWrap[0] ?? 0 },
    ];

    const commissionData = [
        { name: "Commissioned", value: commissions["1"] ?? commissions[1] ?? 0 },
        { name: "Off the shelf", value: commissions["0"] ?? commissions[0] ?? 0 },
    ];

    const tooltipStyle = {
        backgroundColor: "#ffffff",
        border: "1px solid " + NAVY,
        borderRadius: "0.5rem",
        fontSize: "13px",
    };

    return (
        <div>
            <div className="flex items-center gap-3 mb-2">
                <PaletteMark className="w-9 h-9 hidden sm:block" />
                <h1 className="text-3xl font-bold text-navy">Analytics Dashboard</h1>
            </div>
            <BrushDivider className="w-48 mb-8" />

            {/* Stat cards */}
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 mb-10">

                <div className="bg-white p-6 rounded-lg shadow border border-babypink">
                    <h3 className="hand-font text-navy/70 mb-2">Total Revenue</h3>
                    <p className="text-3xl font-bold text-navy">
                        ₹ {revenue.total_revenue?.toLocaleString?.() ?? 0}
                    </p>
                </div>

                <div className="bg-white p-6 rounded-lg shadow border border-babypink">
                    <h3 className="hand-font text-navy/70 mb-2">Top Artist</h3>
                    <p className="text-2xl font-semibold text-navy">
                        {topArtist.top_artist || "—"}
                    </p>
                </div>

                <div className="bg-white p-6 rounded-lg shadow border border-babypink">
                    <h3 className="hand-font text-navy/70 mb-2">Top Style</h3>
                    <p className="text-2xl font-semibold text-navy">
                        {topStyle.top_style || "—"}
                    </p>
                </div>

                <div className="bg-white p-6 rounded-lg shadow border border-babypink">
                    <h3 className="hand-font text-navy/70 mb-2">Top Medium</h3>
                    <p className="text-2xl font-semibold text-navy">
                        {topMedium.top_medium || "—"}
                    </p>
                </div>

                <div className="bg-white p-6 rounded-lg shadow border border-babypink">
                    <h3 className="hand-font text-navy/70 mb-2">Gift Wrap Orders</h3>
                    <p className="text-2xl font-semibold text-navy">
                        {giftWrapData[0].value} of {giftWrapData[0].value + giftWrapData[1].value}
                    </p>
                </div>

                <div className="bg-white p-6 rounded-lg shadow border border-babypink">
                    <h3 className="hand-font text-navy/70 mb-2">Commission Orders</h3>
                    <p className="text-2xl font-semibold text-navy">
                        {commissionData[0].value} of {commissionData[0].value + commissionData[1].value}
                    </p>
                </div>

            </div>

            {/* Revenue trend */}
            <div className="bg-white p-6 rounded-lg shadow border border-babypink mb-8">
                <h3 className="hand-font text-navy/70 mb-4">Revenue over time</h3>
                {revenueTrend.length === 0 && loaded ? (
                    <p className="text-navy/50 text-sm">No orders yet — this chart will fill in as orders come through.</p>
                ) : (
                    <ResponsiveContainer width="100%" height={260}>
                        <AreaChart data={revenueTrend} margin={{ top: 10, right: 20, left: 0, bottom: 0 }}>
                            <defs>
                                <linearGradient id="revenueFill" x1="0" y1="0" x2="0" y2="1">
                                    <stop offset="5%" stopColor={PINK_DEEP} stopOpacity={0.45} />
                                    <stop offset="95%" stopColor={PINK_DEEP} stopOpacity={0.03} />
                                </linearGradient>
                            </defs>
                            <CartesianGrid strokeDasharray="3 3" stroke="#ffe4e6" />
                            <XAxis dataKey="date" tick={AXIS_STYLE} />
                            <YAxis tick={AXIS_STYLE} />
                            <Tooltip contentStyle={tooltipStyle} formatter={(v) => [`₹ ${v}`, "Revenue"]} />
                            <Area
                                type="monotone"
                                dataKey="total"
                                stroke={NAVY}
                                strokeWidth={2.5}
                                fill="url(#revenueFill)"
                            />
                        </AreaChart>
                    </ResponsiveContainer>
                )}
            </div>

            {/* Breakdown charts */}
            <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">

                <div className="bg-white p-6 rounded-lg shadow border border-babypink">
                    <h3 className="hand-font text-navy/70 mb-4">Artwork status</h3>
                    {statusData.length === 0 ? (
                        <p className="text-navy/50 text-sm">No artworks yet.</p>
                    ) : (
                        <ResponsiveContainer width="100%" height={220}>
                            <PieChart>
                                <Pie
                                    data={statusData}
                                    dataKey="value"
                                    nameKey="name"
                                    innerRadius={45}
                                    outerRadius={80}
                                    paddingAngle={3}
                                >
                                    {statusData.map((entry, index) => (
                                        <Cell key={entry.name} fill={CHART_COLORS[index % CHART_COLORS.length]} />
                                    ))}
                                </Pie>
                                <Tooltip contentStyle={tooltipStyle} />
                                <Legend wrapperStyle={{ fontSize: "12px" }} />
                            </PieChart>
                        </ResponsiveContainer>
                    )}
                </div>

                <div className="bg-white p-6 rounded-lg shadow border border-babypink">
                    <h3 className="hand-font text-navy/70 mb-4">Style popularity</h3>
                    {styleData.length === 0 ? (
                        <p className="text-navy/50 text-sm">No artworks yet.</p>
                    ) : (
                        <ResponsiveContainer width="100%" height={220}>
                            <BarChart data={styleData} margin={{ top: 5, right: 10, left: -20, bottom: 0 }}>
                                <CartesianGrid strokeDasharray="3 3" stroke="#ffe4e6" vertical={false} />
                                <XAxis dataKey="name" tick={{ ...AXIS_STYLE, fontSize: 10 }} interval={0} angle={-30} textAnchor="end" height={50} />
                                <YAxis tick={AXIS_STYLE} allowDecimals={false} />
                                <Tooltip contentStyle={tooltipStyle} />
                                <Bar dataKey="count" fill={PINK_DEEP} radius={[4, 4, 0, 0]} />
                            </BarChart>
                        </ResponsiveContainer>
                    )}
                </div>

                <div className="bg-white p-6 rounded-lg shadow border border-babypink">
                    <h3 className="hand-font text-navy/70 mb-4">Medium distribution</h3>
                    {mediumData.length === 0 ? (
                        <p className="text-navy/50 text-sm">No artworks yet.</p>
                    ) : (
                        <ResponsiveContainer width="100%" height={220}>
                            <BarChart data={mediumData} margin={{ top: 5, right: 10, left: -20, bottom: 0 }}>
                                <CartesianGrid strokeDasharray="3 3" stroke="#ffe4e6" vertical={false} />
                                <XAxis dataKey="name" tick={{ ...AXIS_STYLE, fontSize: 10 }} interval={0} angle={-30} textAnchor="end" height={50} />
                                <YAxis tick={AXIS_STYLE} allowDecimals={false} />
                                <Tooltip contentStyle={tooltipStyle} />
                                <Bar dataKey="count" fill={NAVY_SOFT} radius={[4, 4, 0, 0]} />
                            </BarChart>
                        </ResponsiveContainer>
                    )}
                </div>

            </div>
        </div>
    );
}

export default Analytics;
